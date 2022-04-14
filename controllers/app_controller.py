from views.main import main_view, settings_view
from views.login import login_view
from services import user_service, session_service
from repositories import user_repository


def startup():
    session_service.create_session()
    user_repository.create_user('a', 'q', True, False, False)
    user_repository.create_user('u1', 'y', False, False, False)
    user_repository.create_user('u2', 'y', False, True, False)
    main_view.startup()


def login():
    session_service.destroy_session()
    login_view.show()


def main():
    main_view.show(session_service.get_session_username(), session_service.is_admin_session())


def login_handler(username, password):
    user_service.validate_login(username, password)
    user = user_repository.get_user(username)
    session_service.create_session(user.username, user.is_admin)
    main()


def settings():
    settings_view.show(session_service.get_session_username())


def changepass_handler(oldpass, newpass, newpassconf):
    username = session_service.get_session_username()
    if newpass != newpassconf:
        settings_view.show(username, '', 'Password confirmation failed')
        return
    try:
        user_service.change_password(username, oldpass, newpass)
    except Exception as e:
        settings_view.show(username, '', e)
        return
    login()

