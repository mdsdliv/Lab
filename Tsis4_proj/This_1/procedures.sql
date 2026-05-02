-- ============================================================
--  procedures.sql  –  Stored procedures & functions (Practice 9)
--  Do NOT duplicate procedures already defined in Practice 8.
-- ============================================================

-- -------------------------------------------------------
-- 1. add_phone(name, phone, type)
--    Adds a phone number to an existing contact.
-- -------------------------------------------------------
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone        VARCHAR,
    p_type         VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INTEGER;
BEGIN
    -- Try to find existing contact
    SELECT id INTO v_id FROM contacts WHERE name = p_contact_name LIMIT 1;

    -- If not found — create automatically
    IF v_id IS NULL THEN
        INSERT INTO contacts (name) VALUES (p_contact_name) RETURNING id INTO v_id;
        RAISE NOTICE 'Contact "%" did not exist — created automatically', p_contact_name;
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_id, p_phone, p_type);
END;
$$;


-- -------------------------------------------------------
-- 2. move_to_group(contact_name, group_name)
--    Moves a contact to a group; creates the group if needed.
-- -------------------------------------------------------
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name   VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INTEGER;
    v_group_id   INTEGER;
BEGIN
    -- Find contact
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name LIMIT 1;
    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
    END IF;

    -- Find or create group
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name LIMIT 1;
    IF v_group_id IS NULL THEN
        INSERT INTO groups (name) VALUES (p_group_name) RETURNING id INTO v_group_id;
    END IF;

    UPDATE contacts SET group_id = v_group_id WHERE id = v_contact_id;
END;
$$;


-- -------------------------------------------------------
-- 3. search_contacts(query)  →  TABLE
--    Searches name, email, AND all phone numbers.
-- -------------------------------------------------------
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id       INTEGER,
    name     VARCHAR,
    email    VARCHAR,
    birthday DATE,
    grp      VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name AS grp
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE
        c.name  ILIKE '%' || p_query || '%'
        OR c.email ILIKE '%' || p_query || '%'
        OR p.phone ILIKE '%' || p_query || '%'
    ORDER BY c.name;
END;
$$;