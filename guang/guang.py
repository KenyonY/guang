import fire
import os
from guang.Utils.toolsFunc import path



def mie():
    origin_wd = os.getcwd()
    os.chdir(r"C:\Users\beidongjiedeguang\OneDrive\a_github\ScatteringLight")
    os.system("streamlit run app.py")
    os.chdir(origin_wd)

def lorenz():
    app_path = path(os.path.join(os.path.dirname(__file__), "app/compose/anim_demo.py"))
    os.system(f"streamlit run {app_path}")

def sawtooth():
    file_path = path(os.path.join(os.path.dirname(__file__), "app/compose/slider.py"))
    os.system(f"python {file_path}")

def geo():
    file_path = path(os.path.join(os.path.dirname(__file__), "geo/compose.py"))
    os.system(f"python {file_path}")



def main():
    fire.Fire()
if __name__ == "__main__":
    main()


