# This program reads the table of program names and sizes and adds the size attribute to the nodes in graph.
library(igraph)

progsizes<-read.table("ProgramSizes.txt",header=FALSE,sep="\t")

for (i in 1:(length(V(G))+1)){
V(G)[which(V(G)$name == progsizes$V1[i])-1]$size <- progsizes$V2[i]
}



