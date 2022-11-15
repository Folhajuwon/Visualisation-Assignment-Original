# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:09:42 2022

@author: sa22adl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing excel filefrom the URL
def generate_df(url):
    """ This method generates data frame from excel by passing a url"""
    data = pd.read_excel(url)
    return data

df = generate_df('Half Year 2021 data.xlsx')

#Bar Chart
#Importing bar chart 
#This Bar chart shows Y axis against X axis with Y-axis being States total tax for the half year and X-axis been the list of 36 states and FCT 
def plot_bar_chart(x_data,y_data,x_label,y_label,title):
    """ This method plots a bar chart by accepting 5 parameters"""
    plt.figure()
    plt.bar(x_data, y_data, label='Total Tax')
    plt.xlabel('STATES')
    plt.ylabel('TOTAL TAX')
    plt.title('Total tax against states')
    plt.xticks(rotation='vertical')
    plt.legend()
   # plt.show()
    
x_data = df['State']
y_data = df['Total Tax']
x_label = 'STATES'
y_label = 'TOTAL TAX'
title = 'TOTAL TAX AGAINST STATES'

#plot_bar_chart(x_data, y_data, x_label,y_label,title)


#line chart
#importing line plot
#This line plot shows the differences between the road tax, other taxes and total tax of all the 36 states and FCT
plt.figure()
plt.plot(df['State'], df['Road Tax'], label = 'Road Tax')
plt.plot(df['State'], df['Other Taxes'], label = 'Other Taxes')
plt.xlabel('STATES')
plt.ylabel('Road tax,Total tax and Other taxes')
plt.plot(df['State'], df['Total Tax'], label = 'Total Tax')
plt.title('Road tax,Total tax and Other taxes against states')
plt.xticks(rotation='vertical')
plt.legend()
#plt.show()

x_data = df['State']
x_label = 'STATES'
#y_label = 'Road tax,Total tax and Other taxes'
title = 'Road tax,Total tax and Other taxes against states'

#Pie Chart
#importing Pie chart
#This pie chart shows the differences between the total road tax and other taxes of all the 36 states and FCT
def plot_pie(data,label,explodes):
     """ plots a pie chart"""
     plt.figure()
     plt.pie(data, explode=explodes, labels=label, autopct='%1.3f%%', shadow=True, startangle=90)
     plt.show()
     
data = [df['Road Tax'].sum(), df['Other Taxes'].sum()]
explodes = [0, 0.1]
label = ['Road Tax', 'Other Taxes']

plot_pie(data,label,explodes) 

