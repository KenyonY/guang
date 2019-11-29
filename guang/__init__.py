'''
This is a universal function library.
'''
from . import *


def get_version():
    with open('version','r') as fi:
        v_list = fi.read().split('.')
        v = int(''.join(v_list))
        v += 1
    with open('version','w') as fo:
        fo.write('.'.join(list(str(v))))

    return '.'.join(v_list)

__v = get_version()

# '0.0.7.2.7'
__version__ = '0.0.' + __v
print('__version__:', __version__)
__author__ = 'K.y'
__copyright = 'Copyright 2019 K.y'

__all__ = ["ML","Utils","DL", "Voice", "wechat"]

