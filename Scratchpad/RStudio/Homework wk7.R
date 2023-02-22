require(ISLR)
set.seed(1)
arrest.pr = prcomp(USArrests, scale=TRUE)

arrest.var = arrest.pr$sdev^2

arrest.pve = arrest.var/sum(arrest.var)
arrest.pve

arrest.pr
phi = arrest.pr$rotation

divisor = sum(apply(scale(USArrests)^2,2,sum))

usarrests.proj = scale(USArrests) %*% phi

numerator = apply(usarrests.proj^2,2,sum)
arrest.pve.2 = numerator/divisor
arrest.pve.2

arrest.scaled = scale(USArrests)


arrest.cluster.comp = hclust(dist(arrest.scaled, method='euclidean'), method='complete')
plot(arrest.cluster.comp,xlab='', main='', sub='')

arrest.groups = cutree(arrest.cluster.comp, k=3)
rect.hclust(arrest.cluster.comp, k=3, border="red")
arrest.groups


arrest.cluster.comp = hclust(dist(USArrests, method='euclidean'), method='complete')
plot(arrest.cluster.comp,xlab='', main='', sub='')

arrest.groups = cutree(arrest.cluster.comp, k=3)
rect.hclust(arrest.cluster.comp, k=3, border="red")
arrest.groups


set.seed(1)

 
sim.matrix.x = matrix(rnorm(20*3*50),ncol=50)
sim.matrix.y = rep(c(1,2,3),20)
sim.matrix=cbind(sim.matrix.y,sim.matrix.x)
sim.matrix
dim(sim.matrix)
plot(sim.matrix)
plot(sim.matrix.x)


sim.matrix = rbind(matrix(rnorm(20*50, mean=0.5),nrow=20),matrix(rnorm(20*50, mean=1.0),nrow=20),matrix(rnorm(20*50, mean=1.5),nrow=20))
sim.matrix.y=c(rep(1,20),rep(2,20),rep(3,20))
sim.matrix

sim.pca = prcomp(sim.matrix)$x
summary(sim.pca)
plot(sim.pca[,1:2],col=sim.matrix.y)
  
centroid = kmeans(sim.matrix, centers=3, nstart=20)
table(centroid$cluster, sim.matrix.y)
?kmeans

sim.centroid_2 = kmeans(sim.matrix, centers=2)

table(sim.centroid_2$cluster, sim.matrix.y)

sim.centroid_4 = kmeans(sim.matrix, centers=4)

table(sim.centroid_4$cluster, sim.matrix.y)

sim.pr = prcomp(sim.matrix)

sim.pr.centroid = kmeans(sim.pca[,1:2],centers=3)
table(sim.pr.centroid$cluster, sim.matrix.y)

sim.centroid.scaled = kmeans(scale(sim.matrix,center=FALSE), centers=3)
table(sim.centroid.scaled$cluster, sim.matrix.y)
