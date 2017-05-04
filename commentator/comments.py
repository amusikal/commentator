from .connection import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Binary


class Thread(Base):

    __tablename__ = 'commentator_thread'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Thread(id='{id}', name='{name}')".format(id=self.id, name=self.name)


class Parent(Base):

    __tablename__ = 'commentator_parent'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Thread(id='{id}', name='{name}')".format(id=self.id, name=self.name)


class Comment(Base):

    __tablename__ = 'commentator_comments'

    # fields = ['tid', 'id', 'parent', 'created', 'modified', 'mode', 'remote_addr', 'text', 'author', 'email', 'website', 'likes', 'dislikes', 'voters']

    id = Column(Integer, primary_key=True)
    #threadid = relationship('Thread')

    parent_id = Column(Integer, ForeignKey('commentator_parent.id'))

    mode = Column(Integer)
    remote_addr = Column(String)

    text = Column(String)

    author = Column(String)
    email = Column(String)
    website = Column(String)

    likes = Column(Integer)
    dislikes = Column(Integer)
    # TODO - voters

    uid = Column(Binary, index=True)
    created = Column(DateTime)
    modified = Column(DateTime)

    def __repr__(self):
        return "<Comment(uid='{uid}', email={email}, remote_addr='{remote_addr}')>".format(
            uid=self.uid,
            email=self.email,
            remote_addr=self.remote_addr
            )
