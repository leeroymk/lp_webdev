from db import db_session
from models import User

user = User.query.first()
user.salary = 234
db_session.commit()
