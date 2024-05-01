# Final Project Submission

Please fill out:
* Student name: HELLEN SAMUEL,Calvine Dasilver,Sandra kiptum ,Jack Otieno,Salahudin 
* Student pace: full time
* Scheduled project review date/time: 
* Instructor name: NIKITA




 # Demystifying House Sales Analysis with Regression Modeling in a Northwestern County

## Project Overview
Business Understanding
The real estate market is a vital component of regional economic health and stability. This project delves into the dynamics of house sales in a specific northwestern county in the United States, aiming to unravel the key factors influencing property valuation in this area.


## Problem Statements

<li> What are the most significant factors influencing house prices in this northwestern county?

<li> How can we quantify the relationship between these factors and property value?

<li> Can we develop a reliable model to predict house prices based on relevant characteristics?


## Challenges

1. Real estate data complexity, encompassing diverse property features and local market trends.
2. Accurately identifying and quantifying the impact of each factor on house prices.
3. Consideration of external factors like economic conditions and interest rates.

## Proposed Solutions

Utilizing multiple linear regression, a powerful machine learning technique, to analyze a large dataset of house sales and identify statistical relationships between property features and sale prices.

## Objectives

1. Develop a robust multiple linear regression model for accurate house price prediction.
2. Identify significant factors influencing property value in the specific market.
3. Provide insights into regional housing market dynamics.

## Research Questions

<li> How do bedrooms, bathrooms, grade, and square footage correlate with sale price in King County?
<li> What increase in home value can homeowners expect after specific renovation projects?
<li> Which renovation projects have the greatest impact on a home's market value?
<li> Are there specific combinations of renovation projects that provide an interdependent effect on home value?

## Data Understanding

**Dataset Description**

The analysis utilizes the King County House Sales dataset, comprising over 21,500 records and 20 distinct features. Spanning house sales from May 2014 to May 2015, the dataset offers a comprehensive snapshot of the housing market.

**Key Columns**

<li> id: Unique identifier for a house
<li> date: Date of house sale
<li> price: Sale price (prediction target)
<li> bedrooms, bathrooms, sqft_living, sqft_lot, floors, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, sqft_living15, sqft_lot15, sell_yr

**Constraints and Considerations**

<li> Data may contain anomalies or inconsistencies necessitating careful examination.
<li> Time frame (May 2014 - May 2015) may not fully reflect current market dynamics.
<li> Scope of data may not capture external factors such as interest rates or economic climate influencing property values.


**Data preparation**
we import the necessary functions and clean the data in the following ways

1. checking the data and null values
2. deleting the columns with null values
3. checking for non-numeric columns
4. checking for duplicates
5. creating the necessary columns
6. checking for outliers using the box plot and deleting the outliers

![alt text](image.png)


**Exploratory Data Analysis**

we will perform exploratory data analysis (EDA) to understand the data better and discover any patterns, trends using univariate,bivariate and multivariate analysis

We will use descriptive statistics and visualizations to summarize the main characteristics of the data and examine the relationships between the features and the target variable.

We will also check the distribution and correlation of the variables and identify any potential problems or opportunities for the analysis.

 # Univariate Analysis

Univariate analysis involves the examination of single variables.We focus in the summary statistics of target variable-price to help us undersatand the distribution and skewness of house prices.

 # Visualizing the distribution of 'price' using a histogram

 ![alt text](image-1.png)

 The histogram shows that the distribution of house price is positively skewed suggesting that while most houses are concentrated around lower prices, there are some properties with significantly higher prices.

  # Bivariate Analysis

We perform bivariate analysis to examine the relationship between the target variable - price and the other numeric and continuous features in the data using the scatter plots to show the direction, strength, and shape of the relationship between two numeric variables.

![alt text](image-3.png)

The scatter plots show that there is a positive relationship between most of the independent variables and the price of a house. This means that houses with higher values for these variables tend to be more expensive

 # Multivariate Analysis

 In this section, we will perform multivariate analysis to examine the relationship between the target variable - price and multiple features in the data. We will use heatmap to visualize the correlation matrix of the features and see how they are related to each other and to the price.

 ![alt text](image-4.png)

The heatmap shows that Positive correlations are typically represented by shades of red, and negative correlations by shades of blue. We note that bathrooms and sqft_living are highly positively correlated.


**Regression Modelling**
 # Simple Linear Regression

For simple linear regression we will use the one column that has the strongest correlation to the price, this will also be or baseline model for the multiple linear regression.

1. Checking for correlation

from the correlation sqft_living has the highest correlatio with price, we will therefore use sqft_living as the exogenous variable and price as our endogenous variable.
plot using a scatter plot


![alt text](image-5.png)

from this we can see that there is a linearity between the two variables satisfying one of the 4 LINE specifications.

2. building the model

we build the model qand interprate our models results

![alt text](image-6.png)

we are plotting our residuals to understand where our model is perfoming best and where it is performing poorly

![alt text](image-7.png)

our graphs give us the same information as our summary did
from this we can see that our residuals are not normally distributed we can solve this but using multiple linear distribution

 # Multiple Linear Regression

For Multiple Linear Regression, we are going to use more than one predictor variable to predict price for our case

Our baseline for this model will be the linear Regression that we just did above
We then clean our data 

![alt text](image-9.png)
The image above is a heatmap of the cleaned data
 
 # Building the model

1. we build the model,fit it and interprate the results

2. we check for normality

![alt text](image-10.png)

From the diagram above we can see that the errors are not normaly distributed and therefore we will check the other assumptions to evaluate

3. plotting the model

4. independence of errors
We are going to find out the predicted y of the model and calculate the residual from there on

![alt text](image-11.png)
This shows where our modle works best

5. evaluating the model
From this we can see that due to Outliers,Nonlinear Relationships,Heteroscedasticity and overfitting our MSE and RMSE are high, we will build another model to remidy this factors.

**RECOMENDATIONS**
From the 3 modules built we advise potential buyers or sellers to concider model 3 in determining the price of a house. We can also suggest that the factor affecting the price of a house most is square foot living but they should concider increasing the number of bathrooms during renovations for the case of the sellers.

**Next Steps**
1.Find more features that home buyers often value highly to add to the model
2.Correlate the information of this model with ones for other states
