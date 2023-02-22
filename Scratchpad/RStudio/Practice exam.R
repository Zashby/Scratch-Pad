require(ISLR)
require(glmnet)
set.seed(1)
day <- read.csv("C:/Users/bored/Desktop/day.csv")
names(day)
#In case I want to mess with things and don't want to reimport the data set
day.manipulate = day
is.null(day)
summary(day)

day.cnt.hist = hist(day$cnt, breaks=20, ylab="frequency of rental", xlab="rental count")

require(tidyverse)

day %>% 
  ggplot(aes(cnt,color="blue",fill="white"))+
  geom_histogram(binwidth=500,alpha=.5)+
  geom_vline(xintercept=mean(day$cnt))+
  geom_vline(xintercept=median(day$cnt), linetype="dashed", color="red")+
  ggtitle("Histogram of Bike Rental Count against Frequency of Rental")


boxplot(day$cnt~day$season,data=day, main="Bicycle Rentals per Season", ylab="Bike rentals", xlab="season (1:spring, 2:summer, 3:fall, 4:winter)")
boxplot(day$cnt~day$weathersit,data=day, main="Bicycle Rentals based on Weather", ylab="Bike rentals", xlab="Weather (1:Clear, 2:Mist+cloudy, 3:Light snow)")

train = sample(1:nrow(day), size=nrow(day)/2)
day.train = day[train,]
day.test = day[-train,]

day.frame=data.frame(day)
cor(day)
library(leaps)



res = cor(day[,3:16])

install.packages("corrplot")
require(corrplot)
corrplot(res) 

#editing extraneous variables from data set

day.train = day.train[,-c(1,2,14,15)]
day.test = day.test[,-c(1,2,14,15)]
day=day[,-c(1,2,14,15)]

#Linear model, full

day.lm_full = lm(cnt~.,day.train)
day.pred.lm_full = predict(day.lm_full, day.test)
mean((day.pred.lm_full - day.test$cnt)^2)

day.lm_1 = lm(cnt~temp+yr,day.train)
day.pred.lm_1 = predict(day.lm_1,day.test)
mean((day.pred.lm_1-day.test$cnt)^2)

day.regfit.full = regsubsets(cnt~.,day.train, nvmax=11)
summary(day.regfit.full)

#5-fold cross validation using best subset selection

k=5
folds=sample(1:k,nrow(cnt),replace=TRUE)
cv.errors=matrix(NA,k,12,dimnames=list(NULL, paste(1:12)))

for(j in 1:k){
  best.fit=regsubsets(cnt~., data=day[folds !=j,], nvmax=12)
  for(i in 1:12){
    pred=predict(best.fit, day[folds++j,],id=i)
    cv.errors[j,i]=mean( (day$cnt[folds==j]-pred)^2)
  }
}
cv.errors

mean.cv.errors=apply(cv.errors,2,mean)
mean.cv.errors
which.min(mean.cv.errors)

day.reg.best=regsubsets(cnt~., data=day, nvmax=12)
coef(day.reg.best,1)

require(glmnet)
x=model.matrix(cnt~., day)[,-1]
y=day$cnt


grid=10^seq(10,-2,length=100)



y.test=y[-train]


cv.out=cv.glmnet(x[train,],y[train],alpha=0)
plot(cv.out)
cv.out$lambda.min

ridge.pred=predict(ridge.mod,s=cv.out$lambda.min,newx=x[-train,])
mean((ridge.pred-y.test)^2)


#PCR
require(pls)
day.pcr = pcr(cnt~., data=day,validation="CV")
summary(day.pcr)

validationplot(day.pcr, val.type="MSEP")

#returns M=7 has the lowest cross-validation error

pcr.fit=pcr(cnt~., data=day, subset=train,validation='CV')
validationplot(pcr.fit,val.type="MSEP")

#Now M=7

pcr.pred=predict(pcr.fit,x[-train,],ncomp=7)
mean((pcr.pred-y.test)^2)

#Tree model

require(tree)

day.tree = tree(cnt~., data=day.train)
summary(day.tree)
plot(day.tree)
text(day.tree,pretty=0)
day.tree.pred_full = predict(day.tree, day.test)
mean((day.test$cnt-day.tree.pred_full)^2)


day.tree.cv=cv.tree(day.tree)
names(day.tree.cv)
plot(day.tree.cv$size,day.tree.cv$dev, type='b')
which.min(day.tree.cv$size)

day.tree.pruned=prune.tree(day.tree,best=6)
plot(day.tree.pruned)
text(day.tree.pruned,pretty=0)
day.tree.pred=predict(day.tree.pruned,day.test)
mean((day.test$cnt-day.tree.pred)^2)


#Bagging
require(randomForest)
day.bag = randomForest(cnt~., data=day.train, mtry=10, ntree=500, importance=TRUE)
pred.bag=predict(day.bag,day.test)
mean((day.test$cnt-pred.bag)^2)
importance(day.bag)


randomf.cs = randomForest(cnt~., data=day.train, mtry=10/3, ntree=500, importance=TRUE)
pred.random=predict(randomf.cs,day.test)
mean((day.test$cnt-pred.random)^2)
importance(randomf.cs)
plot(randomf.cs)
