from setuptools import setup, find_packages

setup(
    name = "wallapy",
    version = "0.1.0",
    packages = find_packages(),
    requires= ["pillow", "tqdm", "click"],
    entry_points = {"console_scripts": ["wallapy = wallapy.__main__:main"]}
)