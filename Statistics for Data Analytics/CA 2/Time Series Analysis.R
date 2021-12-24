# Importing the eComm_US.csv file into RStudio.
 
timedata = read.csv("/Users/polinaprinii/Documents/Statistics/eComm_US.csv",
                    header = TRUE, stringsAsFactors = FALSE)

# Now we check the class of our time data variable.
class(timedata)

# Now we check the columns of the data-frame.
colnames(timedata)

# Now we print the first 6 rows.
head(timedata)

# Reading the data-frame as a time series object.
timedata.ts = ts(data=timedata['ECOMNSA'], frequency = 4, start = c(1999, 4))

# Checking class of the timedata.ts variable.
class(timedata.ts)

# Checking the start and enf of the timeseries.
start(timedata.ts)
end(timedata.ts)

# Plotting the time-series.
plot(timedata.ts)
autoplot(timedata.ts)
monthplot(timedata.ts)

# Importing ggplot2 library for further analysis.
library(fpp2)

# Running a seasonal plot to evaluate if any seasonality is present in trend.
ggseasonplot(timedata.ts, year.labels=TRUE) +
  ylab("$ Billion") +
  ggtitle("Season plot: Retail Sales")

# Performing seasonal decomposition to evaluate the time series by components.
decom <- decompose(timedata.ts, type = "multiplicative")
plot(decom)
