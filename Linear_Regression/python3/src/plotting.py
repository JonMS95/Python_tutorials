from data_logger import DataLogger
import pandas as pd
import numpy as np
from typing import Optional as opt
from matplotlib import pyplot as plt, axes as axs
from file_utils import savePlotAsPNG, checkXYColumns


_dlog               : DataLogger    = DataLogger()
_plot_default_name  : str           = "dummy_plot"


def plotLinePlot(df             : pd.DataFrame                                  ,
                 x_axis_label   : str           = "X"                           ,
                 y_axis_label   : str           = "Y"                           ,
                 intercept      : opt[float]    = None                          ,
                 slope          : opt[float]    = None                          ,
                 save_plot      : bool          = True                          ,
                 display_plot   : bool          = False                         ,
                 plot_name      : str           = (_plot_default_name + ".png") ) -> None:
    """
    Generate some random data for a linear function given a slope,
    an interceptor point and some additional parameters. 

    Args:
        df              : Input Pandas DataFrame object.
        intercept       : Intercept point (Y's value when X = 0).
        slope           : Line's slope.
        save_plot       : T/F either to save the generated plot as png file or not.
        display_plot    : T/F either to display the generated plot or not.
        plot_name       : Plot's name.
    """

    checkXYColumns(df)

    _dlog.logInf("Plotting data...")

    ax: axs = df.plot(  x = "X"                     ,
                        y = "Y"                     ,
                        kind = "scatter"            ,
                        title = plot_name           ,
                        grid = True                 ,
                        label = "Y"                 )

    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)
    ax.legend()

    if intercept is not None and slope is not None:
        # Line x coordinates.
        x_line = np.array([df["X"].min(), df["X"].max()])
        # Line y coordinates.
        y_line = intercept + slope * x_line

        # Make sure line stays within scatter y-limits.
        y_line = np.clip(y_line, df["Y"].min(), df["Y"].max())

        ax.plot(x_line, y_line, color="red", linestyle="-", label="Fit line")
        ax.legend()

    plt.tight_layout()

    if save_plot:
        savePlotAsPNG(ax.get_figure(), plot_name)
    
    if display_plot:
        plt.show()
