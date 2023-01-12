# Week 6 homework

pos.prob = seq(0,1,.01)
gini = pos.prob*(1-pos.prob)*2

entropy = -(pos.prob*log(pos.prob)+(1-pos.prob)*log(1-pos.prob))

classError = 1-pmax(pos.prob,1-pos.prob)

plot(pos.prob, entropy, type="l", xlab="probability", ylab="measure of error" )
lines(pos.prob, gini, col='red')
lines(pos.prob, classError, col="blue")


#problem 8
set.seed(1)
require(ISLR)
Carseats
set = dim(Carseats)[1]
attach(Carseats)
train = sample(set, set/2)
carseats.train = Carseats[train,]
carseats.test= Carseats[-train,]


require(tree)
?tree

tree.cs = tree(Sales~., data=carseats.train)
summary(tree.cs)

plot(tree.cs)
text(tree.cs, pretty=0)
pred.cs=predict(tree.cs,carseats.test)
mean((carseats.test$Sales-pred.cs)^2)

cv.cs = cv.tree(tree.cs)
names(cv.cs)
plot(cv.cs$size, cv.cs$dev, type='b')

cv.cs

tree.pruned = prune.tree(tree.cs,best=8)
plot(tree.pruned)
text(tree.pruned,pretty=0)

pred.pruned=predict(tree.pruned,carseats.test)
mean((carseats.test$Sales-pred.pruned)^2)

require(randomForest)
?randomForest
bag.cs = randomForest(Sales~., data=carseats.train, mtry=10, ntree=500, importance=TRUE)
pred.bag=predict(bag.cs,carseats.test)
mean((carseats.test$Sales-pred.bag)^2)
importance(bag.cs)


randomf.cs = randomForest(Sales~., data=carseats.train, mtry=10/3, ntree=500, importance=TRUE)
pred.random=predict(randomf.cs,carseats.test)
mean((carseats.test$Sales-pred.random)^2)
importance(randomf.cs)
plot(randomf.cs)


require(ISLR)
OJ
?OJ
train = sample(dim(OJ)[1], 800)
oj.train =  OJ[train,]
oj.test = OJ[-train,]
oj.tree = tree(oj.train$Purchase~.,data=oj.train)
summary(oj.tree)

oj.tree

plot(oj.tree)
text(oj.tree, pretty=0)

oj.pred = predict(oj.tree, oj.test, type="class")
table(oj.test$Purchase, oj.pred)
mean(oj.test$Purchase != oj.pred)

oj.cv=cv.tree(oj.tree)
plot(oj.cv$size, oj.cv$dev, type='b')


oj.pruned= prune.tree(oj.tree, best=5)
plot(oj.pruned)
text(oj.pruned, pretty=0)
oj.pruned
summary(oj.pruned)

oj.pred5 = predict(oj.pruned, oj.test, type="class")
table(oj.test$Purchase, oj.pred5)
mean(oj.test$Purchase != oj.pred5)

oj.pruned8= prune.tree(oj.tree, best=8)
plot(oj.pruned8)
text(oj.pruned8, pretty=0)
oj.pruned8
summary(oj.pruned8)

oj.pred8 = predict(oj.pruned8, oj.test, type="class")
table(oj.test$Purchase, oj.pred8)
mean(oj.test$Purchase != oj.pred8)


?Caravan
train = 1:1000
caravan.train = Caravan[train,]
caravan.test = Caravan[-train,]
dim(Caravan)


fixPurchase = rep(0,nrow(Caravan))
fixPurchase[Caravan$Purchase == "Yes"] <- 1
fixPurchase
Caravan$Purchase
Caravan$Purchase = fixPurchase
Caravan$Purchase


train = 1:1000
caravan.train = Caravan[train,]
caravan.test = Caravan[-train,]
dim(Caravan)
caravan.test$Purchase

sv = 0.01
caravan.boost = gbm(Purchase~., data=caravan.train, distribution="bernoulli", n.trees=1000, shrinkage=sv)
summary(caravan.boost)

caravan.prob=predict(caravan.boost, caravan.test, n.trees=1000, type="response")
willBuy = ifelse(caravan.prob > 0.2,1,0)
table(caravan.test$Purchase, willBuy)

caravan.lr = glm(Purchase~., data=caravan.train, family='binomial')
lr.pred = predict(caravan.lr, newdata=caravan.test, type='response')
lr.willBuy = ifelse(lr.pred>0.2,1,0)
table(caravan.test$Purchase, lr.willBuy)
