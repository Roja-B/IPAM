library(igraph)
G<-read.graph("EdgeList.ncol", format="ncol",directed="FALSE")
programIndex = which(is.bipartite(G)$type==FALSE)
participantIndex = which(is.bipartite(G)$type==TRUE)


print(paste('Highest participant degree = ',max(degree(G)[participantIndex])))
print(paste('Highest program degree = ',max(degree(G)[programIndex])))
print(V(G)[which(degree(G)==max(degree(G)[participantIndex]))-1])
print(V(G)[which(degree(G)==max(degree(G)[programIndex]))-1])

print(quantile(degree(G)[participantIndex],probs=0.98)) 
print(quantile(degree(G)[programIndex],probs=0.98))


pdf("ParticipantDistribution.pdf")
hist(degree(G)[participantIndex],100,main="Distribution of participant degrees.",xlab="Degree (Number of programs)")
dev.off()

#plot(clustering_stats_ordered$ndates2,clustering_stats_ordered$V2,main="Number of communities over sliding window",xlab="Window start date",ylab="Number of communities in graph","l")


pdf("ProgramDistribution.pdf")
hist(degree(G)[programIndex],20, main="Distribution of program degrees.",xlab="Degree (Number of participants)")
dev.off()

