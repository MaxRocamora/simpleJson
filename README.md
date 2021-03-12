<h1><center>Simple JSON Utils</center></h1>
Simple utilities to manage json files.

# JsonMetadata
Load, save, and update data from your class to a json file, and viceversa.

-------

#### Example
```python

import JsonMetadata

class Car():
    def __init__(self, name):
        self.meta = JsonMetadata(name)


ferrari = Car('ferrari')
ferrari.meta.path = your_path_for_save_the_json_file
ferrari.meta.insert('fuel', 200)
ferrari.meta.save()

```

##### Output:

A file named MD_ferrari.json into given path.

Inside the json file:
<dl>
  <dt>
{
   "_about": "Saved by JsonMetada",
   "_version": "1.0.0",
   "fuel": 200,
   "system": {
        "PC": "Your_User",
        "User": "Max",
        "app": "python.exe",
        "name": "ferrari", 
        "time": {
            "day": "11", 
            "month": "Oct", 
            "save_time": "Sun Oct 11 17:27:05 2047", 
            "time": "17:27", 
            "year": "2047", 
            "year_day": "047"
        }
    }
}
  </dt>
</dl>

#### Loading your data into dict

```python

import JsonMetadata

class Car():
    def __init__(self, name):
        self.meta = JsonMetadata(name)


ferrari = Car('ferrari')
ferrari.meta.path = your_path_for_save_the_json_file
ferrari.meta.load()

ferrari.meta.data['fuel']  # 200
ferrari.meta.save()

```

--------------

#### Load the data as an object, the json is converted to a class with attributes

```python

from jsonmd.json_metadata import JsonMetadata

class Car():
    def __init__(self, name):
        self.meta = JsonMetadata(name)


ferrari = Car('ferrari')
ferrari.meta.path = your_path_for_save_the_json_file
ferrari.metadata = ferrari.meta.load_as_class()

ferrari.metadata.fuel  # 200

```

# JsonUtils

load_json, update_json and save_json simplified methods.

#### Install
pip install json-metadata
https://pypi.org/project/json-metadata/1.1.0/
