# setup.py

from setuptools import setup, find_packages

setup(
    name='script',
    version='0.1.0',
    description='''A simple Python package that creates and executes python script files.' 
    Example use-case:
    'An alternative for cv2.imshow for Mac OS
    ''',
    author='Mirza Ali Jaffer',
    packages=find_packages(),  # Automatically finds sub-packages
    python_requires='>=3.6'
)
