#!/usr/bin/python3
""" Print class for SQLAlchemy"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_sessio
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


class DBStorage:
    """Private class attrib."""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        database = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        envir = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        if envir == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary"""
        cls_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            qry = self.__session.query(cls)
            for elmn in qry:
                ky = "{}.{}".format(type(elmn).__name__, elmn.id)
                cls_dict[ky] = elmn
        else:
            lst = [State, City, User, Place, Review, Amenity]
            for clse in lst:
                qry = self.__session.query(clse)
                for elmn in qry:
                    ky = "{}.{}".format(type(elmn).__name__, elmn.id)
                    cls_dict[ky] = elmn
        return (cls_dict)

    def new(self, obj):
        """Add the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sesi = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesi)
        self.__session = Session()

    def close(self):
        """close SQLAlchemy session"""
        self.__session.close()
