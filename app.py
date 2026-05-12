from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = "25060"

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            sslmode="require"
        )

        cur = conn.cursor()
        cur.execute("SELECT first_name, last_name, birthday FROM contacts")
        contacts = cur.fetchall()

        cur.close()
        conn.close()

        return render_template('index.html', contacts=contacts)

    except Exception as e:
        return f"ERROR: {str(e)}", 500


@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)