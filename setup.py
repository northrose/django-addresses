import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-contact_info',
    version = '0.1.2',
    packages = ['contact_info'],
    include_package_data = True,
    license = 'BSD License', # example license
    description = 'A simple Django app to handle contact information data.',
    long_description = README,
    url = 'https://github.com/northrose/django-contact_info',
    author = 'Damien Barchowsky',
    author_email = 'dbarchowsky@gmail.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    install_requires = [
        "django>=1.8",
        ],
    )