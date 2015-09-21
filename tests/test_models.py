class TestUserModel():

    def test_repr(self, user):
        assert str(user) == '<User u\'John\'>'

