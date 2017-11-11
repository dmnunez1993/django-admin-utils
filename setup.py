import os
from setuptools import setup, find_packages


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding='utf-8')
    except TypeError:
        file = open(path)
    return file.read()


def get_install_requires():
    install_requires = ['Django']

    try:
        import importlib
    except ImportError:
        install_requires.append('importlib')

    try:
        from collections import OrderedDict
    except ImportError:
        install_requires.append('ordereddict')

    return install_requires


setup(
    name='django-admin-utils',
    version='0.0.1',
    description='Django admin utilities',
    long_description=read('README.md'),
    author='Diego Maldonado',
    author_email='dmnunez1993@gmail.com',
    url='https://github.com/dmnunez1993/django-admin-utils',
    packages=find_packages(),
    license='GPL',
    classifiers=[
        'Environment :: Web Environment',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=get_install_requires()
)
