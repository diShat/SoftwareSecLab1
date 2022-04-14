global SESSION


class Session:
    username = ''
    is_admin = False


def create_session(username = '', is_admin = False):
    global SESSION
    SESSION = Session()
    SESSION.username = username
    SESSION.is_admin = is_admin
    return SESSION


def get_session():
    global SESSION
    return SESSION


def destroy_session():
    global SESSION
    SESSION.username = ''
    SESSION.is_admin = False


def get_session_username():
    global SESSION
    return SESSION.username


def is_admin_session():
    global SESSION
    return SESSION.is_admin
