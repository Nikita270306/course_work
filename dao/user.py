from dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        result = User(**user_d)
        self.session.add(result)
        self.session.commit()
        return result

    def delete(self, uid):
        result = self.get_one(uid)
        self.session.delete(result)
        self.session.commit()

    def update(self, user_d):
        result = self.get_one(user_d.get("id"))
        result.username = user_d.get("username")
        result.password = user_d.get("password")
        result.role = user_d.get("role")

        self.session.add(result)
        self.session.commit()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()