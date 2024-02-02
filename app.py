from flask import Flask

app = Flask(__name__)

@app.get("/")
def main():
    return f"<p>Hello, Flask! with debugger mode active</p> <br> <p>Database connection is {'working'}</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    