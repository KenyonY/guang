from enum import IntEnum
import time
import datetime
from datetime import timedelta, timezone
import numpy as np
from .time import beijing
from colorama import init, Fore, Back, Style

# class beijing:
#     # utc_time = datetime.utcnow()
#     utc_time = datetime.datetime.now(tz=timezone.utc)
#     bj_time = utc_time.astimezone(timezone(timedelta(hours=8)))
#     now = bj_time.now()

class Fc(IntEnum):
    """Foreground color"""
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    white = 37
class Bc(IntEnum):
    """Background color"""
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    magenta = 45
    cyan = 46
    white = 47
class Disp(IntEnum):
    """Effect of display"""
    default = 0
    highlight = 1
    underline = 4
    twinkle = 5 # 闪烁
    reverse = 6 # 反白显示
    invisible = 8

def cprint(string, fc=Fc.cyan, bg=False, bc=Bc.black, coverage='\r'):

    if bg:
        print(f'{coverage}\033[{Disp.highlight};{fc};{bc}m{string}\033[0m', end='', flush=True)
    else:
        print(f'{coverage}\033[{Disp.highlight};{fc}m{string}\033[0m', end='', flush=True)


def bar(current_size, total_size, color='random', first_time=[time.time()]):
    # init(autoreset=True)
    percent = current_size/total_size
    cost_time = time.time() - first_time[0]
    total_time = cost_time/percent
    remain_time = int(total_time - cost_time)
    remain_time = timedelta(seconds=remain_time)
    ETC = f"{remain_time}| {(datetime.datetime.now() + remain_time).strftime('%m-%d %H:%M:%S')}"

    unit_percent = 0.034
    total_space = 29
    n_sign1, mod_sign1 = divmod(percent, unit_percent)
    N1 = int(np.ceil(n_sign1))

    sign1 = "█" * N1
    N0 = int((mod_sign1/unit_percent) * (total_space - N1)) +1
    sign0 = '>' * N0
    SIGN = '|' + sign1 + sign0 + (total_space- N1 - N0) * ' ' + '|'
    if color == "random":
        color_list = dir(Fore)[:17]
        color1 = Fore.BLACK # eval("Fore."+np.random.choice(color_list))
        color2 = Fore.LIGHTBLACK_EX # eval("Fore." + np.random.choice(color_list))
        color3 = Fore.LIGHTYELLOW_EX # eval("Fore." + np.random.choice(color_list))
        print(color1 +f"\r{percent*100:.2f}% ", color2+SIGN, color3 +f"ETC {ETC}", end='', flush=True)
    # cprint(f"{percent*100:.2f}%  ")
    # cprint(f"ETC {ETC}", fc=Fc.black, coverage='')


class probar:
    """
    Simple progress bar display, to instead of tqdm.
    """

    def __init__(self, iterable, total_steps=None):
        self.iterable = iterable
        self.t0 = time.time()
        self.c = 0
        # self.cT = datetime.datetime.now()
        self.cT = beijing.now
        if hasattr(iterable, '__len__'):
            self.total_steps = len(iterable) - 1
        else:
            self.total_steps = total_steps
            if self.total_steps == None:
                raise ValueError(f'{iterable} has no __len__ attr, use total_steps param')

    def __iter__(self):
        for idx, i in enumerate(self.iterable):
            if idx == 0:
                # cprint(f'{0:.2f}% \t  {0:.1f}|{np.inf:.1f}s ')
                print(f"\r{0:.2f}% \t  {0:.1f}|{np.inf:.1f}s ", end='', flush=True)
                d_percent = 0.01
            else:
                percent = self.c / self.total_steps
                PERCENT = percent * 100

                if PERCENT >= d_percent:
                    d_percent += 0.01
                    cost_time = time.time() - self.t0
                    cost_minute, cost_second = divmod(cost_time, 60)

                    total_time = cost_time / percent
                    t_minute, t_second = divmod(total_time, 60)
                    dT = datetime.timedelta(0, total_time)
                    deadLine = self.cT + dT
                    _PERCENT=f"{PERCENT:.2f}%"
                    _COST = f"""\t{cost_minute:.0f}'{cost_second:.1f}\"|{t_minute:.0f}'{t_second:.1f}\""""
                    _ETC = f"\tETC: {deadLine.month}-{deadLine.day} {deadLine.hour}:{deadLine.minute}:{deadLine.second}"

                    print(Fore.CYAN +f"\r{_PERCENT}", Fore.GREEN +_COST, Fore.YELLOW +_ETC, end='', flush=True)
                    # cprint(_PERCENT, fc=Fc.cyan)
                    # cprint(_COST, fc=Fc.green, coverage='')
                    # cprint(_ETC, fc=Fc.yellow, coverage='')

            yield idx, i
            self.c += 1

def _test1():
    for i in range(1,10):
        time.sleep(1)
        bar(i, 9)
def _test2():
    for idx, i in probar(range(15)):
        time.sleep(1)


if __name__=="__main__":
    # _test1()
    _test2()