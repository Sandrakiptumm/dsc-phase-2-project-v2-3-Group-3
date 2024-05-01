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

Univariate Analysis

Univariate analysis involves the examination of single variables.We focus in the summary statistics of target variable-price to help us undersatand the distribution and skewness of house prices.

 # Visualizing the distribution of 'price' using a histogram

 ![alt text](image-1.png)

 The histogram shows that the distribution of house price is positively skewed suggesting that while most houses are concentrated around lower prices, there are some properties with significantly higher prices.

  # Bivariate Analysis

We perform bivariate analysis to examine the relationship between the target variable - price and the other numeric and continuous features in the data using the scatter plots to show the direction, strength, and shape of the relationship between two numeric variables.

![alt text](image-3.png)

The scatter plots show that there is a positive relationship between most of the independent variables and the price of a house. This means that houses with higher values for these variables tend to be more expensive



