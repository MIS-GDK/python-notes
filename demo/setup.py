from setuptools import setup, find_packages

setup(
    name="demo",  # 包名，真正调用的不是这个包名，这只是一个宏观的包名
    version="0.1",  # 版本号
    packages=find_packages(),  # 所有包含的其他包
)
