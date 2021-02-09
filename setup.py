'''
install countdownday package
'''
from setuptools import setup
setup(
    name='countdownday',
    version='0.0.1',
    author='athe1sm',
    entry_points={
        "console_scripts":['countdownday = countdownday.__main__:run_prog']
    }
)