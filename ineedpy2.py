#!/usr/bin/env python
#
#  Copyright (c) 2011, Sean Reifschneider <jafo@tummy.com>, tummy.com, ltd.
#  Released under the Python Software Foundation License
#     For more information, see: http://docs.python.org/license.html

'''
Find the latest Python 2 version installed on the system and if this
program is not running on that version, re-invoke it with that version.

BACKGROUND

One of the problems of a system administrator is that enterprise Linux distros
which ship with, and often require, /usr/bin/python to be a fairly old versions.
For example, Python 2.1.  Applications can be very difficult to write such that
they are happy on Python 2.1 and Python 2.7.  Many of these distros include a
newer Python, but it has to be invoked as "python2.6", for example.

You can change the "#!" line in the script, but this makes packaging
more difficult.

EXAMPLES

To make sure you are running on the absolutely latest installed Python 2 on
the system:

	import sys
	print 'Version:', sys.version_info
	import ineedpy2
	ineedpy2.rerunonlatest()

If run on a system with the default Python version being 2.1, but python
2.6 also installed will display:

	Version: (2, 1, 3, 'final', 0)
	Version: (2, 6, 5, 'final', 0)

NOTE: Anything run before the "runonlatestpy2" will be run once on the
older version and once on the newer version.

You can also request the reinvocation only if the python minor version
isn't at least a specific value.  In other words, "I know I need at least
Python 2.4":

		from ineedpy2 import requireminor
		requireminor(4)
'''

import sys
import os


##########################
def _get_latest_python2():
	totry = [ '%s.%s' % ( sys.version_info[0], x ) for x in range(7, 0, -1)
			if x > sys.version_info[1] ]
	for version in totry:
		for path in os.environ.get('PATH').split(':'):
			file = os.path.join(path, 'python%s' % version)
			if os.path.exists(file):
				return file


####################
def rerunonlatest():
	'''Re-execute running program on a more recent version of Python 2, if
	available.  If no newer version is available, just continue current
	program.'''
	latest = _get_latest_python2()
	if not latest: return

	args = sys.argv
	os.execv(latest, [latest] + args)


########################
def requireminor(minor):
	'''Re-invoke only if the minor version is less than the 'minor' argument,
	or running on a newer major version of Python (say, Python 3)'''

	if sys.version_info[0] > '2': return
	if sys.version_info[1] >= minor: return
	rerunonlatest()
