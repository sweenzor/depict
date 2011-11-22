#!/usr/bin/env python

import time, sys
import subprocess

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


def read_stdin(buff):
	"""Upon input on stdin.."""

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
	input_buffer = PlotBuffer()

	while True:
		read_stdin(input_buffer)

	exit(proc)
