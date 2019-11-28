import os
from guang.Utils.toolsFunc import rm

rm('build')
rm('dist')
rm('guang.egg-info')

os.system('python setup.py sdist bdist_wheel')
os.system('twine upload dist/*')
