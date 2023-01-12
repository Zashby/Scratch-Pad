require(ISLR)
require(tidyverse)
attach(airquality)
airquality
?airquality
dim(airquality)
cor(Temp, Ozone)
Temp
Ozone
Ozone[is.na(Ozone)] <- mean(Ozone, na.rm = TRUE)
Ozone <- round(Ozone, digits = 0)
Ozone

Temp[is.na(Temp)] <- mean(Temp, na.rm = TRUE)
Temp <- round(Temp , digits = 0)
Temp

length(Ozone)
cor(Temp, Ozone)
cor(Ozone, Temp)
?cor

aq.lm = lm(Ozone~Temp, data= airquality)
plot(aq.lm)

airquality %>% ggplot(aes(Temp, Ozone))+geom_point()+geom_smooth(
  method=lm, se=F  
)+ggtitle("Linear Model of Ozone against Temperature change")

aq.lm
plot(aq.lm)

plot(Temp, Ozone)
abline(aq.lm)

par(mfrow=c(2,1))


airquality %>% ggplot()+geom_boxplot()
ggplot2.boxplot(data=Ozone)


summary(Temp)
boxplot(Temp, main='Temperature Occurence')
hist(Temp, main='Temperature Occurence')

summary(Ozone)
boxplot(Ozone, main='Ozone Level Occurence')
hist(Ozone, main='Ozone level Occurence')


airquality %>% 
  ggplot(aes(Ozone,color="blue",fill="white"))+
  geom_histogram(binwidth=15,alpha=.5)+
  geom_vline(xintercept=mean(Ozone))+
  geom_vline(xintercept=median(Ozone), linetype="dashed", color="red")

summary(aq.lm)
