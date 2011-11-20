#!/usr/bin/env python

import time, sys
import subprocess

proc = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE)
input_buffer = []

def read(buff):
	if sys.stdin:
		point = sys.stdin.readline()
		buff.append(point)
		plot(proc, buff)

def format(line, format_string):
	pass

def set(proc, setting):
	proc.stdin.write(' set %s\n' % setting)

def plot(proc, points):
	proc.stdin.write(" plot '-'\n")
	for point in points:
		proc.stdin.write(point)
	proc.stdin.write('e\n')

def exit(proc):
	proc.communicate('quit')


if __name__=='__main__':

	set(proc, 'style data points')

	while True:
		read(input_buffer)

	exit(proc)
