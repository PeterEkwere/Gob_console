#!/usr/bin/python
"""
    Initialzes the models storage based on the environment
    Author: Peter Ekwere
"""
import models
from os import getenv

storage_type = getenv("GOBAI_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()