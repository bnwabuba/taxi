#!/usr/bin/env python
# coding: utf-8

# Problem Statement:
# You've been tasked with analyzing data from the "Taxis" table, which contains information about taxi rides including pickup and dropoff locations, number of passengers, distance traveled, fare, tips, tolls, total payment, and various categorical attributes such as color, payment method, and zones. Your goal is to extract insights from this data to help improve taxi services and optimize operations by answering the following questions:
# 
# 
# 1. What is the distribution of the number of passengers per ride?
# 2. How does the fare vary with distance traveled?
# 3. Is there a correlation between the total payment and the number of passengers?
# 4. Which payment method is the most common?
# 5. How does the distribution of fares differ between different boroughs?
# 6. What is the relationship between tip amount and total payment?

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#getting the dataset from seaborn library
sns.load_dataset('taxis').head()


# In[3]:


taxis_data = sns.load_dataset('taxis')


# In[6]:


#check for missing values in the dataset 
taxis_data.isnull().sum()


# In[7]:


taxis_data_dropna_any = taxis_data.dropna()
taxis_data.dropna(subset=["payment", "pickup_zone", "dropoff_zone", "pickup_borough", "dropoff_borough"], inplace=True)


# In[8]:


taxis_data.isnull().sum()


# In[9]:


print(taxis_data.info())  # to get summary information about the columns and data types
print(taxis_data.describe())


# In[10]:


#to show records per passengers
print(taxis_data.groupby(['passengers'])[['passengers', 'fare']].count())


# In[11]:


#Question number 1 - What is the distribution of the number of passengers per ride?
# Univariate plot of the distribution of Number of Passengers per Ride
plt.figure(figsize=(8, 6))
sns.histplot(taxis_data['passengers'], bins=range(0, 7), kde=True)
plt.title('Distribution of Number of Passengers per Ride')
plt.xlabel('Number of Passengers')
plt.ylabel('Frequency')
plt.show()


# Right-Skewed Histogram (mean number of passengers per ride is greater than the median) 
# Frequency = number of passengers in that range. This shows that most of the rides have only one passenger.
# The mode number of passengers = 1

# In[12]:


# Question number 2: How does the fare vary with distance traveled? 
# Bivariate plot of the fare vs. Distance Traveled
plt.figure(figsize=(8, 6))
sns.scatterplot(x='distance', y='fare', data=taxis_data, label='Data')
sns.regplot(x='distance', y='fare', data=taxis_data, scatter=False, color='red', label='Trend Line')
plt.title('Fare vs. Distance Traveled')
plt.xlabel('Distance (miles)')
plt.ylabel('Fare ($)')
plt.legend(loc="lower right")

# to calculate correlation coefficient
correlation_coefficient = taxis_data['distance'].corr(taxis_data['fare'])
plt.tight_layout
plt.text(0.1, 0.9, f'Correlation Coefficient: {correlation_coefficient:.2f}', transform=plt.gca().transAxes)

plt.show()


# The correlation coefficient = 0.95 i.e the higher the distance traveled, the higher the fare.

# In[13]:


# Question number 3: Is there a correlation between the total payment and the number of passengers?
# Bivariate plot of the total Payment by Number of Passengers
plt.figure(figsize=(8, 6))
sns.barplot(x='passengers', y='total', data=taxis_data, estimator=sum)
plt.title('Total Payment by Number of Passengers')
plt.xlabel('Number of Passengers')
plt.ylabel('Total Payment ($)')
plt.show()


# In[14]:


#to show payment per passengers
print(taxis_data.groupby(['passengers'])[['passengers', 'total']].sum())


# The barplot above shows the number of passengers in categories (1,2,3,4,5,6) and the total amount they spent. Rides with only 1 passenger made the most amount of payment $83872.75 followed by rides with 2 passengers: $16042.10

# In[15]:


# Question number 4: Which payment method is the most common?
# Univariate plot of the distribution of Payment Methods
plt.figure(figsize=(8, 6))
sns.countplot(x='payment', data=taxis_data)
plt.title('Distribution of Payment Methods')
plt.xlabel('Payment Method')
plt.ylabel('Frequency')
plt.show()


# The above visual shows that credit card is the most used mode of payment. Even though cash is used as a mode of payment almost 2000 times, credit card still tops the chart by over 100%.

# In[16]:


# Question number 5: How does the distribution of fares differ between different boroughs?
# Bivariate plot of the distribution of Fares by Pickup Borough
plt.figure(figsize=(10, 6))
sns.violinplot(x='pickup_borough', y='fare', data=taxis_data)
plt.title('Distribution of Fares by Pickup Borough')
plt.xlabel('Borough')
plt.ylabel('Fare ($)')
plt.xticks(rotation=45)
plt.show()


# The violinplot above shows the distribution of fares by borough (Manhattan, Queens, Bronx and Brooklyn). The breadth determines the frequency of that range of payment. 
# 
# Manhattan: the range of payment is between  $5 𝑎𝑛𝑑 $25 with a rare occurence of  $75 − $125 
# Queens: the range of payment is between  $5 𝑎𝑛𝑑 $60 with a rare occurence of  $100 − $125 
# Bronx: the range of payment is between  $12 𝑎𝑛𝑑 $60 with a rare occurence of  $80 − $90 
# Brooklyn: the range of payment is between  $5 𝑎𝑛𝑑 $20 with a rare occurence of  $75 − $110

