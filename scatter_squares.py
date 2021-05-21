# Using the scatter()
import matplotlib.pyplot as plt

'''
X_values are a list between 1 and 1000(off by 1) and Y_values are each 
x in x_values squared.
'''

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# S = set the size of the dot.
plt.scatter(x_values, y_values, edgecolor = 'none', s = 40)

# Set chart title and label axes.
plt.title('Square Numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize = 14)

# Set size of tick labels.
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the range for each axis.
'''
Axis() has 4 values the min and max for each the x_values and the 
y_values.
'''

plt.axis([0, 1100, 0, 1100000])

plt.show()

