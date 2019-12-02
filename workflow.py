import os
from guang.Utils.toolsFunc import rm
from guang.get_version import get_version
get_version(update=True)

rm('build')
rm('dist')
rm('guang.egg-info')

os.system('python setup.py sdist bdist_wheel')
os.system('twine upload dist/*')
