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

with open('reportQuast_gen_paramSensi_sort.txt') as f :
	for line in f :
			if re.match("^15X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n15.append(c)
			if re.match("^20X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n20.append(c)
			if re.match("^25X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n25.append(c)
			if re.match("^30X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n30.append(c)
			if re.match("^35X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n35.append(c)
			if re.match("^40X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n40.append(c)
			if re.match("^45X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n45.append(c)
			if re.match("^50X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n50.append(c)
			if re.match("^55X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n55.append(c)
			if re.match("^60X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n60.append(c)
			if re.match("^62X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n62.append(c)
			if re.match("^64X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n64.append(c)
			if re.match("^66X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n66.append(c)				
			if re.match("^68X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n68.append(c)
			if re.match("^70X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n70.append(c)
			if re.match("^72X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n72.append(c)
			if re.match("^74X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n74.append(c)
			if re.match("^76X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n76.append(c)
			if re.match("^78X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n78.append(c)
			if re.match("^80X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n80.append(c)
			if re.match("^90X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n90.append(c)
			if re.match("^100X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n100.append(c)
			if re.match("^150X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n150.append(c)
			if re.match("^200X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n200.append(c)
			if re.match("^250X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				n250.append(c)
			if re.match("^300X", line) is  not None :
				a,b=line.split("\t")
				c=float(b)
				n300.append(c)

with open('reportQuast_gen_init_sort.txt') as f :
	for line in f :
			if re.match("^15X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v15.append(c)
			if re.match("^20X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v20.append(c)
			if re.match("^25X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v25.append(c)
			if re.match("^30X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v30.append(c)
			if re.match("^35X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v35.append(c)
			if re.match("^40X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v40.append(c)
			if re.match("^45X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v45.append(c)
			if re.match("^50X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v50.append(c)
			if re.match("^55X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v55.append(c)
			if re.match("^60X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v60.append(c)
			if re.match("^62X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v62.append(c)
			if re.match("^64X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v64.append(c)
			if re.match("^66X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v66.append(c)				
			if re.match("^68X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v68.append(c)
			if re.match("^70X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v70.append(c)
			if re.match("^72X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v72.append(c)
			if re.match("^74X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v74.append(c)
			if re.match("^76X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v76.append(c)
			if re.match("^78X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v78.append(c)
			if re.match("^80X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v80.append(c)
			if re.match("^90X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v90.append(c)
			if re.match("^100X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v100.append(c)
			if re.match("^150X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v150.append(c)
			if re.match("^200X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v200.append(c)
			if re.match("^250X", line) is not None :
				a,b=line.split("\t")
				c=float(b)
				v250.append(c)
			if re.match("^300X", line) is  not None :
				a,b=line.split("\t")
				c=float(b)
				v300.append(c)


BoxName = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 90, 100, 150, 200, 250, 300]

dataParam=[n15, n20, n25, n30, n35, n40, n45, n50, n55, n60, n62, n64, n66, n68, n70, n72, n74, n76, n78, n80, n90, n100, n150, n200, n250, n300]
print ("--------PARAMS--------")
print (dataParam)
dataInit=[v15, v20, v25, v30, v35, v40, v45, v50, v55, v60, v62, v64, v66, v68, v70, v72, v74, v76, v78, v80, v90, v100, v150, v200, v250, v300]
print ("--------INIT--------")
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
plt.plot([], c='#DD1C77', label='default parameter')
plt.plot([], c='#43A2CA', label='modified parameter')
plt.legend()

plt.axhline(y=100, color='lightgreen', linestyle='-', linewidth=0.7)
plt.axvline(x=4, color='grey', linestyle='--', linewidth=1)
plt.axvline(x=10, color='grey', linestyle='--', linewidth=1)
plt.text(1.5, 90, 'high', fontsize = 12,  bbox={'facecolor':'#43A2CA', 'alpha':0.5, 'pad':7})
plt.text(4.5, 90, 'medium', fontsize = 12, bbox={'facecolor':'#43A2CA', 'alpha':0.5, 'pad':7})
plt.text(15.5, 90, 'low',  fontsize = 12, bbox={'facecolor':'#43A2CA', 'alpha':0.5, 'pad':7})

plt.text(8.5, 90, 'high', fontsize = 11, bbox={'facecolor':'#DD1C77', 'alpha':0.5, 'pad':7})
plt.text(19.5, 90, 'high', fontsize = 11, bbox={'facecolor':'#DD1C77', 'alpha':0.5, 'pad':7})

plt.annotate('', xy=(8, 90), xytext=(7.2, 90), arrowprops=dict(arrowstyle="->", facecolor='black'))
plt.annotate('', xy=(18.3, 90), xytext=(17.5, 90), arrowprops=dict(arrowstyle="->", facecolor='black'))

pylab.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], BoxName)
#plt.text(10,10,"parameter by default")
plt.title('Distribution of genome fraction by coverage (X) - B.pertussis')
plt.ylabel('% of genome fraction retrieved')
plt.xlabel('coverage (X)')
plt.savefig('boxplot_quast_gen_txtparam.png', dpi=200)
plt.show()




