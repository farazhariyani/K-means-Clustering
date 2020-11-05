#import library
library(readxl)

# Load the dataset
#input <- read_excel(file.choose())
data <- read_excel("EastWestAirlines.xlsx")

summary(data)

# Normalize the data
normalized_data <- scale(data) 

summary(normalized_data)

# Elbow curve to decide the k value
twss <- NULL
for (i in 2:12) {
  twss <- c(twss, kmeans(normalized_data, centers = i)$tot.withinss)
}
twss

# Look for an "elbow" in the scree plot
plot(2:12, twss, type = "b", xlab = "Number of Clusters", ylab = "Within groups sum of squares")
title(sub = "K-Means Clustering Scree-Plot")


# 3 Cluster Solution
fit <- kmeans(normalized_data, 6) 
str(fit)
fit$cluster
final <- data.frame(fit$cluster, data) # Append cluster membership

aggregate(data, by = list(fit$cluster), FUN = mean)

# creating a csv file 
library(readr)
write_csv(final, "K-means-ClusteringAssignment_Airlines.csv")

getwd() #to get path where csv file is stored