# Importing Libraries:
library(ggplot2)
library(fpp2)
library(ggfortify)

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

# Checking the start and enf of the time series.
start(timedata.ts)
end(timedata.ts)

# Checking the frequency.
frequency(timedata.ts)

# Printing first 6 rows of the time series.
head(timedata.ts)

# Plotting the time-series.
plot(timedata.ts)
autoplot(timedata.ts, main ="eComm_US Raw Plot")
monthplot(timedata.ts)

# Smoothing the time series.
autoplot(ma(timedata.ts, 3), main = "Smoothed eComm_US Plot")

# Running a seasonal plot to evaluate if any seasonality is present in trend.
ggseasonplot(timedata.ts, year.labels=TRUE) +
  ylab("$ Billion") +
  ggtitle("Seasonal plot: Retail Sales")

# Performing seasonal decomposition to evaluate the time series by components.
decom <- decompose(timedata.ts, type = "multiplicative")
autoplot(decom, main = "Seasonal Decomposition eComm_US Plot")

# Simple Time Series Models

# Naive model:
fcast1 <- naive(timedata.ts, h=3)
summary(fcast1)
autoplot(fcast1, ts.colour = 'violetred4') + 
  labs(x ="Year", y = "$ in Billion", title = "Naive Model")

# Seasonal Naive model:
fcast2 <- snaive(timedata.ts, h=3)
summary(fcast2)
autoplot(fcast2, ts.colour = 'violetred4', 
         predict.linetype = 'dashed') + 
  labs(x ="Year", y = "$ in Billion", title = "Seasonal Naive Model")

# Random Walk Forecast
fcast3 <- rwf(timedata.ts, h=3, drift = TRUE)
summary(fcast3)
autoplot(fcast3)
          
