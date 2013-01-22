#!/usr/lib/python3.0
''' This program creates matrices of transition probabilities between communities at different times.
The sorted timeline (also names of directories) of graphs is in U-pol_J100VT5_stats_combined.txt, the number of communities in each is in NumComsAndModularities'''
import string
import math
from PARAMETERS import *
def intersect(a,b):
        return list(set(a) & set(b))
def union(a,b):
        return list(set(a) | set(b))
#PATH = "/media/data3/roja/IPAM"
#SLIDE = 1 # years
#WINDOW = 2 # years
#START_YEAR = 2000
#END_YEAR = 2013
prefix = ""
def contingency(dirname1,dirname2,numComs1,numComs2):
	PATH1 = dirname1
	PATH2 = dirname2
	filename = PATH1+'/ComContingencyTable.txt'
	t = open(filename,"w")
	tt = open(PATH1+'/TransitionProbs',"w")
	Cluster1 = [set() for i in range(numComs1+1)] # sets of programs in communities at time 1
	Cluster2 = [set() for i in range(numComs2+1)]
	X1 = set() # all the programs at time 1
	X2 = set()
	for i in range(numComs1):
		try: f = open(PATH1+'/community'+str(i),"r")
		except: 
			print PATH1,'/community',str(i)," does not exist (community too small)."
			continue
		for line in f: # populate set with uprograms
			program = line.strip()
			Cluster1[i].add(program)
		X1 = X1 | Cluster1[i] 
		f.close()
	for i in range(numComs2):
       		try: f = open(PATH2+'/community'+str(i),"r")
                except:
                        print PATH2,'/community',str(i)," does not exist (community too small)."
                        continue
	        for line in f:
        	        program = line.strip()
                	Cluster2[i].add(program)
		X2 = X2 | Cluster2[i]
		f.close()
#	Cluster1[numComs1] = X2-X1
#	Cluster2[numComs2] = X1-X2
#	for i in range(numComs1+1):
#                for j in range(numComs2+1):
#	print Cluster1
#	print '------------'
#	print Cluster2
	# create contingency table
	print numComs1, numComs2
	for i in range(numComs1):
		for j in range(numComs2):
			intersection = len(intersect(Cluster1[i],Cluster2[j]))
			t.write(str(intersection)+'\t')
			#print intersection
			if len(Cluster1[i])==0 : tt.write('NA\t') 
			else:
				transitionProb = round(float(intersection)/float(len(Cluster1[i])),3)
				tt.write(`transitionProb`+'\t')
		t.write('\n')
		tt.write('\n')
#	print len(X1-X2)
#	print len(X2-X1)
	t.close()
	return filename
def transitionProb(date,contingencyfilename):
	f = open(contingencyfilename,"r")
	n_t1 = []
	n_t2 = []
	n = []
	i = 0
	# read the contingency table
	for line in f:
       		line = line.strip()
	        n.append([])
        	n[i] = line.split("\t")
        	i += 1
	M1 = len(n) # no. of communities in clustering1
	M2 = len(n[0]) # no. of communities in clustering2
	sum_all = 0
	for i in range(M1):
	        n_t1.append(0)
	        for j in range(M2):
                	sum_all += int(n[i][j])
        	        n_t1[i] += int(n[i][j])
	for j in range(M2):
        	n_t2.append(0)
	        for i in range(M1):
        	        n_t2[j] += int(n[i][j])
#print n_t1
#print n_t2
	N = sum(n_t1)
	#print N, sum_all
	p = []
	for i in range(M1):
        	p.append([])
        	if n_t1[i] == 0 : 
			for j in range(M2):
				p[i].append(0)
			continue
	        for j in range(M2):
        	        p_t1 = float(n_t1[i])/N
	                p_t2 = float(n_t2[j])/N
                	joint_p = float(n[i][j])/sum_all
        	        p[i].append(round(joint_p/p_t1,3))
	#print p
        t = open(PATH+"/LongWay_TrProbs"+date,"w") # these numbers are different from the tranition probabilities calculated above
	for i in range(M1):
		for j in range(M2):
        		t.write(str(p[i][j])+'\t')
		t.write('\n')
        t.close()
#----------- main() ---------------
year = START_YEAR
while year <= END_YEAR-WINDOW-SLIDE+1:
        print year
	if MODE == "NORMAL":
        	dirname1 = ''.join([PATH,"/myResults/",str(year),str(year+WINDOW-1)])
		dirname2 = ''.join([PATH,"/myResults/",str(year+SLIDE),str(year+SLIDE+WINDOW-1)])
	elif MODE == "AGGREGATE":
        	dirname1 = ''.join([PATH,"/myResults/",str(START_YEAR),str(year+WINDOW-1)])
	        dirname2 = ''.join([PATH,"/myResults/",str(START_YEAR),str(year+SLIDE+WINDOW-1)])
	print dirname1,dirname2
	try: f1 = open(''.join([dirname1,"/NumComsAndModularities"])).readline()
	except: 
		year += SLIDE
		continue
        try: f2 = open(''.join([dirname2+"/NumComsAndModularities"])).readline()
	except: 
		print "reached end of list", dirname2
		break
	#print f1
	#print f2
	num1 = int(f1.split(' ')[1])
        num2 = int(f2.split(' ')[1])
	#print dirname1,num1
	#print dirname2,num2 
	print num1,num2
	contingencyfilename = contingency(dirname1,dirname2,num1,num2)
	#rand(date1,contingencyfilename)
	#transitionProb(str(year),contingencyfilename)
	year += SLIDE
