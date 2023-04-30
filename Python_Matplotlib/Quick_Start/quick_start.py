from matplotlib import pyplot as plt

# Size of the X axis
X_AXIS_SIZE = 5

# Declare the X axis.
x_axis      = [i for i in range(0, X_AXIS_SIZE, 1)]

# Declare the Y axis.
linear      = x_axis
quadratic   = [i**2 for i in x_axis]
cubic       = [i**3 for i in x_axis]

# Add some beautiful style. The whoe list of built-in styles can be seen in console by using the following statement:
# print(plt.style.available)
plt.style.use("Solarize_Light2")
# It should be done ASAP, otherwise, only the features after the call to "plt.style.use" will be shown in the chosen style.

# Figure object is the outermost container for a matplot graphic.
# Axes refers to every individual plot within the figure.
fig, ax = plt.subplots()

# Create each graph. Bear in mind that ax is an object which stands for each target graph.
# First argument is the X axis used as reference, second is the Y axis function, third (optional) is the format string.
# Arguments used as plt-legend input parameters might be used as well, although is way more readable if they are used
# within that function instead of the one below.
ax.plot(x_axis, linear   ,  ".-b")
ax.plot(x_axis, quadratic,  "X--r")
ax.plot(x_axis, cubic    ,  "o-.g")

# Add X and Y axis labels, as well as a title for the graph.
plt.xlabel("Numbers")
plt.ylabel("Linear, quadratic and cubic")
plt.title("Number progression")

# Add a legend, for the viewer to know what's what. It will label each variable in the y axis in plot order.
plt.legend(["linear", "quadratic", "cubic"])

# Add a grid, so values may be easier to retrieve visually.
plt.grid(True)

# Set margins to the plot. x and y arguments stand for the relative margins. For example, x=0.1 stands for a 10% margin.
# There is a margin by default on either axes, but it may be needed to modify it by ourselves.
plt.margins(x=0.1, y=0.1)

# Store the graph somewhere. Remember that "fig" is the object that contains the whole plot data, so use fig's method.
# On top of that, keep in mind that the path of the file will be the one where the script is executed into.
fig.savefig("my_first_plt.jpg")

# Show the plot on screen!
plt.show()
