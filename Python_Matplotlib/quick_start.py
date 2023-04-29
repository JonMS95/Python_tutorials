import matplotlib.pyplot as plt
from random import randint

X_AXIS_SIZE = 5

# Declare the X axis.
x_axis      = [i for i in range(0, X_AXIS_SIZE, 1)]

# Declare the Y axis.
linear      = x_axis
quadratic   = [i**2 for i in x_axis]
cubic       = [i**3 for i in x_axis]

# Figure object is the outermost container for a matplot graphic.
# Axes refers to every individual plot within the figure.
fig, ax = plt.subplots()

# Create each graph. Bear in mind that ax is an object which stands for each target graph.
ax.plot(x_axis, linear   )
ax.plot(x_axis, quadratic)
ax.plot(x_axis, cubic    )

# Add X and Y axis labels, as well as a title for the graph.
plt.xlabel("Numbers")
plt.ylabel("Linear, quadratic and cubic")
plt.title("Number progression")

# Add a legend, for the viewer to know what's what. It will label each variable in the y axis in plot order.
plt.legend(["linear", "quadratic", "cubic"])

plt.show()