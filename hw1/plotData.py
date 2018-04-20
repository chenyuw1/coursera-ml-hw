# import data

text_file = open('ex1data1.txt', 'r')
# data = [ text_file.readline() for i in range len(text_file.readlines()) ]
data = text_file.readlines()
data2 = []
with open ('ex1data1.txt') as file:
    for line in file:
        data2.append(line)
file.close

x = []
y = []
for item in data:
    x.append(item.split(',')[0])
    y.append(item.split(',')[1][0:-1])

# print (data2)
# print (x)
# print (y)

# scatter plot

import matplotlib.pyplot as plt
plt.scatter(x, y, marker='x', c='r')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
