#from distutils.core import setup
from setuptools import setup

setup(
	name='ineedpy2',
	url = 'https://github.com/linsomniac/ineedpy2',
	author = 'Sean Reifschneider',
	author_email = '<jafo@tummy.com>',
	version='1.01',
	py_modules=['ineedpy2',],
	license='Python Software Foundation',
	description = '''Library to swap to newer python version on a multi-version system.''',
	long_description = open('README.markdown', 'r').read(),
)
