from repositories import user_repository
from views.users import users_view


def list():
    users = user_repository.get_all()
    users_view.show(users)
