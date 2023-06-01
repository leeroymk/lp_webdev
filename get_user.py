from models import User

user = User.query.first()
print(f'''Имя: {user.name},
зарплата: {user.salary},
email: {user.email}''')
