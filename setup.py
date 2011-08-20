#! /usr/bin/env python
from setuptools import setup
"""
`werk [status|start|stop] projname`
    keep track of work stop and stop times
"""

setup(
    name='werk',
    version='0.1',
    url='http://github.com/gregglind/werk/',
    license='BSD',
    author='Gregg Lind',
    author_email='gregg.lind@gmail.com',
    description='Simple work tracker',
    long_description=__doc__,
    py_modules=['werk',],
    #packages=['werk'],
    #namespace_packages=['flasktool'],
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    #test_suite='test_tool',
    #classifiers=[
    #    'Environment :: Web Environment',
    #    'Intended Audience :: Developers',
    #    'License :: OSI Approved :: BSD License',
    #    'Operating System :: OS Independent',
    #    'Programming Language :: Python',
    #    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    #    'Topic :: Software Development :: Libraries :: Python Modules'
    #],
    entry_points = {
        'console_scripts': [
            'werk = werk:run'
        ],
    }
)

