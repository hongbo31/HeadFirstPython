from distutils.core import setup
import setuptools
setup(
    name='nester',
    version='1.0.0',
    py_modules=['nester'],
    author='Hongbo',
    author_email="315594984@qq.com",
    url='https://github.com/hongbo31/HeadFirstPython',
    description='对列表嵌套列表迭代的处理',
    packages=setuptools.find_packages(),
    classifiers=['Programming Languages ::Python ::3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent']
)