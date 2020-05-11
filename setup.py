#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import find_packages, setup

with open('README.rst', 'r') as fobj:
    long_description = fobj.read()

setup(
    name='sociophysics',
    version='0.1.0',
    license='BSD-2-Clause',
    description='{project_description}',
    long_description=long_description,
    author='Miguel Gómez Donoso',
    author_email='miguelgdonoso@gmail.com',
    url='https://github.com/MiguelGDonoso/sociophysics',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: BSD License',
    ],
    keywords=[
        'scientific computing',
        'physics',
        'complex systems',
        'dynamical systems',
        'sociophysics',
    ],
    python_requires='>=3.5',
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
    ]
)
