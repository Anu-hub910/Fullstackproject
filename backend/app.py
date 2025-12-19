from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = "database.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- AUTO CREATE TABLES ----------
def init_db():
    db = get_db()
    db.executescript("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image TEXT,
        name TEXT,
        description TEXT
    );

    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image TEXT,
        name TEXT,
        description TEXT,
        designation TEXT
    );

    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email TEXT,
        mobile TEXT,
        city TEXT
    );

    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT
    );
    """)
    db.commit()

init_db()

# ---------- PROJECTS ----------
@app.route("/projects", methods=["POST"])
def add_project():
    data = request.json
    db = get_db()
    db.execute(
        "INSERT INTO projects (image, name, description) VALUES (?, ?, ?)",
        (data["image"], data["name"], data["description"])
    )
    db.commit()
    return {"message": "Project added"}

@app.route("/projects", methods=["GET"])
def get_projects():
    db = get_db()
    rows = db.execute("SELECT image, name, description FROM projects").fetchall()
    return jsonify([dict(r) for r in rows])

# ---------- CLIENTS ----------
@app.route("/clients", methods=["POST"])
def add_client():
    data = request.json
    db = get_db()
    db.execute(
        "INSERT INTO clients (image, name, description, designation) VALUES (?, ?, ?, ?)",
        (data["image"], data["name"], data["description"], data["designation"])
    )
    db.commit()
    return {"message": "Client added"}

@app.route("/clients", methods=["GET"])
def get_clients():
    db = get_db()
    rows = db.execute(
        "SELECT image, description, name, designation FROM clients"
    ).fetchall()
    return jsonify([dict(r) for r in rows])

# ---------- CONTACT ----------
@app.route("/contact", methods=["POST"])
def submit_contact():
    data = request.json
    db = get_db()
    db.execute(
        "INSERT INTO contacts (full_name, email, mobile, city) VALUES (?, ?, ?, ?)",
        (data["full_name"], data["email"], data["mobile"], data["city"])
    )
    db.commit()
    return {"message": "Contact submitted"}

@app.route("/contact", methods=["GET"])
def view_contacts():
    db = get_db()
    rows = db.execute(
        "SELECT full_name, email, mobile, city FROM contacts"
    ).fetchall()
    return jsonify([dict(r) for r in rows])

# ---------- NEWSLETTER ----------
@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json
    db = get_db()
    db.execute("INSERT INTO subscribers (email) VALUES (?)", (data["email"],))
    db.commit()
    return {"message": "Subscribed"}

@app.route("/subscribe", methods=["GET"])
def view_subscribers():
    db = get_db()
    rows = db.execute("SELECT email FROM subscribers").fetchall()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(debug=True)
