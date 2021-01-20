# setup_requires and tests_require is used to integrate testing with setuptools
# testing can be done by running command: python setup.py test
# "test" in the command refers to the alias made in setup.cfg which is equal to pytest

from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ]
)
