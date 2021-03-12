# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------
# Methods that handles commons json operations.
# --------------------------------------------------------------------------------------------

from __future__ import absolute_import, print_function

import json
import os
from jsonmd import MissingJson, InvalidJson


def load_json(json_file):
    ''' returns a dict from json file
    Args:
        json_file (path) file to read data.
    '''
    if not os.path.exists(json_file):
        raise MissingJson(
            "json file not found ({}).".format(json_file))

    fIn = open(json_file, 'r')
    try:
        value = json.load(fIn)
    except ValueError as e:
        msg = "{} \n JSON File issue: {}".format(json_file, str(e))
        raise InvalidJson(msg)
    finally:
        fIn.close()

    return value


def save_json(dataDict, json_file):
    ''' Saves a dictionary into a json file
    Args:
        dataDict (dictionary) dictionary to save
        json_file (file) target file to save into
    '''

    if not os.path.dirname(json_file):
        os.makedirs(json_file)

    try:
        with open(json_file, 'w') as loadedJsn:
            json.dump(dataDict, loadedJsn, sort_keys=True, indent=4)
    except IOError:
        print('IOError: No such file of directory:', json_file)


def update_json(values, json_file):
    ''' Opens a json file, load its params,
    add new keys and save it
    '''
    if not os.path.exists(json_file):
        dictData = {}
        with open(json_file, 'w') as loadedJsn:
            json.dump(dictData, loadedJsn, sort_keys=True, indent=4)

    # opens and read json into dictData
    with open(json_file, 'r') as loadedJsn:
        dictData = json.load(loadedJsn)
        dictData.update(values)

    with open(json_file, 'w') as loadedJsn:
        json.dump(dictData, loadedJsn, sort_keys=True, indent=4)
