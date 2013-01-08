clustergraph<-function(G){
# Run Girvan-Newman's fast-greedy algoithm for community detection:
fgreedy<-fastgreedy.community(G,merges=TRUE, modularity=TRUE,weights=E(G)$weight)
memberships <-community.to.membership(G, fgreedy$merges, steps=which.max(fgreedy$modularity)-1)
print(paste('Number of detected communities=',length(memberships$csize)))
print('Community sizes = ')
print(memberships$csize)
modularity <- max(fgreedy$modularity)
#print(paste('Modularity = ',modularity))
return(c(memberships,modularity))
}



