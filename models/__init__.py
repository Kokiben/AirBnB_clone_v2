#!/usr/bin/python3
"""This script create a unique FileStorage instance for our application."""
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


#Add a conditional depending of value of environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
# Call the reload() method on this variable
storage.reload()
