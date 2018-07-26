#!/usr/bin/python3.5
import os
import matplotlib.pyplot as plt
import re 
import pylab

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

c15=[]
c20=[]
c25=[]
c30=[]
c35=[]
c40=[]
c45=[]
c50=[]
c55=[]
c60=[]
c62=[]
c64=[]
c66=[]
c68=[]
c70=[]
c72=[]
c74=[]
c76=[]
c78=[]
c80=[]
c90=[]
c100=[]
c150=[]
c200=[]
c250=[]
c300=[]

with open('reportBusco_bord_init_sort.txt') as f :
	for line in f :
			if re.match("^run_15X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n15.append(c)
			if re.match("^run_20X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n20.append(c)
			if re.match("^run_25X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n25.append(c)
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
			if re.match("^run_62X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n62.append(c)
			if re.match("^run_64X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n64.append(c)
			if re.match("^run_66X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n66.append(c)				
			if re.match("^run_68X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n68.append(c)
			if re.match("^run_70X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n70.append(c)
			if re.match("^run_72X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n72.append(c)
			if re.match("^run_74X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n74.append(c)
			if re.match("^run_76X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n76.append(c)
			if re.match("^run_78X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n78.append(c)
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
			if re.match("^run_150X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n150.append(c)
			if re.match("^run_200X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n200.append(c)
			if re.match("^run_250X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n250.append(c)
			if re.match("^run_300X", line) is  not None :
				a,b=line.split("\t")
				c=float(b)
				n300.append(c)

with open('reportBusco_bord_paramSensi_sort.txt') as f :
	for line in f :
			if re.match("^run_15X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c15.append(c)
			if re.match("^run_20X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c20.append(c)
			if re.match("^run_25X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c25.append(c)
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
			if re.match("^run_62X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c62.append(c)
			if re.match("^run_64X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c64.append(c)
			if re.match("^run_66X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c66.append(c)				
			if re.match("^run_68X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c68.append(c)
			if re.match("^run_70X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c70.append(c)
			if re.match("^run_72X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c72.append(c)
			if re.match("^run_74X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c74.append(c)
			if re.match("^run_76X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c76.append(c)
			if re.match("^run_78X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c78.append(c)
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
			if re.match("^run_150X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c150.append(c)
			if re.match("^run_200X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c200.append(c)
			if re.match("^run_250X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				c250.append(c)
			if re.match("^run_300X", line) is  not None :
				a,b=line.split("\t")
				c=float(b)
				c300.append(c)


BoxName = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 90, 100, 150, 200, 250, 300]

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

data=[n15, n20, n25, n30, n35, n40, n45, n50, n55, n60, n62, n64, n66, n68, n70, n72, n74, n76, n78, n80, n90, n100, n150, n200, n250, n300]
print (data)
dataP=[c15, c20, c25, c30, c35, c40, c45, c50, c55, c60, c62, c64, c66, c68, c70, c72, c74, c76, c78, c80, c90, c100, c150, c200, c250, c300]
print (dataP)
plt.figure(figsize=[11,7])
bpData = plt.boxplot(data, sym='', widths=0.6)
set_box_color(bpData, '#43A2CA')
bpDataP = plt.boxplot(dataP, sym='', widths=0.6)
set_box_color(bpDataP, '#DD1C77')

plt.plot([], c='#43A2CA', label='B.pertussis default parameter')
plt.plot([], c='#DD1C77', label='B.pertussis modified parameter')
plt.legend()

plt.axhline(y=100, color='lightgreen', linestyle='-', linewidth=0.7)

#plt.boxplot(data)
pylab.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], BoxName)
#plt.text(10,10,"parameter by default")
plt.title('Distribution of complete gene retrived by coverage (X) - B.pertussis')
plt.ylabel('% of complete gene retrieved')
plt.savefig('boxBusco_bord_init.png')
plt.show()
