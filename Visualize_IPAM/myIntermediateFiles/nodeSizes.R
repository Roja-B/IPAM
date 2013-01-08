
library(igraph)
for (i in 1:(length(V(G))+1)){
V(G)[which(V(G)$name == progsizes$V1[i])-1]$size <- progsizes$V2[i]
}

