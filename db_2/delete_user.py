from db.db import db_session
from db.models import User

user = User.query.first()
db_session.delete(user)
db_session.commit()