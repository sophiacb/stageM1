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

with open('reportQuast_lenC_paramSensi_sort.txt') as f :
	for line in f :
		if re.match("^15X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n15.append(e)
		if re.match("^20X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n20.append(e)
		if re.match("^25X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n25.append(e)
		if re.match("^30X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n30.append(e)
		if re.match("^35X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n35.append(e)
		if re.match("^40X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n40.append(e)
		if re.match("^45X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n45.append(e)
		if re.match("^50X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n50.append(e)
		if re.match("^55X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n55.append(e)
		if re.match("^60X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n60.append(e)
		if re.match("^62X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")	
			d =float(c)
			e = d/4086189
			n62.append(e)
		if re.match("^64X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n64.append(e)		
		if re.match("^66X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n66.append(e)
		if re.match("^68X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n68.append(e)
		if re.match("^70X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n70.append(e)
		if re.match("^72X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n72.append(e)
		if re.match("^74X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n74.append(e)
		if re.match("^76X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n76.append(e)
		if re.match("^78X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n78.append(e)
		if re.match("^80X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n80.append(e)
		if re.match("^90X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n90.append(e)
		if re.match("^100X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n100.append(e)
		if re.match("^150X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n150.append(e)
		if re.match("^200X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n200.append(e)
		if re.match("^250X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n250.append(e)
		if re.match("^300X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			n300.append(e)

with open('reportQuast_lenC_init_sort.txt') as f :
	for line in f :
		if re.match("^15X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v15.append(e)
		if re.match("^20X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v20.append(e)
		if re.match("^25X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v25.append(e)
		if re.match("^30X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v30.append(e)
		if re.match("^35X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v35.append(e)
		if re.match("^40X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v40.append(e)
		if re.match("^45X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v45.append(e)
		if re.match("^50X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v50.append(e)
		if re.match("^55X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v55.append(e)
		if re.match("^60X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v60.append(e)
		if re.match("^62X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")	
			d =float(c)
			e = d/4086189
			v62.append(e)
		if re.match("^64X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v64.append(e)		
		if re.match("^66X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v66.append(e)
		if re.match("^68X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v68.append(e)
		if re.match("^70X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v70.append(e)
		if re.match("^72X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v72.append(e)
		if re.match("^74X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v74.append(e)
		if re.match("^76X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v76.append(e)
		if re.match("^78X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v78.append(e)
		if re.match("^80X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v80.append(e)
		if re.match("^90X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v90.append(e)
		if re.match("^100X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v100.append(e)
		if re.match("^150X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v150.append(e)
		if re.match("^200X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v200.append(e)
		if re.match("^250X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v250.append(e)
		if re.match("^300X", line) is not None :
			a,b=line.split("\t")
			c = b.replace(" ","").replace("\t","").replace("\n","")
			d =float(c)
			e = d/4086189
			v300.append(e)

BoxName = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 90, 100, 150, 200, 250, 300]

dataParam=[n15, n20, n25, n30, n35, n40, n45, n50, n55, n60, n62, n64, n66, n68, n70, n72, n74, n76, n78, n80, n90, n100, n150, n200, n250, n300]
print (dataParam)

dataInit=[n15, n20, n25, n30, n35, n40, n45, n50, n55, n60, n62, n64, n66, n68, n70, n72, n74, n76, n78, n80, n90, n100, n150, n200, n250, n300]
print (dataInit)

plt.figure(figsize=[11,7])

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

bpParam = plt.boxplot(dataParam, sym='', widths=0.6)
bpInit = plt.boxplot(dataInit, sym='', widths=0.6)
set_box_color(bpParam, '#43A2CA') #Colors from http://colorbrewer2.org/
set_box_color(bpInit, '#DD1C77')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#DD1C77', label='B.pertussis default parameter')
plt.plot([], c='#43A2CA', label='B.pertussis modified parameter')
plt.legend()

plt.axhline(y=1, color='lightgreen', linestyle='-', linewidth=0.7)

pylab.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], BoxName)
sum =(r'$\sum_{i=1}^{n} \frac{contigsLength}{refLength}$')
plt.title('Distribution of {} by coverage (X) - B.pertussis'.format(sum), va='bottom')
plt.ylabel(sum)
plt.xlabel('coverage (X)')
plt.savefig('boxplot_quast_lenC.png', dpi=200)
plt.show()
