import matplotlib.pyplot as plt

x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds,
edgecolor='none', s=20)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()