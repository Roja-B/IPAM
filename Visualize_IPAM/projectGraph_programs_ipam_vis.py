# Unipartite Projection 
# Creates Unipartite graph using Jaccard Index from a bipartite graph 
# Input: Bipartite Graph
# 	Form: "EdgeList"
import math
import sys
import string
from PARAMETERS import *

def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)
degreeThreshold = 0
coefficient = 100
sigDigit = 4
bgraphname = ''.join([PATH,"/myIntermediateFiles/EdgeList_resolved"]) 
ugraphname = ''.join([PATH,"/myIntermediateFiles/unipartite.txt"])
f = open(bgraphname,"r")
t = open(ugraphname,"w")
Participants = dict()
for line in f:
	L1 = line.strip().split("\t")
	program = L1[0]
	participant = L1[1]
	try: Participants[program].add(participant)
	except KeyError: 
#		print program
		Participants[program] = set()
		Participants[program].add(participant)
f.close()


zeros = 0.0
edges = 0.0
numPrograms = len(Participants.keys())
for i in range(numPrograms):
	for j in range(i+1,numPrograms):
#		print i,j
		prog1 = Participants.keys()[i]
		prog2 = Participants.keys()[j]
		denominator = float(len(set.union(Participants[prog1],Participants[prog2])))
#set(user_links[u1]).union(set(user_links[u2]))))
		if denominator == 0.0:
			continue
		numerator = float(len(set.intersection(Participants[prog1],Participants[prog2])))
		weight = round(coefficient*(numerator/denominator),sigDigit)
		if weight == 0.0:
			zeros = zeros + 1
			print prog1,prog2
			continue
		t.write(str(prog1)+' '+str(prog2)+' '+str(weight)+'\n')
		edges = edges+1
t.close()
combinations = nCr(numPrograms,2)
eDensity = round(edges/combinations,sigDigit)
#print "There were "+str(len(eliminations)) +" eliminations with a minimum threshold of "+str(voteThreshold)+" votes."
print "Coefficient multiplier for Jaccard Index: "+str(coefficient)
print "There are "+str(numPrograms)+" valid programs."		
print "Total possible combinations between each pair: "+str(combinations)
#	print "Total number of edges: " + str(int(edges))+ " | "+str(round(perEdges,2))+" Percent"
#	print "Total number of zeros: " + str(int(zeros))+ " | "+str(round(perZeros,2))+" Percent"
#h.close()
################################################
