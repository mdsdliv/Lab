# db.py
import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def get_or_create_player(username):
    """Возвращает ID игрока. Если игрока нет, создает его."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Пытаемся вставить нового игрока
        cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING;", (username,))
        # Получаем ID игрока
        cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
        player_id = cur.fetchone()[0]
        conn.commit()
        return player_id
    except Exception as e:
        print(f"DB Error (get_or_create_player): {e}")
        return None
    finally:
        cur.close()
        conn.close()

def get_personal_best(player_id):
    """Возвращает максимальный рекорд игрока по его ID."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s;", (player_id,))
        res = cur.fetchone()[0]
        return res if res is not None else 0
    except Exception as e:
        print(f"DB Error (get_personal_best): {e}")
        return 0
    finally:
        cur.close()
        conn.close()

def save_game_result(player_id, score, level):
    """Сохраняет данные сессии после Game Over."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s);",
            (player_id, score, level)
        )
        conn.commit()
    except Exception as e:
        print(f"DB Error (save_game_result): {e}")
    finally:
        cur.close()
        conn.close()

def get_leaderboard():
    """Возвращает топ-10 результатов: (имя, очки, уровень)."""
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = """
            SELECT p.username, s.score, s.level_reached 
            FROM game_sessions s 
            JOIN players p ON s.player_id = p.id 
            ORDER BY s.score DESC 
            LIMIT 10;
        """
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print(f"DB Error (get_leaderboard): {e}")
        return []
    finally:
        cur.close()
        conn.close()
        