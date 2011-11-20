#!/usr/bin/env python

from random import random
import time

# this is just a silly litte script to generate a
# pseudo log file to `tail -f` into the plotter

def log_entry(text):
	fid = open('awwlog.log', 'a')
	fid.write(text+'\n')
	fid.close()

while True:
	log_entry(str(random())+' '+str(random()))
	time.sleep(random()*2)
