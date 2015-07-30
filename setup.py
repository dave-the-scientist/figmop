#!/usr/bin/python
from distutils.core import setup

setup(name='FiGMoP', version='1.1',
      description='FInding Genes using MOtif Patterns',
      author='David Curran',
      author_email='curran.dave.m@gmail.com',
      url='https://github.com/dave-the-scientist/figmop',
      long_description=open('README').read(),
      license='LICENSE',
      scripts=['figmop'],
      requires=['patternHmm (>= 0.4)'],
     )
