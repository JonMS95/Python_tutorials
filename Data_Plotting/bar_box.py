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

def main():
    barChart()

if __name__ == "__main__":
    main()