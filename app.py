from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        dob TEXT NOT NULL,
                        therapist TEXT NOT NULL
                    )""")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    dob = request.form.get('dob', '')
    therapist = request.form.get('therapist', '').strip()

    error = None
    if not first_name or not last_name or not dob or not therapist:
        error = "All fields are required."
    else:
        try:
            dob_date = datetime.strptime(dob, "%Y-%m-%d")
            if dob_date >= datetime.today():
                error = "Date of Birth must be in the past."
        except ValueError:
            error = "Invalid date format."

    if error:
        return render_template('form.html', error=error,
                               first_name=first_name, last_name=last_name,
                               dob=dob, therapist=therapist)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (first_name, last_name, dob, therapist) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, dob, therapist))
    conn.commit()
    conn.close()
    return render_template('confirmation.html', first_name=first_name,
                           last_name=last_name, dob=dob, therapist=therapist)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=10000)
