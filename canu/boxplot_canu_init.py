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


BoxName = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 90, 100, 150, 200, 250, 300]
def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

data=[n15, n20, n25, n30, n35, n40, n45, n50, n55, n60, n62, n64, n66, n68, n70, n72, n74, n76, n78, n80, n90, n100, n150, n200, n250, n300]
print (data)
plt.figure(figsize=[11,7])
bpData = plt.boxplot(data, sym='', widths=0.6)

set_box_color(bpData, 'blue') #Colors from http://colorbrewer2.org/



plt.axhline(y=1, color='lightgreen', linestyle='-', linewidth=0.7)
pylab.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], BoxName)
plt.ylabel('# contigs')
plt.xlabel('coverage (X)')
plt.title('Distribution of contigs by coverage (X) - B.pertussis')
plt.savefig('boxplot_canu_init.png')
plt.show()




