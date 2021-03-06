from repositories import user_repository
from views.users import users_view, newuser_form_view


def list():
    users = user_repository.get_all()
    users_view.show(users)


def set_block_status_handler(username, is_blocked_status):
    user_repository.set_block_status(username, is_blocked_status)
    list()


def set_restrict_status_handler(username, is_pass_restricted_status):
    user_repository.set_pass_restriction_status(username,is_pass_restricted_status)
    list()


def add_user():
    newuser_form_view.show()


def add_user_handler(username):
    try:
        user_repository.create_user(username, '')
    except Exception as e:
        newuser_form_view.show('', e)
        return
    list()
