# coding=utf-8
from __future__ import absolute_import, print_function

import unittest
import os
import sys

path = 'D:/Repos/Arcane2/services/simpleJson'
if path not in sys.path:
    sys.path.append(path)

from jsonmd.json_metadata import JsonMetadata

# test path & name
base_path = os.path.dirname(os.path.dirname(__file__))
test_path = os.path.join(os.path.dirname(__file__), 'test_files')
test_name = 'test'
test_class_name = 'proxy'
att_list = ['foo', 'bar']


class Test_windows(unittest.TestCase):

    def test_create_and_save(self):
        meta = JsonMetadata(test_name)

        # test properties
        self.assertEqual(meta.name, test_name)
        meta.version
        meta.data
        meta.extension
        meta.prefix
        meta.path
        meta.filepath
        meta.filename
        meta.has_file

        meta.path = test_path
        meta.insert(key='coins', value=12)

        # check if data have coins and value 12
        self.assertEqual(meta.data['coins'], 12)

        meta.save()

        # check if file exists
        self.assertEqual(os.path.exists(meta.filepath), True)

        meta.insert('coins', 7)

        # check if data have coins and value 7
        self.assertEqual(meta.data['coins'], 7)

        meta.remove('coins')
        self.assertEqual(meta.data.get('coins', None), None)

        meta.insert(key='items', value=att_list)
        meta.save()

        metaObj = meta.load_as_class()
        self.assertEqual(type(metaObj), type)
        self.assertEqual(hasattr(metaObj, 'items'), True)
        self.assertEqual(metaObj.items, att_list)

    def test_create_from_class(self):
        ''' save_from_a_class '''
        meta = JsonMetadata(test_class_name)
        self.assertEqual(meta.name, test_class_name)
        meta.path = test_path

        proxyClass = type('Proxy', (), {'foos': 12, 'items': att_list})
        meta.insert_class(proxyClass)
        self.assertEqual(meta.data['foos'], 12)
        self.assertEqual(meta.data['items'], att_list)
        meta.save()


if __name__ == '__main__':
    unittest.main()
