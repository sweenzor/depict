#!/usr/bin/env python

import time, sys
import subprocess
import argparse

proc = subprocess.Popen(['gnuplot', '-noraise'], stdin=subprocess.PIPE)

class PlotBuffer(object):
	"""Buffer for holding incoming streaming data"""

	def __init__(self):
		self.buffer = []
	
	def __getitem__(self, key):
		return self.buffer[key]
	
	def manage_size(self):
		if len(self.buffer) > 1000:
			self.buffer = self.buffer[100:]
	
	def append(self, data):
		self.buffer.append(data)

def cmdline_interaction():
	"""Command line argument handler"""

	desc = 'Pipe data into depict to plot'

	parser = argparse.ArgumentParser(
			description=desc)

	parser.add_argument( '-b', '--buffer',
						action='store',
						default=False,
						dest='buffer_size',
						help='set the buffer size')

	cmdargs = parser.parse_args().__dict__

	return cmdargs

def read_stdin(buff):
	"""Upon input on stdin.."""

	if sys.stdin:
		point = sys.stdin.readline()
		point = format(point)
		buff.append(point)
		plot(proc, buff)

def format(line, format_string=''):
	"""Detect formatting (or try too)"""

	# Identify input formed like '(x,x)'
	if '(' and ')' in line:
		line = line[line.find('(')+1:line.find(')')]
		line = line.split(',')
		return str(line[0]+' '+line[1]+'\n')
	
	return line

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

	cmdline_interaction()
	input_buffer = PlotBuffer()

	while True:
		read_stdin(input_buffer)

	exit(proc)
