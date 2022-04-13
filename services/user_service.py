from repositories import user_repository


def validate_login(username, password):
    user = user_repository.get_user(username)
    if user.password != password:
        raise Exception('Login failed')


def compare_password(username, oldpassword):
    user = user_repository.get_user(username)
    return user.password == oldpassword


def is_admin(username):
    user = user_repository.get_user(username)
    return user.is_admin == True


def change_password(username, oldpass, newpass):
    if not compare_password(username, oldpass):
        raise Exception('Invalid old password')
    user_repository.change_password(username, newpass)
