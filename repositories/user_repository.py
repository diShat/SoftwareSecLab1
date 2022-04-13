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
    is_blocked = Column("is_blocked", Boolean)
    is_pass_restricted = Column("is_pass_restricted", Boolean)


Base.metadata.create_all(bind=engine)


def get_user(username):
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    session.close()
    return user


def create_user(username, password, is_admin=False, is_blocked=False, is_pass_restricted=False):
    session = Session()

    user = User()
    user.username = username
    user.password = password
    user.is_admin = is_admin
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