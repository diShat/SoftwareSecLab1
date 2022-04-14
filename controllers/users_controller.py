from repositories import user_repository
from views.users import users_view


def list():
    users = user_repository.get_all()
    users_view.show(users)


def set_block_status_handler(username, is_blocked_status):
    user_repository.set_block_status(username, is_blocked_status)
    list()