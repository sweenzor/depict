#!/usr/bin/env python

import subprocess
import time
import random

proc = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE)

def set(setting):
	proc.stdin.write(' set %s' % setting)

def plot(function):
	proc.stdin.write(' plot %s\n' % function)

def exit(proc):
	proc.communicate('quit')


if __name__=='__main__':

	#set('style function dots')

	for i in range(100):
		proc.stdin.write(" plot '-'\n")
		for i in range(10000):
			proc.stdin.write('%f %f\n' % (random.random(), random.random()))
		proc.stdin.write('e\n')
		time.sleep(0.1)

	#exit(proc)
