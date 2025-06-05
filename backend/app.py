from flask import Flask, jsonify, render_template
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)


DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "dotastat")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "1234")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/api/heroes', methods=['GET'])
def get_heroes():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM heroes')
        rows = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]

        heroes = []
        for row in rows:
            hero = dict(zip(column_names, row))

           
            hero['roles'] = hero['roles'].split(',') if isinstance(hero['roles'], str) else []
            hero['attributes'] = {
                "strength": hero.get("strength", 0),
                "strengthGain": hero.get("strength_gain", 0),
                "agility": hero.get("agility", 0),
                "agilityGain": hero.get("agility_gain", 0),
                "intelligence": hero.get("intelligence", 0),
                "intelligenceGain": hero.get("intelligence_gain", 0),
                "attackDamage": hero.get("attack_damage", 0),
            }

            
            for k in ['strength_gain', 'agility_gain', 'intelligence_gain', 'strength', 'agility', 'intelligence', 'attack_damage']:
                hero.pop(k, None)

            heroes.append(hero)

        cur.close()
        conn.close()

        return jsonify(heroes)

    except Exception as e:
        print(f"Error fetching heroes: {e}")
        return jsonify({"error": "Could not fetch heroes"}), 500
    



@app.route('/api/matchups', methods=['GET'])
def get_matchups():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT hero_id, against_hero_id, advantage, games_played FROM matchups;")
    rows = cur.fetchall()
    matchups = [
        {
            "hero_id": row[0],
            "againts_hero_id": row[1],
            "advantage": float(row[2]),
            "games_played": row[3]
        }
        for row in rows
    ]
    cur.close()
    conn.close()
    return jsonify(matchups)


@app.route('/api/abilities', methods=['GET'])
def get_abilities():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, hero_id, name, description, ability_type FROM abilities;")
    rows = cur.fetchall()
    abilities = [
        {
            "id": row[0],
            "hero_id": row[1],
            "name": row[2],
            "description": row[3],
            "ability_type": row[4],
            
        }
        for row in rows
    ]
    cur.close()
    conn.close()
    return jsonify(abilities)


@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, cost, description FROM items;")
    rows = cur.fetchall()
    items = [
        {
            "id": row[0],
            "name": row[1],
            "cost": row[2],
            "description": row[3],
            
        }
        for row in rows
    ]
    cur.close()
    conn.close()
    return jsonify(items)


@app.route('/api/item-builds', methods=['GET'])
def get_item_builds():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT build_id, item_id, position FROM build_items;")
    rows = cur.fetchall()
    builds = []
    for row in rows:
        builds.append({
            "build_id": row[0],
            "item_id": row[1],  
            "position": row[2],
            
        })
    cur.close()
    conn.close()
    return jsonify(builds)

@app.route("api/hero/<int:hero_id>")
def hero_page(hero_id):
    conn = get_db_connection()
    hero = conn.execute("SELECT * FROM heroes WHERE id = %s", (hero_id,)).fetchone()
    return render_template("hero.html", hero=hero)






if __name__ == '__main__':
    app.run(debug=True)
