#!/usr/bin/python3
"""This script defines DBStorage engine"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Database Storage Engine

    Attributes:
        __engine: SQLAlchemy engine
        __session: SQLAlchemy session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes new DBStorage instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                        format(getenv("HBNB_MYSQL_USER"),
                                               getenv("HBNB_MYSQL_PWD"),
                                               getenv("HBNB_MYSQL_HOST"),
                                               getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, ob):
        """Add ob(ject) to current database session"""
        self.__session.add(ob)

    def delete(self, ob=None):
        """Deletes ob(ject) from current database session"""
        self.__session.delete(ob)

    def save(self):
        """Commit(s) all changes to current database session"""
        self.__session.commit()

    def reload(self):
        """Initializes new session of database"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()

        def all(self, cls=None):
            """Query on current database session all obj(ects) of given class

            Return:
                Dict of queried class <class name>.<obj id> = obj
            """
            if cls is None:
                obj = self.__session.query(State).all()
                obj.extend(self.__session.query(City).all())
                obj.extend(self.__session.query(User).all())
                obj.extend(self.__session.query(Place).all())
                obj.extend(self.__session.query(Review).all())
                obj.extend(self.__session.query(Amenity).all())
            else:
                if type(cls) == str:
                    cls = eval(cls)
                obj = self.__session.query(cls)
            return {"{}.{}".format(type(x).__name__, x.id): x for x in obj}

    def close(self):
        """Close working database session"""
        self.__session.close()
