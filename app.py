from flask import Flask
from settings.config import Config
from logics.db import get_db_conn

app = Flask(__name__)

@app.get("/")
def main():
    is_dbconn = get_db_conn()
    return f"<p>Hello, Flask! with debugger mode active</p> <br> <p>Database connection established:{str(is_dbconn)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.config.from_object(Config)
