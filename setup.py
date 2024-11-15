#!/usr/bin/env python3

import codecs
import os
import re

from setuptools import setup, find_packages

#Copied from wheel package
here = os.path.abspath(os.path.dirname(__file__))
#README = codecs.open(os.path.join(here, 'README.txt'), encoding='utf8').read()
#CHANGES = codecs.open(os.path.join(here, 'CHANGES.txt'), encoding='utf8').read()

with codecs.open(os.path.join(os.path.dirname(__file__), 'trainscanner', '__init__.py'),
                 encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))

setup(name='TrainScanner',
      version=metadata['version'],
      description='Generate a long image strip from a train video',
      long_description=open('README.md', encoding='utf-8_sig').read(),
      long_description_content_type="text/markdown",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        ],
      author='Masakazu Matsumoto',
      author_email='vitroid@gmail.com',
      url='https://github.com/vitroid/TrainScanner/',
      keywords=['trainscanner',],
      license='MIT',
      packages=find_packages(
        include=['trainscanner', 'ts_conv', ], 
        exclude=['trainscanner.i18n', ],
      ),
      install_requires=[# 'numpy==1.19.3',
                        "tiledimage",
                        "scikit-video@git+https://github.com/scikit-video/scikit-video.git",
                        "scikit-build",
                        "videosequence",
                        "opencv-python-headless",
                        "pyqt6",
                        ],#'pyqt5', ], #cv2
      entry_points = {
              'console_scripts': [
                  'trainscanner        = trainscanner.trainscanner_gui:main',
                  'trainscanner_pass1  = trainscanner.pass1_gui:main',
                  'trainscanner_stitch = trainscanner.stitch_gui:main',
                  'trainscanner_shakereduction = trainscanner.shakereduction:main',
                  'filmify             = ts_conv.film:main',
                  'rectify             = ts_conv.rect:main',
                  'helicify            = ts_conv.helix:main',
                  'hansify             = ts_conv.hans_style:main',
                  'ts_converter        = ts_conv.converter_gui:main',
              ]
          },
       include_package_data=True,
       package_data={
      'trainscanner': ['i18n/*.qm'],
      'ts_conv':      ['i18n/*.qm'],
       },
      )
