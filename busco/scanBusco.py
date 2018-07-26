#!/usr/bin/python3.5 
#-*- coding: utf-8 -*-

import os
import re #pour chercher des mots
import glob #pour gérer plusieurs file

data = {}

for fileReport in glob.glob('run_*/short_summary_*.txt'):
	with open(fileReport, "r") as f :
		for line in f :
			coregenome = re.search(r'\tC:(.*)\%\[S:(.*)\%,D:(.*)\%\],F:(.*)\%,M:(.*)\%', line, re.M|re.I)
			if coregenome is not None : 
				data[fileReport] = coregenome.group(1)
				break
			
print (data)

with open('reportBusco_init.txt', "w") as fout :
	for a, b in data.items():
		fout.write(str(a)+'\t'+str(b)+'\n')
