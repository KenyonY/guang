import helium
from helium import *
import time
import numpy as np


def roll(orient, times=30):
    if orient == "up":
        ORIENT = helium.UP
    elif orient == "down":
        ORIENT = helium.DOWN
    else:
        pass
    for i in range(times):
        helium.press(ORIENT)
        time.sleep(0.1)


def randtime(t_min=10, tmax=300):
    return t_min + np.random.rand() * tmax


def zhihu():
    try:
        driver = start_chrome("www.baidu.com", headless=True)
        write('知乎')
        time.sleep(1)
        press(ENTER)
        click('发现')
        click(driver.find_element_by_class_name("SearchBar"))
        write('caloi')
        press(ENTER)
        click(Button("关闭"))  # close zhihu sign in
        click("用户")
        click("caloi")
        click(Button("关闭"))  # close zhihu sign in

        click("python进度条")
        roll("down")
        roll("up")
        try:
            click("python-progress-bar")
            roll("down", 50)
        except:
            pass
        time.sleep(randtime(10, 100))
        kill_browser()
        print("zhihu complete")
    except:
        print("zhihu except...........")


def csdn():
    try:
        driver = start_chrome("www.baidu.com", headless=True)
        write('pyprobar')
        time.sleep(1)
        press(ENTER)
        click("python进度条")
        roll("down")
        roll("up")
        click("知乎")
        roll("down")
        roll("up")
        driver.switch_to.window(driver.window_handles[1])  # 切换窗口

        click("简书")
        roll("down")
        roll("up")
        driver.switch_to.window(driver.window_handles[1])  # 切换窗口
        try:
            click("python-progress-bar")
            roll("down", 30)
        except:
            pass
        time.sleep(randtime(10, 50))
        kill_browser()
        print("csdn complete")
    except:
        print("csdn except...........")


def browse(clickable, driver):
    current_window = driver.current_window_handle
    click(clickable)
    print(f"click <{clickable}> success")
    roll("down", 50)
    roll("up", 10)
    driver.switch_to.window(current_window)


def caloi():
    try:
        driver = start_chrome("www.baidu.com", headless=True)
        print("start success")
        write('caloi 简书')
        time.sleep(2)
        press(ENTER)

        roll("down", 4)
        browse("ag 的安装与使用", driver)
        roll("down", 4)
        browse("使用hugo布置网站", driver)
        browse("远程jupyter", driver)
        browse("ubuntu18.04 安装配置apache2笔记", driver)
        roll("down", 4)
        browse("linux下代替find命令的工具: fzf", driver)
        #         time.sleep(randtime())
        kill_browser()
        print("csdn complete")
    except:
        print("caloi except...........")
        return


if __name__ == "__main__":
    for counts in range(10):
        print(counts)
        zhihu()
        csdn()
        caloi()
