import io
import re

from collections import OrderedDict
from setuptools import setup, find_packages


with io.open('data_validator/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='data_validator',
    version=version,
    url='https://github.com/jucyai/data_validator',
    project_urls=OrderedDict((
        ('Code', 'https://github.com/jucyai/data_validator'),
        ('Issue tracker', 'https://github.com/jucyai/data_validator/issues'),
    )),
    license='MIT',
    author='Jiachen Yao',
    maintainer='Jiachen Yao',
    description='Data Validator ABC',
    long_description='Data Validator ABC',
    packages=find_packages(include=['data_validator']),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
            'tox'
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)