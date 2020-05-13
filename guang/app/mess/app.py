import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import guang
from glob import glob
import matplotlib as mpl
from guang.Utils.mathFunc import sawtooth
import time

mpl.rc('mathtext',fontset = 'cm',rm = 'serif') 
mpl.rc(["xtick"], direction="in", top=1)
mpl.rc(["ytick"], direction="in", right=1)
mpl.rc('font', family='Times New Roman', size=12)
mpl.rc('lines', linewidth=1.)

# path_list = glob('/data/Downloads/*')
# path = path_list[0]

def listen():
    with open(path, 'rb') as fi:
        voice = fi.read()
    st.audio(voice, format='audio/wav', start_time=0)
    st.write('guang version'+guang.__version__)


def animate():
    
    x = np.linspace(-10, 10, 2000)
    fig,ax = plt.subplots()
    ax.set_ylim(-3, 3)
    line, = ax.plot(x, sawtooth(1,x))
    for i in range(2, 5):
        plt.pause(0.5)
        line.set_ydata(sawtooth(i,x))
        time.sleep(0.05)
        theplot.pyplot()

animate()

def show_Fourier():
    x = np.linspace(-10, 10, 2000)
    fig2, ax2 = plt.subplots()
    n = st.slider('order', 1, 100, 10, 2)
    ax2.plot(x, sawtooth(n, x))
    ax2.set_xlabel(r'$x$')
    ax2.set_ylabel(r'$f(x) = \frac{\sin nx}{x} $')
    st.pyplot()

show_Fourier()

# from guang.wechat import *
# from guang.wechat import dynamic_msg, dynamic_specified_msg, d_time, download_file
# import itchat
# import os
# st.cache(itchat.auto_login(hotReload=True))

# nickName = 'caloi'
# while d_time(60):
#     msg = dynamic_specified_msg(get_userName(nickName)[nickName])
#     msg, download_path = download_file(msg)
#     print(download_path)


    # if os.path.exists(download_path):
    #     with open(download_path, 'rb') as fi:
    #         music = fi.read()
        # st.audio(music, fomat='audio/mp3')












