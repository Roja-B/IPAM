
from PARAMETERS import *
f = open(PATH+"/myResults/ComEvolutions","r")
t = open(PATH+"/myResults/Edgelist_comEvolutions.txt","w")
time = 1
# 11062006-11202006	(0,0.571,[0])	(1,0.5,[3])	(2,0.5,[3])	(3,0.476,[2])
prevLine = f.readline()
for nextLine in f:
	nextDate = nextLine.split('\t')[0].strip()
	prevLine = prevLine.strip()
	for entry in prevLine.split('\t'):
        	if "," not in entry : 
			prevDate = entry.strip()
			continue
	        com = entry.split(',')[0].split('(')[1]
        	nextCom = entry.split('[')[1].split(']')[0]
        	prob = entry.split(',')[1]
 		if float(prob)>0:
			if "," in nextCom: 
				nextComs=nextCom.split(',')
				for element in nextComs:
					element = element.strip()
#					t.write("C"+str(time)+"_"+com+'\t'+"C"+str(time+1)+"_"+element+'\t'+prob+'\n')
					t.write(prevDate+"_"+com+'\t'+nextDate+"_"+element+'\t'+prob+'\n')
			else:
				#t.write("C"+str(time)+"_"+com+'\t'+"C"+str(time+1)+"_"+nextCom+'\t'+prob+'\n')
				t.write(prevDate+"_"+com+'\t'+nextDate+"_"+nextCom+'\t'+prob+'\n')
	time += 1
	prevLine = nextLine
f.close()
t.close()
