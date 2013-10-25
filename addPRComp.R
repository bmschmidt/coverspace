library(rjson)

#Runs through the json file and adds the first 10 Principal components based on all the other data that has been collected.
toSort = fromJSON( file = "summaries.json" )
bound = do.call(rbind,lapply(toSort,as.data.frame))
matrix = as.matrix(bound[,names(bound)!="filename"])
matrix = apply(matrix,2,rank)
bound = cbind(bound,predict(prcomp(matrix))[,c(1:10)])
if (nrow(bound)>=.9*length(toSort)) { #A few empty rows?
  output = apply(bound,1,as.list)
  cat(file="summaries.json",toJSON(unname(apply(bound,1,as.list))))
}