import numpy as np
import os
import shutil
import time
import datetime

class probar:
    """
    Simple progress bar display, to instead of tqdm.
    """
    def __init__(self, iterable, total_steps=None):
        self.iterable = iterable
        self.t0 = time.time()
        self.c = 0
        self.cT = datetime.datetime.now()
        if hasattr(iterable, '__len__'):
            self.total_steps = len(iterable) -1
        else:
            print(f'{iterable} has no __len__ attr, use total_steps param')
            self.total_steps = total_steps  -1
            if self.total_steps:
                self.total_steps = self.total_steps
        
    def __iter__(self):
        for idx, i in enumerate(self.iterable):
            if idx == 0:
                print(f'\r{0:.2f}% \t  {0:.1f}|{np.inf:.1f}s \t', end='', flush=1)
            else:
                cost_time = time.time() - self.t0
                percent = self.c/self.total_steps
                total_time = cost_time/percent
                t_minute, t_second = divmod(total_time, 60)
                cost_minute, cost_second = divmod(cost_time, 60)
                dT = datetime.timedelta(0, total_time)
                deadLine = self.cT + dT

                print(f"\r{percent*100:.2f}% \t{cost_minute:.0f}'{cost_second:.1f}\"|{t_minute:.0f}'{t_second:.1f}\"\tExpect:\
{deadLine.month}-{deadLine.day} \
{deadLine.hour}:{deadLine.minute}:{deadLine.second} \t", end='', flush=1)
            yield idx, i
            self.c += 1

def broadcast(func):
    '''
        example:
        @broadcast
        def f(x):
            # A function that can map only a single element
            if x==1 or x==0:
                return x
            else:
                return f(x-1)+f(x-2)
            
        >> f([2,4,10])
        >> array([1, 3, 832040], dtype=object)
    '''
    def wrap(*args, **kwargs):
        '''
        Takes an arbitrary Python function and returns a NumPy ufunc
        Can be used, for example, to add broadcasting to a built-in Python function
        return: only one out, 
        type:numpy object

        '''
        nin, nout = len(args)+len(kwargs), 1
        return np.frompyfunc(func,nin, nout)(*args, **kwargs)
    return wrap

# :Enables the dictionary to be dot operated
class _Dict_enhance(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self 

def dict_dotable(dic):
    '''
    : input: a dictionary
    : output: an enhanced dictionary
    Example:
        enhance_dic = dict_dotable(dic)
    then, you can operate an enhanced dictionary like this:
        enhance_dic.key1.key2. ...
    '''
    dic = _Dict_enhance(dic)
    for i in dic:
        if type(dic[i]) == dict:
            dic[i] = dict_dotable(dic[i])
    return dic


# define a constant like C language.
class Cons:
    '''
    `object.__setattr__(self, name, value)`
    this built-in function will called when assigning values to properties of the class
    
    `object.__dict__` holds all writable attributes in object, 
    key as variable name and value as variable value.
    '''
    def __setattr__(self, name,value):
        if hasattr(self,name):
            raise " "
        else:
            self.__dict__[name] = value


def rm(path):
    '''remove path
    '''
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            print(f'{path} is  illegal !')