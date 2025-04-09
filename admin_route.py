from flask import Blueprint, request, jsonify
import sqlite3

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/admin/start_game", methods=["POST"])
def start_game():
    data = request.get_json()

    if data.get("admin_password") != "secretpassword":
        return jsonify({"error": "Invalid password"}), 403

    word = data.get("word")
    hints = data.get("hints")

    if not word or not hints or len(hints) != 10:
        return jsonify({"error": "Word and exactly 10 hints are 
required"}), 400
@admin_bp.route("/admin/current_game", methods=["GET"])
def current_game():
    conn = sqlite3.connect("bonkword.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT word, hints, fail_count, pot_bonk, guess_price_bonk
        FROM games
        ORDER BY id DESC
        LIMIT 1
    ''')

    row = cursor.fetchone()
    conn.close()

    if row:
        word, hints, fail_count, pot_bonk, guess_price_bonk = row
        return jsonify({
            "word": word,
            "hints": hints.split(","),
            "fail_count": fail_count,
            "pot_bonk": pot_bonk,
            "guess_price_bonk": guess_price_bonk
        })
    else:
        return jsonify({"error": "No game found"}), 404

    conn = sqlite3.connect("bonkword.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO games (word, hints, fail_count, pot_bonk, 
guess_price_bonk)
        VALUES (?, ?, ?, ?, ?)
    ''', (word.lower(), ','.join(hints), 0, 0, 100000))

    conn.commit()
    conn.close()

    return jsonify({"message": "Game started", "word": word, "hints": 
hints}), 200

@admin_bp.route("/admin/current_game", methods=["GET"])
def current_game():
    conn = sqlite3.connect("bonkword.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "id": row[0],
            "word": row[1],
            "hints": row[2],
            "fail_count": row[3],
            "pot_bonk": row[4],
            "guess_price_bonk": row[5]
        })
    else:
        return jsonify({"error": "No game found"}), 404

