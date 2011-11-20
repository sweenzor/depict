#!/usr/bin/env python

import subprocess
import time

plot = subprocess.Popen(['gnuplot', '-persist'], stdin=subprocess.PIPE)
plot.stdin.write('\n')

for i in range(100):
	plot.stdin.write(' plot sin(x+%i)\n' % i)
	time.sleep(0.1)
