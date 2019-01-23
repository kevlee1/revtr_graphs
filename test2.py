import matplotlib.pyplot as plt

# line 1 points
X1 = [1, 2, 3]
Y1 = [2, 4, 1]

# plotting the line 1 points
plt.plot(X1, Y1, label="line 1")

# line 2 points
X2 = [1, 2, 3]
Y2 = [4, 1, 3]

# plotting the line 2 points
plt.plot(X2, Y2, label="line 2")

# naming the x axis
plt.xlabel('x-axis')
# naming the y axis
plt.ylabel('y-axis')

# title for graph
plt.title('two lines Pog')

# show the legend on the plot
plt.legend()

# function to show the plot
plt.show()
