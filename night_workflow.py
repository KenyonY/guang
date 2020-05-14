import os
import subprocess
from guang.Utils.toolsFunc import rm
import guang
from generateREADME import generateREADME

generateREADME(guang.__version__)
rm('build')
rm('dist')
rm('guang.egg-info')

os.system('python setup.py sdist bdist_wheel')
upgrade = f'pip uninstall guang -y && pip install dist/guang-{guang.__version__}-py3-none-any.whl'
os.system(upgrade)
rm('build')
rm('guang.egg-info')


"""
>>> res = os.popen(commend) # use os 更简洁
>>> res = subprocess.Popen(commend, shell=True, stdout=subprocess.PIPE).stdout   # use subprocess 适用于更复杂情况
>>> print(res.read())
# or 
>>> res = subprocess.getoutput(commend)
# ps
returncode = subprocess.call(commend)
# is equal to 
returncode = os.system(commend)

# 执行结果保存文件
>>> fhandle = open(filename, "w")
>>> pipe = subprocess.Popen(commend, shell=True, stdout=fhandle).stdout
>>> fhandle.close()

"""

