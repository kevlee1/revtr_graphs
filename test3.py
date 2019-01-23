import matplotlib.pyplot as plt

# x axis values
X = [1, 2, 3, 4, 5, 6]
# y axis values
Y = [2, 4, 1, 5, 2, 6]

# plotting the points
plt.plot(X, Y, color='green', linestyle='dashed', linewidth=3, marker='o',
         markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(1, 8)
plt.xlim(1, 8)

# name the x axis
plt.xlabel('x-axis')
# name the y axis
plt.ylabel('y-axis')

# graph's title
plt.title('customized graphs Pog')

plt.show()
