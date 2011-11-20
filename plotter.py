#!/usr/bin/env python

import time, sys
import subprocess

proc = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE)

def set(proc, setting):
	proc.stdin.write(' set %s' % setting)

def plot(proc, points):
	proc.stdin.write(" plot '-'\n")
	for point in points:
		proc.stdin.write(point)
	proc.stdin.write('e\n')

def exit(proc):
	proc.communicate('quit')


if __name__=='__main__':

	#set('style function dots')
	buff = []

	while True:
		if sys.stdin:
			point = sys.stdin.readline()
			buff.append(point)
			plot(proc, buff)

	#exit(proc)
