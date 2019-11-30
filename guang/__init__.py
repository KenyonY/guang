'''
This is a universal function library.
'''
from . import *
import sys
sys.path.append('..')

import version
def get_version():
    v= version.version
    v += 1
    with open('version.py','w') as fo:
        fo.write('version= '+ str(v))
    return '.'.join(list(str(v)))

__v = get_version()

# '0.0.7.2.7'
__version__ = '0.0.' + __v
print('__version__:', __version__)
__author__ = 'K.y'
__copyright = 'Copyright 2019 K.y'

__all__ = ["ML","Utils","DL", "Voice", "wechat"]

