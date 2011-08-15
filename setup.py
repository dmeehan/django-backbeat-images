from setuptools import setup, find_packages
import media
import os

try:
    long_description = open('README.rst').read()
except IOError:
    long_description = ''

try:
    reqs = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read()
except (IOError, OSError):
    reqs = ''

setup(
    name='django-backbeat-media',
    version=media.get_version(),
    description='A pluggable media management app.',
    long_description=long_description,
    author='Douglas Meehan',
    author_email='dmeehan@gmail.com',
    include_package_data=True,
    url='http://github.com/dmeehan/django-backbeat-projects',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
    ],
    install_requires = reqs,
    dependency_links = []
)