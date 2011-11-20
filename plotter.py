#!/usr/bin/env python

import time, sys
import subprocess

proc = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE)

def set(setting):
	proc.stdin.write(' set %s' % setting)

def plot(function):
	proc.stdin.write(' plot %s\n' % function)

def exit(proc):
	proc.communicate('quit')


if __name__=='__main__':

	#set('style function dots')

	while True:
		proc.stdin.write(" plot '-'\n")
		line = sys.stdin.readline()
		proc.stdin.write(line)
		proc.stdin.write('e\n')

	#exit(proc)
