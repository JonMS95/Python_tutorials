'''
Bar charts and boxplots using Matplotlib's OO API.
'''

import matplotlib
matplotlib.use("TkAgg")  # Must be before pyplot
import matplotlib.pyplot as plt
import numpy as np

def barChart() -> None:
    # Let's start by adding values and category names.
    categories: list[str] = ["A", "B", "C", "D"]
    values:     list[int] = [23, 45, 12, 34]

    fig, ax = plt.subplots(figsize = (8, 4))

    ax.bar(categories       ,
           values           ,
           color = "teal"   )

    ax.set_title("Bar Chart: categorical comparison")
    ax.set_xlabel("Category")
    ax.set_ylabel("value")

    ax.grid(axis = "y") # Draws solely vertical reference lines.

    fig.tight_layout()
    # fig.savefig("bar_chart.png")
    plt.show()

def boxPlot() -> None:
    # Establish a seed so as to make the plot reproducible.
    np.random.seed(0)

    # Generate random data as Gaussian (normal) distributions. loc is for mean value, scale is for standard deviation and size is for number of data points.
    data_0: np.ndarray = np.random.normal(loc = 0   ,   scale = 1   ,   size = 200)
    data_1: np.ndarray = np.random.normal(loc = 1   ,   scale = 0.5 ,   size = 200)
    data_2: np.ndarray = np.random.normal(loc = -1  ,   scale = 1.5 ,   size = 200)

    random_dist_list: list[np.ndarray]  = [data_0, data_1, data_2]
    label_list      : list[str]         = ["Group 0", "Group 1", "Group 2"]

    fig, ax = plt.subplots(figsize = (8, 4))

    ax.boxplot(random_dist_list ,
               label_list       ,
               showmeans = True )
    
    ax.set_title("Boxplot: distribution summary")
    ax.set_ylabel("Value")
    ax.grid(axis = "y")

    fig.tight_layout()
    # fig.savefig("boxplot.png")
    plt.show()

def main():
    barChart()
    boxPlot()

if __name__ == "__main__":
    main()