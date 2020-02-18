import os
from guang.Utils.toolsFunc import rm
from guang.get_version import get_version
from generateREADME import generateREADME
__version__ = get_version(update=True)

generateREADME('0.0.'+ __version__)

rm('build')
rm('dist')
rm('guang.egg-info')

os.system('python setup.py sdist bdist_wheel')
upgrade = f'pip uninstall guang -y && pip install dist/guang-0.0.{__version__}-py3-none-any.whl'
os.system(upgrade)