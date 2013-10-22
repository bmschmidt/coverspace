
library(rjson)
toSort = fromJSON( file = "summaries.json" )
bound = do.call(rbind,lapply(toSort,as.data.frame))
matrix = as.matrix(bound[,names(bound)!="filename"])
matrix = apply(matrix,2,rank)
bound = cbind(bound,predict(prcomp(matrix)))[,c(1:5)])
if (nrow(bound)==length(toSort)) {
  output = apply(bound,1,as.list)
  sapply(output,return)
  cat(file="summaries.json",toJSON(unname(apply(bound,1,as.list))))
}