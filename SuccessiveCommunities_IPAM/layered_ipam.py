import math
from PARAMETERS import *
import pygraphviz as pgv
#PATH = "/media/data3/roja/IPAM"
#SLIDE = 1 # years
#WINDOW = 2 # years

f1 = open(PATH+"/myResults/Edgelist_comEvolutions.txt","r")
f2 = open(PATH+"/myResults/CommunitySizes","r")

G=pgv.AGraph(ranksep='2')
nodesizes = dict()
for line in f2:
	node = line.split()[0]
	nodesize = int(line.split()[2])
	nodesizes[node] = nodesize

#print nodesizes

for line in f1:
	line = line.strip()
	node1 = line.split()[0]
	node2 = line.split()[1]
	edgeWeight = str(10*float(line.split()[2]))
#	print node1
	if node1 not in nodesizes.keys(): nodesizes[node1] = 3
        if node2 not in nodesizes.keys(): nodesizes[node2] = 3
	size1= int(nodesizes[node1])
	size2= int(nodesizes[node2])
	#size1= int(math.sqrt(nodesizes[node1]))
	#size2= int(math.sqrt(nodesizes[node2]))
#	size1 = 5
#	size2 = 5
#	G.add_node(node1,group=node1.split("_")[0]) #size=nodesizes[node1])
	G.add_node(node1,group=node1.split("_")[0],fontsize=size1,penwidth=size1)#'setfontsize(20)')#+str(int(nodesizes[node1]/2))+')')
#	print node2
        G.add_node(node2,group=node1.split("_")[0],fontsize=size2,penwidth=size2)#+str(nodesizes[node2])+')') 
#        G.add_node(node2,group=node2.split("_")[0]) #size=nodesizes[node2])
	G.add_edge(node1,node2,style='setlinewidth('+edgeWeight+')')	
	
G.graph_attr['outputorder']='edgesfirst'
G.write(PATH+"/myResults/IPAMfile.dot")
G.layout(prog='dot')
G.draw(PATH+'/myResults/IPAMLayeredNetwork_W'+str(WINDOW)+'S'+str(SLIDE)+MODE+'.pdf')

f1.close()
f2.close()

