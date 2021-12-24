#Reading csv file
mydata <- read.csv("/Users/polinaprinii/Downloads/Credit_v2.csv")

summary(mydata)

attach(mydata)

#Plotting a box plot, to identify outliers.
boxplot(creddebt_transformed~age,data=mydata, main="Age Debt Data", 
        xlab="Age", ylab="Credit Debt by Age")

#Testing for linear relationships 
plot(age, creddebt_transformed, main="Linearity between Age of Credit Holders and Credit Debt", 
     xlab="Age of Credit Holders ",  ylab="Credit Debt Accumulated ", ylim=c(0,10000), pch=19)
abline(lm(creddebt_transformed~age), col="red")

# Basic Scatterplot Matrix
pairs(mydata)

pairs(~creddebt_transformed+age+employ+address+income_transformed+debtinc+othdebt_transformed,data=mydata,main="Linearity between the dependent var and the independent vars collectively")

#Applying a linear model to our data. 
c_lm <-lm(creddebt_transformed ~ income_transformed + debtinc + othdebt_transformed)

#Now we print the results of the linear regression.
summary(c_lm)

#(d) Use the plot () function to produce diagnostic plots of the linear regression fit.

plot(c_lm)

#Attaching new and transformed data to see if violations have been addressed.
mydata2 <- read.csv("/Users/polinaprinii/Documents/Statistics/Credit Debt SPSS.csv")
summary(mydata2)

attach(mydata2)

c_lm2 <-lm(LnCreddebt ~ LnIncome + debtinc + othdebt_transformed)
summary(c_lm2)

plot(c_lm2)
