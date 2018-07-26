#!/usr/bin/python3.5
import os
import matplotlib.pyplot as plt
import re 
import pylab
import numpy as np



#COLI PARAMSENSI
v15=[]
v20=[]
v25=[]
v30=[]
v35=[]
v40=[]
v45=[]
v50=[]
v55=[]
v60=[]
v62=[]
v64=[]
v66=[]
v68=[]
v70=[]
v72=[]
v74=[]
v76=[]
v78=[]
v80=[]
v90=[]
v100=[]
v150=[]
v200=[]
v250=[]
v300=[]

n15=[]
n20=[]
n25=[]
n30=[]
n35=[]
n40=[]
n45=[]
n50=[]
n55=[]
n60=[]
n62=[]
n64=[]
n66=[]
n68=[]
n70=[]
n72=[]
n74=[]
n76=[]
n78=[]
n80=[]
n90=[]
n100=[]
n150=[]
n200=[]
n250=[]
n300=[]

with open('reportCanu_init_sort.txt') as f :
	for line in f :
			if re.match("^sample_15X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n15.append(c)
			if re.match("^sample_20X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n20.append(c)
			if re.match("^sample_25X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n25.append(c)
			if re.match("^sample_30X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n30.append(c)
			if re.match("^sample_35X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n35.append(c)
			if re.match("^sample_40X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n40.append(c)
			if re.match("^sample_45X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n45.append(c)
			if re.match("^sample_50X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n50.append(c)
			if re.match("^sample_55X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n55.append(c)
			if re.match("^sample_60X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n60.append(c)
			if re.match("^sample_62X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n62.append(c)
			if re.match("^sample_64X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n64.append(c)
			if re.match("^sample_66X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n66.append(c)				
			if re.match("^sample_68X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n68.append(c)
			if re.match("^sample_70X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n70.append(c)
			if re.match("^sample_72X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n72.append(c)
			if re.match("^sample_74X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n74.append(c)
			if re.match("^sample_76X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n76.append(c)
			if re.match("^sample_78X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n78.append(c)
			if re.match("^sample_80X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n80.append(c)
			if re.match("^sample_90X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n90.append(c)
			if re.match("^sample_100X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n100.append(c)
			if re.match("^sample_150X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n150.append(c)
			if re.match("^sample_200X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n200.append(c)
			if re.match("^sample_250X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				n250.append(c)
			if re.match("^sample_300X", line) is  not None :
				a,b=line.split("\t")
				c=int(b)
				n300.append(c)

with open('reportCanu_paramSensi_sort.txt') as f :
	for line in f :
			if re.match("^sample_15X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v15.append(c)
			if re.match("^sample_20X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v20.append(c)
			if re.match("^sample_25X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v25.append(c)
			if re.match("^sample_30X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v30.append(c)
			if re.match("^sample_35X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v35.append(c)
			if re.match("^sample_40X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v40.append(c)
			if re.match("^sample_45X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v45.append(c)
			if re.match("^sample_50X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v50.append(c)
			if re.match("^sample_55X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v55.append(c)
			if re.match("^sample_60X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v60.append(c)
			if re.match("^sample_62X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v62.append(c)
			if re.match("^sample_64X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v64.append(c)
			if re.match("^sample_66X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v66.append(c)
			if re.match("^sample_68X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v68.append(c)
			if re.match("^sample_70X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v70.append(c)
			if re.match("^sample_72X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v72.append(c)
			if re.match("^sample_74X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v74.append(c)
			if re.match("^sample_76X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v76.append(c)
			if re.match("^sample_78X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v78.append(c)
			if re.match("^sample_80X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v80.append(c)
			if re.match("^sample_90X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v90.append(c)
			if re.match("^sample_100X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v100.append(c)
			if re.match("^sample_150X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v150.append(c)
			if re.match("^sample_200X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v200.append(c)
			if re.match("^sample_250X", line) is not None :
				a,b=line.split("\t")
				c=int(b)
				v250.append(c)
			if re.match("^sample_300X", line) is  not None :
				a,b=line.split("\t")
				c=int(b)
				v300.append(c)


BoxName = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 62, 64, 66, 68, 70, 72, 74, 78, 80, 90, 100, 150, 200, 250, 300]

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)


dataColi=[n15, n20, n25, n30, n35, n40, n45, n50, n55, n60, n62, n64, n66, n68, n70, n72, n74, n76, n78, n80, n90, n100, n150, n200, n250, n300]
print ('------ COLI  INIT DATA -------')
print (dataColi)
dataColiSensi=[v15, v20, v25, v30, v35, v40, v45, v50, v55, v60, v62, v64, v66, v68, v70, v72, v74, v76, v78, v80, v90, v100, v150, v200, v250, v300]
print ('------ COLI PARAMSENSI DATA -------')
print (dataColiSensi)
plt.figure(figsize=[11,7])

bpColi = plt.boxplot(dataColi, sym='', widths=0.6)
bpColiSensi = plt.boxplot(dataColiSensi, sym='', widths=0.6)
set_box_color(bpColi, '#43A2CA') #Colors from http://colorbrewer2.org/
set_box_color(bpColiSensi, '#DD1C77')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#43A2CA', label='B.pertussis default parameter')
plt.plot([], c='#DD1C77', label='B.pertussis modified parameter')
plt.legend()

plt.axhline(y=1, color='lightgreen', linestyle='-', linewidth=0.7)


pylab.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], BoxName)
plt.title('Distribution of contigs by coverage (X) - B.pertussis')
plt.ylabel('# contigs')
plt.xlabel('coverage (X)')
plt.savefig('boxCanu_bord.png', dpi=200)
plt.show()




