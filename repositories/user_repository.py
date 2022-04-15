from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    username = Column("username", String, unique=True)
    password = Column("password", String)
    is_admin = Column("is_admin", Boolean)
    login_attempt = Column('login_attempt', Integer)
    is_blocked = Column("is_blocked", Boolean)
    is_pass_restricted = Column("is_pass_restricted", Boolean)


Base.metadata.create_all(bind=engine)


def get_user(username):
    session = Session()
    user = session.query(User).filter(User.username == username).first()
    session.close()
    return user


def create_user(username, password, is_admin=False, is_blocked=False, is_pass_restricted=False):
    if username == '':
        raise Exception('Empty username')

    session = Session()

    user = User()
    user.username = username
    user.password = password
    user.is_admin = is_admin
    user.login_attempt = 0
    user.is_blocked = is_blocked
    user.is_pass_restricted = is_pass_restricted

    session.add(user)
    session.commit()
    session.close()

    return user


def get_all():
    session = Session()
    users = session.query(User).all()

    session.close()
    return users


def change_password(username, newpass):
    user = get_user(username)
    session = Session()
    user.password = newpass

    session.add(user)
    session.commit()
    session.close()


def set_block_status(username, is_blocked_status):
    user = get_user(username)
    session = Session()
    user.is_blocked = is_blocked_status

    session.add(user)
    session.commit()
    session.close()


def set_pass_restriction_status(username, is_pass_restricted_status):
    user = get_user(username)
    session = Session()
    user.is_pass_restricted = is_pass_restricted_status

    session.add(user)
    session.commit()
    session.close()


def add_failed_login_attempt(username):
    user = get_user(username)

    session = Session()

    user.login_attempt += 1

    session.add(user)
    session.commit()
    session.close()


def reset_login_attempt(username):
    user = get_user(username)

    session = Session()

    user.login_attempt = 0

    session.add(user)
    session.commit()
    session.close()

