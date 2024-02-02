from flask import Flask
from settings.config import Config
from logics.db import get_db_conn

app = Flask(__name__)
app.config.from_object(Config)

@app.get("/")
def main():
    if get_db_conn():
        is_dbconn = True
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sample_table")
    result = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return f"""<p>Hello, Flask! with debugger mode active</p> <br> 
        <p>Database connection established:{str(is_dbconn)}</p>
        <br> <p>{result['DATA']}</p>"""

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)
    
