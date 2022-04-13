from views.main import main_view, settings_view
from views.login import login_view
from services import user_service
from repositories import user_repository


def startup():
    user_repository.create_user('a', 'q', True, False, False)
    user_repository.create_user('u1', 'y', False, False, False)
    user_repository.create_user('u2', 'y', False, True, False)
    main_view.startup()


def login():
    login_view.show()


def main(username):
    main_view.show(username, user_service.is_admin(username))


def login_handler(username, password):
    user_service.validate_login(username, password)
    user = user_repository.get_user(username)
    main(user.username)


def settings(username):
    settings_view.show(username)


def changepass_handler(username, oldpass, newpass, newpassconf):
    if newpass != newpassconf:
        settings_view.show(username, '', 'Password confirmation failed')
        return
    try:
        user_service.change_password(username, oldpass, newpass)
    except Exception as e:
        settings_view.show(username, '', e)
        return
    login()

