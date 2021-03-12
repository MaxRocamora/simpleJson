# -*- coding: utf-8 -*-
'''
Handles saving/loading key,values to/from a json file
author: maxirocamora@gmail.com
'''

from sys import executable
from sys import version as python_version
import os
import time
import inspect
from datetime import datetime
import platform
from json_utils import load_json, save_json
from version import *


class JsonMetadata():
    def __init__(self, name):
        self._name = name
        self._data = {}
        self._data["_about"] = 'Saved by JsonMetada'
        self._data["_version"] = version

    @property
    def version(self):
        ''' version '''
        return version

    @property
    def name(self):
        ''' name of this metadata class'''
        return self._name

    @property
    def data(self):
        ''' main metadata info of the data dict '''
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def extension(self):
        ''' extension of the json file '''
        return ".json"

    @property
    def prefix(self):
        ''' file prefix, is autoincluded on the filename '''
        return "MD_"

    @property
    def filename(self):
        ''' Returns default filename with prefix and extension '''
        return self.prefix + self.name + self.extension

    @property
    def filepath(self):
        ''' full json metadata filepath '''
        return os.path.join(self.path, self.filename)

    @property
    def path(self):
        ''' base path location of metadata json file
        if path is not set, returns default dir '''
        if not hasattr(self, '_path'):
            return os.path.join(os.path.dirname(__file__), 'md_files')
        return self._path

    @path.setter
    def path(self, val):
        self._path = os.path.realpath(val)

    @property
    def has_file(self):
        return os.path.exists(self.filepath)

# --------------------------------------------------------------------------------------------
# METADATA LOAD/INSERT/REMOVE/SAVE
# --------------------------------------------------------------------------------------------

    def load_as_class(self):
        ''' returns the metada dict as a class obj '''
        metadataClass = type(self.name, (), self._data)
        return metadataClass

    def load(self):
        ''' loads metadata from disk '''
        if self.has_file:
            self._data = load_json(self.filepath)
        else:
            self._data = {}

    def insert(self, key, value):
        ''' inserts value into metadata '''
        self._data[key] = value

    def remove(self, key):
        ''' remove key from metadata '''
        if key in self._data.keys():
            del self._data[key]

    def save(self):
        ''' Save current metadata into json file. '''
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        self.data = self._include_system_data(self.data)
        save_json(self.data, self.filepath)

    def insert_class(self, _class):
        ''' set class dict to data, data is cleared '''
        self.data = self._attributes_from_class(_class)

    def _attributes_from_class(self, _class):
        attributes = {}
        for name in dir(_class):
            value = getattr(_class, name)
            if not name.startswith('__') and not inspect.ismethod(value):
                attributes[name] = value
        return attributes

# --------------------------------------------------------------------------------------------
# SYSTEM METADATA OS/USER/TIME
# --------------------------------------------------------------------------------------------

    def _include_system_data(self, data):
        ''' add system metadata to the default data before save '''
        sys_data = {}
        sys_data['name'] = self.name
        sys_data['app'] = os.path.basename(executable)
        sys_data['PC'] = str(platform.node())
        sys_data['python_version'] = python_version
        sys_data['jsonmd_version'] = version
        sys_data['User'] = str(os.getenv('username'))
        sys_data['time'] = self._get_time_metadata
        data['system'] = sys_data
        return data

    @property
    def _get_time_metadata(self):
        ''' Get export time info. '''
        ftime = time.strftime("%Y,%b,%d,%j,%H:%M", time.localtime())
        times = ftime.split(",")
        td = {
            "year": times[0],
            "month": times[1],
            "day": times[2],
            "year_day": times[3],
            "time": times[4],
            'save_time': datetime.now().ctime()
        }
        return td
