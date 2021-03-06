#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/03/30 12:10
# @Author  : niuliangtao
# @Site    :
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup, find_packages

install_requires = ['beautifulsoup4', 'opencv-python', 'pytesseract', 'keras', 'numpy', 'tushare', 'pymysql', 'pyhtml']

setup(name='notechat',
      version='0.0.9.2',
      description='notechat',
      author='euler',
      author_email='1007530194@qq.com',
      url='https://github.com/1007530194',

      packages=find_packages(),
      install_requires=install_requires
      )
