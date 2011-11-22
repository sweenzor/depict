#!/usr/bin/env python

from random import random
import time
import os

# this is just a silly litte script to generate a
# pseudo log file to `tail -f` into the plotter

def clear_log():
	fid = open('awwlog.log', 'w')
	fid.close()
		

def log_entry(text):
	fid = open('awwlog.log', 'a')
	fid.write(text+'\n')
	fid.close()


clear_log()
while True:
	log_entry(str(random())+' '+str(random()))
	time.sleep(random()/4)
	print 'generating random log..'
	if os.path.getsize('awwlog.log') > 1000:
		clear_log()