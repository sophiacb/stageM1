#!/usr/bin/python3.5
import os
import matplotlib.pyplot as plt
import re 
import pylab
import numpy as np



#COLI PARAMSENSI
v15=[]
v20=[]
v30=[]
v35=[]
v40=[]
v45=[]
v50=[]
v55=[]
v60=[]
v70=[]
v80=[]
v90=[]
v100=[]
v200=[]
v300=[]

n15=[]
n20=[]
n30=[]
n35=[]
n40=[]
n45=[]
n50=[]
n55=[]
n60=[]
n70=[]
n80=[]
n90=[]
n100=[]
n200=[]
n300=[]

with open('reportCanu_coli_init_sort.txt') as f :
	for line in f :
			if re.match("^sampleC_15X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n15.append(c)
			if re.match("^sampleC_20X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n20.append(c)
			if re.match("^sampleC_30X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n30.append(c)
			if re.match("^sampleC_35X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n35.append(c)
			if re.match("^sampleC_40X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n40.append(c)
			if re.match("^sampleC_45X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n45.append(c)
			if re.match("^sampleC_50X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n50.append(c)
			if re.match("^sampleC_55X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n55.append(c)
			if re.match("^sampleC_60X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n60.append(c)
			if re.match("^sampleC_70X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n70.append(c)
			if re.match("^sampleC_80X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n80.append(c)
			if re.match("^sampleC_90X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n90.append(c)
			if re.match("^sampleC_100X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n100.append(c)
			if re.match("^sampleC_200X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n200.append(c)
			if re.match("^sampleC_300X", line) is  not None :
				a,b=line.split("\t")
				c=int(b)
				n300.append(c)

with open('reportCanu_coli_paramSensi_sort.txt') as f :
	for line in f :
			if re.match("^sampleC_15X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v15.append(c)
			if re.match("^sampleC_20X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v20.append(c)
			if re.match("^sampleC_30X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v30.append(c)
			if re.match("^sampleC_35X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v35.append(c)
			if re.match("^sampleC_40X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v40.append(c)
			if re.match("^sampleC_45X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v45.append(c)
			if re.match("^sampleC_50X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v50.append(c)
			if re.match("^sampleC_55X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v55.append(c)
			if re.match("^sampleC_60X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v60.append(c)
			if re.match("^sampleC_70X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v70.append(c)
			if re.match("^sampleC_80X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v80.append(c)
			if re.match("^sampleC_90X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v90.append(c)
			if re.match("^sampleC_100X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v100.append(c)
			if re.match("^sampleC_200X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v200.append(c)
			if re.match("^sampleC_300X", line) is  not None :
				a,b=line.split("\t")
				c=int(b)
				v300.append(c)


BoxName = [15, 20, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 150, 200, 250, 300]

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)


dataColi=[n15, n20, n30, n35, n40, n45, n50, n55, n60, n70, n80, n90, n100, n200, n300]
print ('------ COLI  INIT DATA -------')
print (dataColi)
dataColiSensi=[v15, v20, v30, v35, v40, v45, v50, v55, v60, v70, v80, v90, v100,  v200, v300]
print ('------ COLI PARAMSENSI DATA -------')
print (dataColiSensi)

bpColi = plt.boxplot(dataColi, sym='', widths=0.6)
bpColiSensi = plt.boxplot(dataColiSensi, sym='', widths=0.6)
set_box_color(bpColi, '#43A2CA') #Colors from http://colorbrewer2.org/
set_box_color(bpColiSensi, '#DD1C77')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#43A2CA', label='Veillonella default parameter')
plt.plot([], c='#DD1C77', label='Veillonella modified parameter')
plt.legend()

plt.axhline(y=1, color='lightgreen', linestyle='-', linewidth=0.7)


pylab.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], BoxName)
plt.title('Distribution of contigs by coverage (X) - E.coli')
plt.ylabel('# contigs')
plt.xlabel('coverage (X)')
plt.savefig('boxCanu_coli.png')
plt.show()




