try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Alfie Mendoza",
    "url": "url to get it at",
    "download_url": "where to download it",
    "author_email": "alfie.mendoza929@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"]
    "packages": ["ex47"],
    "scripts": [],
    "name": "Python the Hard Way Game"
}

setup(**config)
