binPlot=function(binary,split,data){
  ggplot(data=data,aes(split, binary,fill=split))+
    geom_boxplot()+
    scale_y_continuous()
}
