#!/usr/bin/python3.5
import os
import matplotlib.pyplot as plt
import re 
import pylab

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

c15=[]
c20=[]
c30=[]
c35=[]
c40=[]
c45=[]
c50=[]
c55=[]
c60=[]
c70=[]
c80=[]
c90=[]
c100=[]
c200=[]
c300=[]

with open('reportBusco_veil_init_sort.txt') as f :
	for line in f :
			if re.match("^run_15X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n15.append(c)
			if re.match("^run_20X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n20.append(c)
			if re.match("^run_30X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n30.append(c)
			if re.match("^run_35X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n35.append(c)
			if re.match("^run_40X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n40.append(c)
			if re.match("^run_45X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n45.append(c)
			if re.match("^run_50X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n50.append(c)
			if re.match("^run_55X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n55.append(c)
			if re.match("^run_60X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n60.append(c)
			if re.match("^run_70X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n70.append(c)
			if re.match("^run_80X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n80.append(c)
			if re.match("^run_90X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n90.append(c)
			if re.match("^run_100X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n100.append(c)
			if re.match("^run_200X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n200.append(c)
			if re.match("^run_300X", line) is  not None :
				a,b=line.split("\t")
				c=float(b)
				n300.append(c)

with open('reportBusco_veil_paramSensi_sort.txt') as f :
	for line in f :
			if re.match("^run_15X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c15.append(c)
			if re.match("^run_20X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c20.append(c)
			if re.match("^run_30X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c30.append(c)
			if re.match("^run_35X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c35.append(c)
			if re.match("^run_40X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c40.append(c)
			if re.match("^run_45X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c45.append(c)
			if re.match("^run_50X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c50.append(c)
			if re.match("^run_55X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c55.append(c)
			if re.match("^run_60X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c60.append(c)
			if re.match("^run_70X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c70.append(c)
			if re.match("^run_80X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c80.append(c)
			if re.match("^run_90X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c90.append(c)
			if re.match("^run_100X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c100.append(c)
			if re.match("^run_200X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c200.append(c)
			if re.match("^run_300X", line) is  not None :
				a,b=line.split("\t")
				c=float(b)
				c300.append(c)


BoxName = [15, 20, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 200, 300]

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

data=[n15, n20, n30, n35, n40, n45, n50, n55, n60, n70, n80, n90, n100, n200, n300]
print (data)
dataP=[c15, c20, c30, c35, c40, c45, c50, c55, c60, c70, c80, c90, c100, c200, c300]
print (dataP)

bpData = plt.boxplot(data, sym='', widths=0.6)
set_box_color(bpData, '#43A2CA')
bpDataP = plt.boxplot(dataP, sym='', widths=0.6)
set_box_color(bpDataP, '#DD1C77')
plt.plot([], c='#43A2CA', label='E.coli default parameter')
plt.plot([], c='#DD1C77', label='E.coli modified parameter')
plt.legend()

plt.axhline(y=100, color='lightgreen', linestyle='-', linewidth=0.7)

#plt.boxplot(data)
pylab.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], BoxName)
#plt.text(10,10,"parameter by default")
plt.title('Distribution of complete gene retrived by coverage (X) - Veillonella')
plt.ylabel('% of complete gene retrieved')
plt.xlabel('coverage (X)')
plt.savefig('boxBusco_veil.png')
plt.show()
