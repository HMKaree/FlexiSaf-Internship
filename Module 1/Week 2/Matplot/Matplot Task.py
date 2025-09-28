#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data CSV file directly from the URL into a Pandas DataFrame.
url = "C:/Users/USER/OneDrive/Documents/FlexiSaf Internship/Week 1/Task 2/Matplot/company_sales_data.csv"
df = pd.read_csv(url)

# Exercise 1: Plot Total Profit of all months using a line plot.

# Create a new figure with a specified size for better visualization.
plt.figure(figsize=(10, 5))

# Plot 'total_profit' against 'month_number' using a line with circle markers.
plt.plot(df['month_number'], df['total_profit'], marker='o', linestyle='-', color='blue')

# Set the chart title and axis labels to explain what is plotted.
plt.title("Total Profit Over Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")

# Customize the x-axis to show each month number explicitly.
plt.xticks(df['month_number'])

# Add a grid to improve readability of the plot.
plt.grid(True)

# Display the plot on screen.
plt.show()

# Exercise 2: Create subplots for Bathing Soap and Facewash sales over the months.

# Initialize a figure with 2 vertically stacked subplots sharing the x-axis.
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# First subplot: Bathing Soap sales over time
axs[0].plot(df['month_number'], df['bathingsoap'], color='green', marker='o')
axs[0].set_title("Bathing Soap Sales Over Months")  # Title specific to this subplot
axs[0].set_ylabel("Units Sold")  # Y-axis label for quantity sold
axs[0].grid(True)  # Add gridlines for clarity

# Second subplot: Facewash sales over time
axs[1].plot(df['month_number'], df['facewash'], color='red', marker='o')
axs[1].set_title("Facewash Sales Over Months")  # Title for the second subplot
axs[1].set_xlabel("Month Number")  # X-axis label shared by both subplots
axs[1].set_ylabel("Units Sold")  # Y-axis label for quantity sold
axs[1].grid(True)  # Add gridlines for clarity

# Ensure month numbers appear as ticks on the x-axis for both subplots.
plt.xticks(df['month_number'])

# Automatically adjust subplot parameters for a cleaner layout.
plt.tight_layout()

# Display the figure with both subplots.
plt.show()


# In[ ]:





# In[ ]:




