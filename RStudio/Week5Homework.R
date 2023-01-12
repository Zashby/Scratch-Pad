require(ISLR)
?College
College
dim(College)

set.seed(1)

?sample
train=sample(1:dim(College)[1], dim(College)[1]/2)
College.train = College[train,]
College.test = College[-train,]

lm.fit = lm(Apps~., data=College.train)
lm.fit
lm.pred= predict(lm.fit, College.test)
?table
mean((College.test$Apps-predict(lm.fit,College.test))^2)
mean((lm.pred - College.test$Apps)^2)

require(glmnet)
train.matrix=model.matrix(Apps~.,data=College.train)
train.y=College.train[,"Apps"]
test.matrix=model.matrix(Apps~., data=College.test)
test.y=College.test[,"Apps"]
grid = 10^seq(4,-2,length=100)
ridge.fit=cv.glmnet(train.matrix,College.train[,"Apps"],alpha=0, lambda=grid,thresh=1e-12)
ridge.Blambda=ridge.fit$lambda.min
ridge.Blambda

ridge.cv=cv.glmnet(train.matrix,College.train$Apps,alpha=0,lambda=grid, thresh=1e-12)
ridge.Blambda=ridge.cv$lambda.min
ridge.Blambda

train.mat <- model.matrix(Apps ~ ., data = College.train)
test.mat <- model.matrix(Apps ~ ., data = College.test)
grid <- 10 ^ seq(4, -2, length = 100)
fit.ridge <- glmnet(train.mat, College.train$Apps, alpha = 0, lambda = grid, thresh = 1e-12)
cv.ridge <- cv.glmnet(train.mat, College.train$Apps, alpha = 0, lambda = grid, thresh = 1e-12)
bestlam.ridge <- cv.ridge$lambda.min
bestlam.ridge



set.seed(1)
model.form <- Apps ~ .
library(ISLR)
data(College)
names(College)
train <- sample(1:nrow(College), size = nrow(College)/2)
Training <- College[train, ]
Testing <- College[ - train, ]

lm.fit <- lm(model.form, data=Training)
lm.pred <- predict(lm.fit, newdata = Testing)
mean((Testing$Apps - lm.pred)^2)

library(glmnet)


Training.x <- model.matrix(model.form, data = Training)
ridge.cv <- cv.glmnet(Training.x , Training$Apps, alpha = 0)
ridge.cv$lambda.min

Testing.x <- model.matrix(model.form, data = Testing)
ridge.pred <- predict(ridge.cv, newx = Testing.x, s = ridge.cv$lambda.min)
mean((Testing$Apps - ridge.pred)^2)

lasso.cv = cv.glmnet(Training.x, Training$Apps,alpha=1)
lasso.cv$lambda.min

lasso.pred = predict(lasso.cv,newx=Testing.x,s=lasso.cv$lambda.min)
mean((Testing$Apps-lasso.pred)^2)

install.packages('pls')
library(pls)
pcr.fit = pcr(model.form, data=Training, validation = "CV")
validationplot(pcr.fit, val.type="MSEP")
pcr.pred = predict(pcr.fit, newdata=Testing, ncomp=5)
mean((Testing$Apps - pcr.pred)^2)


pls.fit = plsr(model.form, data=Training, scale=TRUE, valdation = 'CV')
validationplot(pls.fit, val.type="MSEP")

pls.pred=predict(pls.fit, newdata=Testing,ncomp=4)
mean((Testing$Apps-pls.pred)^2)
pls.pred=predict(pls.fit, newdata=Testing,ncomp=5)
mean((Testing$Apps-pls.pred)^2)

test.avg=mean(Testing$Apps)
lm.r2=1-(mean((Testing$Apps - lm.pred)^2))/mean((test.avg-Testing$Apps)^2)
ridge.r2 = 1-(mean((Testing$Apps - ridge.pred)^2))/mean((test.avg-Testing$Apps)^2)
lasso.r2 = 1-(mean((Testing$Apps - lasso.pred)^2))/mean((test.avg-Testing$Apps)^2)
pcr.r2 = 1-(mean((Testing$Apps - pcr.pred)^2))/mean((test.avg-Testing$Apps)^2)
pls.r2= 1-(mean((Testing$Apps - pls.pred)^2))/mean((test.avg-Testing$Apps)^2)

lm.r2
ridge.r2
lasso.r2
pcr.r2
pls.r2
boxplot(College$Apps, main="Apps per college")
summary(Training$Apps)




# question 10

set.seed(1)

n=1000
p=20

x=matrix(rnorm(n*p),n,p)
b = rnorm(p)
# I am lazy, if this were python I would use a randint method for this.
for(i in 1:19){
  if(i%%3==0){
    b[i]=0
  }
}
b

epsilon = rnorm(1000)
y=x%*% b +epsilon

observe=100
train=sample(seq(n), observe, replace=FALSE)
test = -train
x.train = x[train,]
x.test=x[test,]
y.train=y[train,]
y.test=y[test,]

library(leaps)

df.train = data.frame(y=y.train, x=x.train)
fit.full = regsubsets(y~.,data=df.train,nvmax=20)
matrix.train = model.matrix(y~., data=df.train, nvmax=20)
val.errors=rep(NA,20)
for( i in 1:20){
  coefi = coef(fit.full, id=i)
  pred=matrix.train[,names(coefi)]%*% coefi
  val.errors[i]=mean((pred-y.train)^2)
}

plot(val.errors, xlab="Number of prediction variables", ylab="Training Mean Squared Error",pch=19, type="b")


df.test = data.frame(y=y.test,x=x.test)
matrix.test = model.matrix(y~., data=df.test, nvmax=20)
val.errors.test = rep(NA,20)
for( i in 1:20){
  coefi = coef(fit.full, id=i)
  pred=matrix.test[,names(coefi)]%*% coefi
  val.errors.test[i]=mean((pred-y.test)^2)
}
plot(val.errors.test,main="Test error", xlab="Number of prediction variables", ylab="Test Mean Squared Error",pch=19, type="b")
which.min(val.errors.test)
sd(val.errors.test)
val.errors.test[15]
coef(fit.full, which.min(val.errors.test))


value.errors.true <- rep(NA, 20)
col.x = colnames(x, do.NULL = FALSE, prefix = "x.")
for (i in 1:20) {
  coefi = coef(fit.full, id = i)
  value.errors.true[i] = sqrt(sum((b[col.x %in% names(coefi)] - coefi[names(coefi) %in% col.x])^2) )
}
plot(value.errors.true, xlab = "Number of coefficients", ylab = "Coefficient error between True and Fit data", pch = 19, type = "b")


value.errors.true2 <- rep(NA, 20)
col.x = colnames(x, do.NULL = FALSE, prefix = "x.")
for (i in 1:20) {
  coefi = coef(fit.full, id = i)
  value.errors.true2[i] = sqrt(sum((b[names(coefi)] - coefi)^2))
}
plot(1:20,value.errors.true2, xlab = "Number of coefficients", ylab = "Coefficient error between True and Fit data", pch = 19, type = "b")
names(fit.full)
coef(fit.full)
colnames(col.x)
col.x
