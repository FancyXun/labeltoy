#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Command
from sys import platform as _platform
from shutil import rmtree
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))
NAME = 'labeltoy'
REQUIRES_PYTHON = '>=3.0.0'
REQUIRED_DEP = ['pyqt5']
about = {}

with open(os.path.join(here, '__init__.py')) as f:
    exec(f.read(), about)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


# OS specific settings
SET_REQUIRES = []
if _platform == "linux" or _platform == "linux2":
   # linux
   print('linux')
elif _platform == "darwin":
   # MAC OS X
   SET_REQUIRES.append('py2app')

required_packages = find_packages()
required_packages.append('labeltoy')

APP = [NAME + '.py']
OPTIONS = {
    'argv_emulation': True,
}

class UploadCommand(Command):
    """Support setup.py upload."""

    description=readme + '\n\n' + history,

    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            self.status('Fail to remove previous builds..')
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(
            '{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag -d v{0}'.format(about['__version__']))
        os.system('git tag v{0}'.format(about['__version__']))
        # os.system('git push --tags')

        sys.exit()


setup(
    app=APP,
    name=NAME,
    version=about['__version__'],
    description="labeltoy is a graphical image annotation tool for OCR",
    long_description=readme + '\n\n' + history,
    author="Xun Zhang",
    author_email='837633751@qq.com',
    url='https://github.com/FancyXun/labeltoy',
    python_requires=REQUIRES_PYTHON,
    package_dir={'labeltoy': '.'},
    packages=required_packages,
    entry_points={
        'console_scripts': [
            'labeltoy=labeltoy.labeltoy:main'
        ]
    },
    include_package_data=True,
    install_requires=REQUIRED_DEP,
    license="Apache License 2.0 license",
    zip_safe=False,
    keywords='labeltoy labelTool development annotation OCR',
    classifiers=[
    ],
    package_data={},
    options={'py2app': OPTIONS},
    setup_requires=SET_REQUIRES,
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    }
)