import os
import io
from setuptools import setup, find_packages

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name='simple-json-utils',
    version='1.0.0',
    description='Simple Json Utitilies',
    author='Maximiliano Rocamora',
    author_email='maxirocamora@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MaxRocamora/simpleJson',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7')
