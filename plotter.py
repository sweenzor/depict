#!/usr/bin/env python

import subprocess
import time

proc = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE)

def plot(function):
	proc.stdin.write(' plot %s\n' % function)

def exit(proc):
	proc.communicate('quit')


for i in range(100):
	plot('sin(x+%i)' % i)
	time.sleep(0.1)

exit(proc)