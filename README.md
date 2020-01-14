# Guang

[![image](https://img.shields.io/badge/Pypi-0.0.7.7.4-green.svg)](https://pypi.org/project/guang)
[![image](https://img.shields.io/badge/python-3.X-blue.svg)](https://www.python.org/)
[![image](https://img.shields.io/badge/license-GNU_GPL--v3-blue.svg)](LICENSE)
[![image](https://img.shields.io/badge/author-K.y-orange.svg?style=flat-square&logo=appveyor)](https://github.com/beidongjiedeguang)




Scientific calculation of universal function library

## Requirements

```python
Python 3
CUDA >= 10.0
PyTorch >= 1.0
Tensorflow >= 1.12.0
opencv-python
pydub
librosa
pyworld
soundfile
pypinyin
pomegranate
python-Levenshtein
```



## Installation

```python
pip install guang
```

​	*Nightly* Build

```python
pip install git+https://github.com/beidongjiedeguang/guang
```



## Examples

- Convert audio in .mp3/ .wav format to (sample rate=16k, single channel) .wav format

  ```python
  from guang.Voice.convert import cvt2wav
  cvt2wav(orig_path, target_path, sr=16000)
  
  # Multi-process
  from guang.Voice.convert import multi_cvt2wav 
  multi_cvt2wav(PATH1, PATH2,sr=16000, n_cpu=None)
  ```



* Use `dict_dotable` to convert a dictionary to dot-able dictionary:

  ```python
  from guang.Utils.toolsFunc import dict_dotable
  a = {'a':{'b':1}}
  a = dict_dotable(a)
  print(a.a.b)
  
  >> 1
  ```

  

* Use `probar` to display current progress

  ```python
  from guang.Utils.toolsFunc import probar
  for idx, x in probar(range(10)):
      time.sleep(0.8)
  
  >> 100.00%         0'7.3"|0'7.3"     Expect: 12-2 23:59:8
  ```

  

* `@broadcast`  broadcast a non-broadcast function.

  ```python
  from guang.Utils.toolsFunc import broadcast
  
  @broadcast
  def f(x):
      # A function that can map only a single element
      if x==1 or x==0:
          return x
      else:
          return f(x-1)+f(x-2)
  
  >> f([2,4,10])
  >> array([1, 3, 832040], dtype=object)
  ```

  

* `txt2ph` Convert Chinese characters to phoneme.

  ```python
  from guang.Voice.txt2pinyin import txt2ph
  txt2ph('你好，我是光')
  
  >> [('n', 'i3'), ('h', 'ao3'), ('sp1',), ('uo3',), ('sh', 'ii4'), ('g', 'uang1')]
  ```




* `reduce_from_duration` Remove files with duration less than `least_time` seconds. 
  Note that this function does not work in the interactive interpreter because it uses [`multiprocessing.pool.Pool`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.pool.Pool)

  ```python
  from guang.Voice.reduce import reduce_from_duration
  
  reduced_list = reduce_from_duration(path_list, least_time=2)
  print(len(path_list), len(reduced_list))
  
  >> (6889, 6714)
  ```



* Find silence part of a sound file: `find_no_silence`

  ```python
  from guang.Voice.reduce import find_no_silence
  start, end, arg_start, arg_end = find_no_silence(filename)
  ```

  

* Download wechat files.

  ```python
  from guang.wechat.Utils.download import downloads
  downloads(nickName='caloi', fileType='mp3', d_t=60)
  ```




* Plots 3D Scatter:

  ```python
  from guang.Utils.plotly import Scatter3d
  from guang.Utils.interesting import Lorenz
  trace = Lorenz.Trace()
  x,y,z = trace[:,0], trace[:,1], trace[:,2]
  
  fig = Scatter3d()
  fig.scatter3d(x,y,z,mode="lines+markers",color_line=z,color_marker=None,marker_size=2)
  fig.show()
  ```
  
  <img src="docs/picture/Lorenz.gif" width = "400" height = "300"/>



* Data dimension reduction:

  ```bash
  cd guang/ML/manifold
  python test_digits.py
  ```

  <img src="docs/picture/digits_dimension_reduction.PNG" width = "800" height = "400" />

  ```bash
  python test_s_curve
  ```

  

  <img src="docs/picture/s_curve.gif" width = "500" height = "500" />

  <img src="docs/picture/s_curve_dimension_reduction.PNG" width = "1000" height = "400"/>











* :smiley: 





























