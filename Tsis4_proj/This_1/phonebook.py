"""
phonebook.py  –  Practice 9: full-featured phone book CLI
"""
import csv
import json
import os
from connect import get_connection

PAGE_SIZE = 5  # rows per page


# ─────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────

def print_contacts(rows):
    """Pretty-print a list of contact rows."""
    if not rows:
        print("  (no contacts)")
        return
    print(f"\n{'ID':<5} {'Name':<20} {'Email':<25} {'Birthday':<12} {'Group':<10}  Phones")
    print("─" * 90)
    for r in rows:
        cid, name, email, bday, grp, phones = r
        phone_str = " | ".join(f"{p}({t})" for p, t in (phones or []))
        print(f"{cid:<5} {str(name):<20} {str(email or ''):<25} "
              f"{str(bday or ''):<12} {str(grp or ''):<10}  {phone_str}")
    print()


def fetch_contacts_full(conn, where="", params=(), order="c.name", offset=0, limit=PAGE_SIZE):
    """Return contacts with their phones aggregated."""
    sql = f"""
        SELECT c.id, c.name, c.email, c.birthday, g.name,
               ARRAY_AGG(ROW(p.phone, p.type)) FILTER (WHERE p.id IS NOT NULL)
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        LEFT JOIN phones p ON p.contact_id = c.id
        {where}
        GROUP BY c.id, c.name, c.email, c.birthday, g.name
        ORDER BY {order}
        LIMIT %s OFFSET %s
    """
    with conn.cursor() as cur:
        cur.execute(sql, params + (limit, offset))
        return cur.fetchall()


def count_contacts(conn, where="", params=()):
    sql = f"""
        SELECT COUNT(DISTINCT c.id)
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        LEFT JOIN phones p ON p.contact_id = c.id
        {where}
    """
    with conn.cursor() as cur:
        cur.execute(sql, params)
        return cur.fetchone()[0]


# ─────────────────────────────────────────────
#  3.2  Search / Filter / Sort / Paginate
# ─────────────────────────────────────────────

def menu_search_filter(conn):
    print("\n── Search & Filter ──")
    group_filter = input("Filter by group (leave blank to skip): ").strip()
    email_filter = input("Search by email (partial, blank to skip): ").strip()
    sort_choice  = input("Sort by [name / birthday / date] (default: name): ").strip() or "name"

    sort_map = {"name": "c.name", "birthday": "c.birthday", "date": "c.created_at"}
    order_col = sort_map.get(sort_choice, "c.name")

    conditions, params = [], []

    if group_filter:
        conditions.append("g.name ILIKE %s")
        params.append(f"%{group_filter}%")
    if email_filter:
        conditions.append("c.email ILIKE %s")
        params.append(f"%{email_filter}%")

    where = ("WHERE " + " AND ".join(conditions)) if conditions else ""

    # ── Paginated navigation ──
    offset = 0
    total  = count_contacts(conn, where, tuple(params))
    total_pages = max(1, (total + PAGE_SIZE - 1) // PAGE_SIZE)

    while True:
        page = offset // PAGE_SIZE + 1
        rows = fetch_contacts_full(conn, where, tuple(params), order_col, offset)
        print(f"\nPage {page}/{total_pages}  ({total} contacts total)")
        print_contacts(rows)

        nav = input("[next/prev/quit]: ").strip().lower()
        if nav == "next":
            if offset + PAGE_SIZE < total:
                offset += PAGE_SIZE
            else:
                print("Already on the last page.")
        elif nav == "prev":
            if offset > 0:
                offset -= PAGE_SIZE
            else:
                print("Already on the first page.")
        elif nav == "quit":
            break


# ─────────────────────────────────────────────
#  3.3  Export / Import JSON
# ─────────────────────────────────────────────

def export_to_json(conn, filename="contacts_export.json"):
    rows = fetch_contacts_full(conn, limit=100_000, offset=0)
    data = []
    for cid, name, email, bday, grp, phones in rows:
        data.append({
            "id":       cid,
            "name":     name,
            "email":    email,
            "birthday": str(bday) if bday else None,
            "group":    grp,
            "phones":   [{"phone": p, "type": t} for p, t in (phones or [])],
        })
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Exported {len(data)} contacts → {filename}")


def import_from_json(conn, filename="contacts_export.json"):
    if not os.path.exists(filename):
        print(f"  File not found: {filename}")
        return

    with open(filename, encoding="utf-8") as f:
        data = json.load(f)

    with conn.cursor() as cur:
        for item in data:
            name = item.get("name", "").strip()
            if not name:
                continue

            # Check duplicate
            cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
            existing = cur.fetchone()

            if existing:
                choice = input(f"  '{name}' already exists – [skip/overwrite]: ").strip().lower()
                if choice != "overwrite":
                    print(f"    Skipped '{name}'")
                    continue
                # Overwrite: delete old phones, update contact
                cur.execute("DELETE FROM phones WHERE contact_id = %s", (existing[0],))
                cur.execute("""
                    UPDATE contacts SET email=%s, birthday=%s, group_id=(
                        SELECT id FROM groups WHERE name=%s LIMIT 1)
                    WHERE id=%s
                """, (item.get("email"), item.get("birthday"), item.get("group"), existing[0]))
                contact_id = existing[0]
            else:
                # Ensure group exists
                grp = item.get("group")
                if grp:
                    cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (grp,))
                cur.execute("""
                    INSERT INTO contacts (name, email, birthday, group_id)
                    VALUES (%s, %s, %s, (SELECT id FROM groups WHERE name=%s LIMIT 1))
                    RETURNING id
                """, (name, item.get("email"), item.get("birthday"), grp))
                contact_id = cur.fetchone()[0]

            # Insert phones
            for ph in item.get("phones", []):
                cur.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                    (contact_id, ph["phone"], ph.get("type", "mobile"))
                )

        conn.commit()
    print(f"  Import complete — {len(data)} records processed.")


