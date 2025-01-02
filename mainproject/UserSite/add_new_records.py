from UserSite.models import User

def add_new_user(username, email, password):
    user = User(username=username, email=email, password=password)
    user.save()
    return user

user_0 = add_new_user('user_0', 'user_0@gmail.com', 'password_0')
print(user_0)