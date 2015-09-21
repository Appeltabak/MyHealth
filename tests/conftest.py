import pytest
from app import db
from app.models import User


@pytest.fixture
def user():
    db.create_all()
    user = User('John', 'john@example.com')

    db.session.add(user)
    db.session.commit()

    return user
