from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlite3 import dbapi2 as sqlite
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///file.db', echo=True)
Session = sessionmaker(bind=engine)

@event.listens_for(engine, 'connect')
def do_connect(dbapi_connection, connection_record):
    # Disable sqlite's emitting of the BEGIN statement entirely.
    # Also stops it from emitting COMMIT before the DDL.
    dbapi_connection.isolation_level = None


@event.listens_for(engine, 'begin')
def do_begin(conn):
    # Emit our own BEGIN.
    conn.execute('BEGIN')


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(username='%s', fullname='%s', password='%s')>" % (
            self.username, self.fullname, self.password
            )
