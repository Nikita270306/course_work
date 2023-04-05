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

    def update(self, result):
        self.session.add(result)
        self.session.commit()


    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()
