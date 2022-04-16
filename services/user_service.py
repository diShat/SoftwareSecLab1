from repositories import user_repository
import re


def validate_login(username, password):
    user = user_repository.get_user(username)
    if user is None:
        raise Exception('Login failed: no such user')
    if user.is_blocked:
        raise Exception('Login failed: user is blocked')
    if user.password != password:
        if user.login_attempt >= 2:
            user_repository.set_block_status(user.username, True)
            user_repository.reset_login_attempt(user.username)
            raise Exception('Login failed: user has been blocked')
        else:
            user_repository.add_failed_login_attempt(user.username)
        raise Exception('Login failed: incorrect password')
    user_repository.reset_login_attempt(user.username)


def compare_password(username, oldpassword):
    user = user_repository.get_user(username)
    return user.password == oldpassword


def is_admin(username):
    user = user_repository.get_user(username)
    return user.is_admin == True


def change_password(username, oldpass, newpass):
    if not compare_password(username, oldpass):
        raise Exception('Invalid old password')
    user = user_repository.get_user(username)
    if user.is_pass_restricted and not regex_password(newpass):
        raise Exception(
            """Your new password format is restricted:\n
            must contain a letter(A-Z,a-z), an arithmetic sign(*/+=) and a punktuation mark(,.:;?!-)""")
    user_repository.change_password(username, newpass)


def regex_password(password):
    if not re.search("[A-Za-z]", password):
        return False
    if not re.search("[,.:;?!-]", password):
        return False
    if not re.search("[*/+=-]", password):
        return False
    return True
