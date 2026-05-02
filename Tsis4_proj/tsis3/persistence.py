import json
import os

L_FILE = "leaderboard.json"
S_FILE = "settings.json"

def load_json(path, default):
    if not os.path.exists(path): return default
    with open(path, 'r') as f:
        try: return json.load(f)
        except: return default

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_leaderboard(): return load_json(L_FILE, [])

def save_leaderboard(data): save_json(L_FILE, data)

def add_entry(leaderboard, name, score, distance):
    leaderboard.append({"name": name, "score": score, "distance": int(distance)})
    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:10]
    save_leaderboard(leaderboard)
    return leaderboard

def load_settings():
    return load_json(S_FILE, {"username": "", "sound": True, "car_color": "Red", "difficulty": "Normal"})

def save_settings(settings): save_json(S_FILE, settings)