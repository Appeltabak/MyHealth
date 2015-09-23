from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database_exists, create_database


def init(app):
    print "starting db test..."
    db = SQLAlchemy(app)

    from app.models import User

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
    # if not database_exists(engine.url):
    #     print "Database not found, creating new..."
    #     create_database(engine.url)
    #     print "Done!"

    Session = sessionmaker(bind=engine)
    session = Session()

    db.create_all()

    print "creating user 'admin'..."
    admin = User("admin", "test@test.com")
    session.add(admin)
    session.commit()
    print "done!"

    print "Users found in database:"
    for instance in session.query(User):
        print instance.username
        print "destroying user..."
        session.delete(instance)
        session.commit()
        print "done!"

    print "db test done!"
