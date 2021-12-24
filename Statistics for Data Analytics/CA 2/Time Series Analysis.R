# Importing the eComm_US.csv file into RStudio.
 
timedata = read.csv("/Users/polinaprinii/Documents/Database & Analytics Programming/eComm_US.csv",
                    header = TRUE, stringsAsFactors = FALSE)

# Now we check the class of our timedata variable.
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

# Plotting the timeseries.
plot(timedata.ts)
