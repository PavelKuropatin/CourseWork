from distutils.core import setup
import py2exe
from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Users\Павел\PycharmProjects\CourseWork\controller\mario\r1.png'))]
setup(
    # data_files=data_files,
    windows=['controller/Manager.py'])