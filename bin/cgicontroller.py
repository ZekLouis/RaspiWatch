#!/usr/bin/python2

import ConfigParser
import sys

import os 
print "uid = " + str(os.getuid())+ ", gid = " + str(os.getgid())

import os
os.system('touch sdsdsd')

configPath='/home/pi/RaspiWatch/bin/config.cfg'

str = sys.argv[1]
temp = str.split('&')
temp = [i.split('=') for i in temp]
args = []
for i in temp:
	args += i
print args
args = ['padding']+args


if len(args) > 1:
	cfg = ConfigParser.ConfigParser()
	cfg.read(configPath)
	action = args[1]
	if len(args) == 2:
		if action == "off":
			print "kill du programme de detection"
			cfg.set('Section1', 'detectenmarche', False)
			cfg.write(open(configPath,'w'))
		elif action == "on":
			print "lancement du programme de detection"
			cfg.set('Section1', 'detectenmarche', True)
			cfg.write(open(configPath,'w'))
		elif action == "photo":
			print "prise de la bastille(1780)"
			
	elif len(args)%2 == 1:
		
		i = 1
		
		while i < len(args):
	
			
			action2 = args[i]
			if action2 == "res":
			
				if args[i+1]== '1':
					cfg.set('Section1', 'width', '1900')
					cfg.set('Section1', 'height', '1080')
				elif args[i+1]== '2':
					cfg.set('Section1', 'width', '1280')
					cfg.set('Section1', 'height', '720')
				elif args[i+1] == '3':
					cfg.set('Section1', 'width', '640')
					cfg.set('Section1', 'height', '480')
				else:
					cfg.set('Section1', 'width', '1900')
					cfg.set('Section1', 'height', '1080')
					
					
			elif action2 == "ips":
				cfg.set('Section1', 'fps', args[i+1])
				
			elif action2 == "seuil":
				cfg.set('Section1', 'seuil', args[i+1])
				
			elif action2 == "luminosite":
				cfg.set('Section1', 'luminosite', args[i+1])

			i = i + 2
		cfg.write(open(configPath,'w'))
	
	
