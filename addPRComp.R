
library(rjson)
toSort = fromJSON( file = "summaries.json" )
bound = do.call(rbind,lapply(toSort,as.data.frame))
bound = cbind(bound,predict(prcomp(as.matrix(bound[,names(bound)!="filename"])))[,c(1:5)])
if (nrow(bound)==length(toSort)) {
  output = apply(bound,1,as.list)
  sapply(output,return)
  cat(file="summaries.json",toJSON(unname(apply(bound,1,as.list))))
}