# ─────────────────────────────────────────────
#  3.3  Extended CSV import
# ─────────────────────────────────────────────

def import_from_csv(conn, filename="contacts.csv"):
    """
    CSV columns (all optional except name):
      name, phone, phone_type, email, birthday, group
    """
    if not os.path.exists(filename):
        print(f"  File not found: {filename}")
        return

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with conn.cursor() as cur:
        imported = 0
        for row in rows:
            name = row.get("name", "").strip()
            if not name:
                continue

            grp = row.get("group", "Other").strip() or "Other"
            cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (grp,))

            cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
            existing = cur.fetchone()
            if existing:
                contact_id = existing[0]
                cur.execute("""
                    UPDATE contacts SET email=%s, birthday=%s,
                        group_id=(SELECT id FROM groups WHERE name=%s LIMIT 1)
                    WHERE id=%s
                """, (row.get("email") or None, row.get("birthday") or None, grp, contact_id))
            else:
                cur.execute("""
                    INSERT INTO contacts (name, email, birthday, group_id)
                    VALUES (%s, %s, %s, (SELECT id FROM groups WHERE name=%s LIMIT 1))
                    RETURNING id
                """, (name, row.get("email") or None, row.get("birthday") or None, grp))
                contact_id = cur.fetchone()[0]

            phone = row.get("phone", "").strip()
            ptype = row.get("phone_type", "mobile").strip() or "mobile"
            if phone:
                cur.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                    (contact_id, phone, ptype)
                )
            imported += 1

        conn.commit()
    print(f"  CSV import done — {imported} rows processed.")


# ─────────────────────────────────────────────
#  Stored procedure callers
# ─────────────────────────────────────────────

def call_add_phone(conn):
    name  = input("Contact name: ").strip()
    phone = input("Phone number: ").strip()
    ptype = input("Type (home/work/mobile): ").strip()
    try:
        with conn.cursor() as cur:
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        conn.commit()
        print("  Phone added.")
    except Exception as e:
        conn.rollback()
        print(f"  Error: {e}")



def call_move_to_group(conn):
    name  = input("Contact name: ").strip()
    group = input("Group name: ").strip()
    try:
        with conn.cursor() as cur:
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
        conn.commit()
        print(f"  Moved '{name}' → '{group}'.")
    except Exception as e:
        conn.rollback()
        print(f"  Error: {e}")


def call_search_contacts(conn):
    query = input("Search query: ").strip()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        rows = cur.fetchall()
    if not rows:
        print("  No results.")
    else:
        print(f"\n{'ID':<5} {'Name':<20} {'Email':<25} {'Birthday':<12} {'Group'}")
        print("─" * 70)
        for r in rows:
            print(f"{r[0]:<5} {str(r[1]):<20} {str(r[2] or ''):<25} {str(r[3] or ''):<12} {r[4] or ''}")


# ─────────────────────────────────────────────
#  Main menu
# ─────────────────────────────────────────────

def main():
    conn = get_connection()
    print("=== Phone Book  (Practice 9) ===")

    while True:
        print("""
1. Search / Filter / Sort contacts  (with pagination)
2. Export contacts → JSON
3. Import contacts ← JSON
4. Import contacts ← CSV
5. Add phone number  (call add_phone procedure)
6. Move contact to group  (call move_to_group procedure)
7. Full-text search  (call search_contacts function)
0. Exit
""")
        choice = input("Choice: ").strip()

        if choice == "1":
            menu_search_filter(conn)
        elif choice == "2":
            fname = input("Output filename [contacts_export.json]: ").strip() or "contacts_export.json"
            export_to_json(conn, fname)
        elif choice == "3":
            fname = input("Input filename [contacts_export.json]: ").strip() or "contacts_export.json"
            import_from_json(conn, fname)
        elif choice == "4":
            fname = input("CSV filename [contacts.csv]: ").strip() or "contacts.csv"
            import_from_csv(conn, fname)
        elif choice == "5":
            call_add_phone(conn)
        elif choice == "6":
            call_move_to_group(conn)
        elif choice == "7":
            call_search_contacts(conn)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Unknown option.")

    conn.close()


if __name__ == "__main__":
    main()
