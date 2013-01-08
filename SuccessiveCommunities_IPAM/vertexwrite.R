vertexwrite <- function(memberships, G, name){
write(c("com","vertices","edges","density"),file="communityStats",ncolumns=4)
for (i in 0:(length(memberships$csize)-1)){
	Vi=which(memberships$membership==i)-1 # V is the index of nodes in V(G) that belong to community i
	if (length(Vi)<2){
#		write(c(i,length(V(Gi)),"NA","NA"),file="communityStats",ncolumns=4,append=TRUE)
		next}
	Gi=subgraph(G,Vi) # V(Gi) will have the "names" of the nodes in V(G) that belong to community i
	filename=paste('community',i,sep="")
	write(V(Gi)$name,file=filename,ncolumns=1)
#	filename = paste('G',name,i)
#	write(Gi,file=filename)
#	filename=paste("VertexIndex",name,i,sep="")
#	write(Vi,file=filename,ncolumns=1)
# here report size and density of each com
	stats<- c(i,length(V(Gi)),length(E(Gi)),graph.density(Gi))
        write(stats,file="communityStats",ncolumns=4,append=TRUE)
#	pagerank <- page.rank(Gi,vids=V(Gi),directed=FALSE,weights=E(Gi)$weight)
#	filename = paste("pageranks",i,sep="")
#	write(pagerank$vector,file=filename,ncolumns=1)
}
}