# In[21]:


# Question number 6: What is the relationship between tip amount and total payment?
#Multivariate plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='tip', y='total', data=taxis_data)
plt.title('Total Payment vs. Tip Amount')
plt.xlabel('Tip Amount ($)')
plt.ylabel('Total Payment ($)')

correlation_coefficient = taxis_data['tip'].corr(taxis_data['total'])
plt.legend(loc="upper right")
plt.text(0.1, 0.95, f'Correlation Coefficient: {correlation_coefficient:.2f}', transform=plt.gca().transAxes)
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")
plt.show()


# The correlation coefficient = 0.65 This is not a strong correlation so there's a possibility that the higher the total payment, the higher the tip

# In[23]:


# Univariate plot of the histogram of fare amount
plt.figure(figsize=(8, 6))
plt.hist(taxis_data['fare'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Fare Amount')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.show()


# In[24]:


# Multivariate Plot of Fare vs. Distance Traveled with Passenger Count as Hue
plt.figure(figsize=(10, 8))
sns.scatterplot(x='distance', y='fare', hue='passengers', data=taxis_data)
plt.title('Fare vs. Distance Traveled (Passenger Count)')
plt.xlabel('Distance (miles)')
plt.ylabel('Fare ($)')
plt.legend(title='Passengers')
plt.show()


# The above scatterplot shows that rides with a single passenger had the highest distance in miles compared to rides with other number of passengers

# In[25]:


# Multivariate Plot of the Total Payment by Number of Passengers and Payment Method
plt.figure(figsize=(10, 8))
sns.boxplot(x='passengers', y='total', hue='payment', data=taxis_data)
plt.title('Total Payment by Number of Passengers and Payment Method')
plt.xlabel('Number of Passengers')
plt.ylabel('Total Payment ($)')
plt.legend(title='Payment Method')
plt.show()


# In[26]:


# Multivariate Plot of the Fare vs. Tip by Payment Method
plt.figure(figsize=(10, 8))
sns.scatterplot(x='fare', y='tip', hue='payment', data=taxis_data)
plt.title('Fare vs. Tip by Payment Method')
plt.xlabel('Fare ($)')
plt.ylabel('Tip ($)')
plt.legend(title='Payment Method')
plt.show()


# In[30]:


# to sort the DataFrame by the 'tips' column in descending order
top_10_tips = taxis_data.sort_values(by='tip', ascending=False).head(10)

# Print the top 10 tips
print(top_10_tips[['fare', 'distance', 'tip']])


# The above code and visual shows that most riders were tipped with credit cards and the highest tip received was $23.19 from a ride whose distance was 26.92 miles

# In[31]:


# Multivariate Plot of the Total Payment vs. Distance Traveled by Pickup Borough
plt.figure(figsize=(10, 8))
sns.scatterplot(x='distance', y='total', hue='pickup_borough', data=taxis_data)
plt.title('Total Payment vs. Distance Traveled by Pickup Borough')
plt.xlabel('Distance (miles)')
plt.ylabel('Total Payment ($)')
plt.legend(title='Pickup Borough')
plt.show()


# Proferred recommendations for the taxi business to help improve taxi services and optimize operations:
# 
# 1. Optimize Operations for Single Passenger Rides:
# Since most rides have only one passenger and they contribute significantly to the total payments, prioritize optimizing operations to cater to this segment. Offering discounts or promotions for single passenger rides during off-peak hours could attract more customers and increase revenue.
# 
# 2. Distance-Based Fare Pricing:
# Given the high correlation coefficient of 0.95 between distance traveled and fare amount, implement a distance-based fare pricing strategy. This can help ensure that customers are charged fairly based on the distance of their rides, which aligns with the observed trend in the dataset.
# 
# 3. Payment Method Promotion:
# Although cash is commonly used as a payment method, credit card payments are more frequent and contribute significantly to the total payments. To further incentivize credit card payments, consider offering rewards or discounts for customers who choose this payment method. Additionally, ensure that payment processing systems are reliable and user-friendly to encourage more customers to use credit cards.
# 
# 4. Location-Specific Pricing Strategies:
# Implement location-specific pricing strategies based on the payment range and rare occurrence observations for different pickup/dropoff locations. This can involve adjusting fare rates or offering targeted promotions to attract more customers from specific areas.
# 
# 5. Encourage Tipping Culture:
# With a correlation coefficient of 0.65 between total payment and tip amount, it is evident that tips contribute to the total revenue of taxi drivers. Encourage tipping culture among customers by providing excellent customer service, maintaining clean and comfortable vehicles, and offering incentives for customers who tip generously.
# 
# 6. Efficient Single Passenger Ride Allocation:
# Since rides with a single passenger have the highest distance traveled compared to rides with other numbers of passengers, optimize the allocation of single passenger rides to drivers to maximize efficiency. This can involve using data-driven algorithms to match single passengers with available drivers efficiently, reducing wait times and increasing customer satisfaction.
# 
# 7. Track and Reward High-Tip Rides:
# Identify and track rides where customers provide high tips, such as the ride with a $23.19 tip for a 26.92-mile distance. Reward drivers who consistently receive high tips with incentives or bonuses to incentivize excellent service and encourage repeat business.
