
import jwt
from flask import abort
import datetime
import calendar
from constants import JWT_ALGORITHM, JWT_SECRET


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_token(self, username, password, is_refresh=False):
        user = self.user_service.get_by_user_name(username)
        if user is None:
            abort(404)

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get("username")

        return self.generate_token(username, None, is_refresh=True)
