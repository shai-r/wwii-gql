from flask import Flask

from app.db.database import init_db

app = Flask(__name__)

if __name__ == '__main__':
    init_db()
    app.run()