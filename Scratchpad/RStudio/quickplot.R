quickPlot <- function(response, explanatory, dataset){
  quickfit <- lm(response ~ explanatory, data=dataset)
  plot(explanatory, response, main="Fast plot")
  abline(quickfit, col="red")
  
  }