from app import app

from testdatabaseconnection import init
init(app)

if __name__ == "__main__":
    app.run()
