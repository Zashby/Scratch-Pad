ggplot(BOD,aes(Time, demand))+geom_point(size=3)+geom_line(colour="red")

CO2
view(CO2)

CO2 %>% ggplot(aes(conc, uptake, colour=Treatment))+geom_point()+geom_smooth(
method=lm, se=F  
)+facet_wrap(~Type)
CO2 %>% 
  ggplot(aes(Treatment, uptake))+
  geom_boxplot()+
  geom_point(alpha=.5,aes(size=conc, colour=Plant))+
  facet_wrap(~Type)+
  coord_flip()+
  theme_bw()

mpg

newData %>% 
  ggplot(aes(selling_price, year))+
  geom_point(aes(colour=fuel))

newData2 %>% 
  ggplot(aes(fuel, selling_price, color=fuel))+geom_point()+geom_boxplot()



newDataSub %>% 
  ggplot(aes(selling_price, color=fuel,fill=fuel))+
  geom_histogram(binwidth=60000,alpha=.5)+
  geom_vline(xintercept=mean(selling_price))+
  geom_vline(xintercept=median(selling_price), linetype="dashed")
  
