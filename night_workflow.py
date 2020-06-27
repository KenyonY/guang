import os
import subprocess
from guang.Utils.toolsFunc import rm
import guang
from generateREADME import generateREADME

generateREADME(guang.__version__)
rm('build')
rm('dist')
rm('guang.egg-info')

# os.system("yapf -i -r ./guang")
os.system('pip uninstall guang -y && python setup.py install')

rm('build')
rm('guang.egg-info')



