# Importing the Pandas library
import pandas as pd
import random

# Load Dataset as Dataframe
dataset = pd.read_csv('./index.html')

# Show dataset
# head() bydefault show
dataset.head()

# Calculate the Mean
# of 'COLOURS' column
mean = dataset['COLOURS'].mean()
 
# Print mean
print(mean)

# Calculate Mode of 'COLOURS' column
# The colour that's mostly worn durint the week
mode = dataset['COLOURS'].mode()
 
# Print mode
print(mode)

# Calculate Median of 'COLOURS' column
median = dataset['COLOURS'].median()
 
# Print median
print(median)

# To calculate variance
print(dataset.var())

# To calculate probability of choosing red
def check_frequency():
    dataset = 0
for i in range(100):
    if random.random():
        dataset += 1
    print(dataset)
def simulate(n):
    trials = []
    for i in range(n):
        trials.append(check_frequency())
    return(sum(trials)/n)
simulate(dataset)

# To save the colours and frequencies in a table
dataset.describe()

# To generate random 4 numbers between 0 and 1
numbers = random.sample(range(1), 4)
print(''.join(map(str, numbers)))


# Write a program to sum the first 50 fibonacci sequence
x,y = 0,1

while y < 50:
    print(y)
    x,y = y,x+y