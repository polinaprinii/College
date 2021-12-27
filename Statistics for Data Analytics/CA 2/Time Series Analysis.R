# Importing Libraries:
library(ggplot2)
library(fpp2)
library(tsbox)
library(forecast)

# Importing the eComm_US.csv file into RStudio.
timedata = read.csv("/Users/polinaprinii/Documents/Statistics/eComm_US.csv",
                    header = TRUE, stringsAsFactors = FALSE)

# Now we check the class and structure of our time data variable.
class(timedata)
str(timedata)

# Converting DATE column from chr to date.
timedata$DATE <- as.Date(timedata$DATE)

# Checking structure of DATE column.
str(timedata$DATE)
# Checking structure of the whole data frame once again.
str(timedata)

# Converting the data frame to a ts object.
timedata.ts <- ts_ts(ts_long(timedata))

# Below initial understanging on how to read a df as a ts, which was incorrect.
#timedata.ts = ts(data=timedata['ECOMNSA'], frequency = 4, start = c(1999, 4))

# Checking class and structure of the timedata.ts variable.
class(timedata.ts)
str(timedata.ts)
head(timedata.ts)

# Checking the start and end of the time series.
start(timedata.ts)
end(timedata.ts)

# Checking the frequency.
frequency(timedata.ts)

# Printing first 3 rows of the time series.
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
autoplot(fcast3, ts.colour = 'orchid4',) +
  labs(x ="Year", y = "$ in Billion",
       title = "Random Walk Forest - Naive Model")

# Exponential smoothing, both additive and multiplicative.
ts <- window(timedata.ts, start = c(1999, 4), end = c(2021, 2))
hw1 <- hw(ts, h = 3, seasonal = c("additive"))
summary(hw1)
autoplot(hw1)

hw2 <- hw(ts, h = 3, seasonal = c("multiplicative"))
summary(hw2)
checkresiduals(hw2)
autoplot(hw2)

# Plotting the Holt-Winters Models.
autoplot(ts,) +
  autolayer(hw1, series = "Additive") +
  autolayer(hw2, series = "Multiplicative") +
  xlab("Year") +
  ylab("$ in Billions") +
  ggtitle("Holt-Winters eComm Forecasts") +
  guides(colour = guide_legend(title = "Forecasts"))

# Applying the ets function to confirm the fit of the Holt-Winters model.
autofit <- ets(timedata.ts, model = "ZZZ")
summary(autofit)
checkresiduals(autofit)
autoplot(autofit)

autofit %>% forecast(h=3) %>%
  autoplot() +
  ylab("$ Retail Sales (billions)") +
  xlab("Year")

# Applying an ARIMA Model to a seasonal time series.
# First we plot the time series.
plot(timedata.ts)

# Second we check the order of differencing required.
ndiffs(timedata.ts)

# Read the ACF and PACF for the time series.
acf(timedata.ts)
Pacf(timedata.ts)

# Third we plot the differenced time series.
dtimeseries <- diff(timedata.ts, lag = 2, differences = 1)
autoplot(dtimeseries, 
         main = "eComm_US Time Series - Differecing (lag=2, differences=1)")

# Read the ACF and PACF of the difference time series.
acf(dtimeseries)
Pacf(dtimeseries)
checkresiduals(dtimeseries)
