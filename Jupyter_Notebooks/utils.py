import numpy as np              # Data generation
import matplotlib.pyplot as plt # Plotting

def generateRandomArray(input_low: int = 0, input_high: int = 100, input_size: int = 10) -> np.ndarray:
    return np.random.randint(low = input_low, high = input_high, size = input_size)

def plot1DTimeSeries(data           : np.ndarray            ,
                     time_step      : float = 1.0           ,
                     title          : str   = "Time Series" ,
                     xlabel         : str   = "Time"        ,
                     ylabel         : str   = "Value"       ,
                     marker         : str   = 'o'           ,
                     margin_ratio   : float = 0.05          ) -> None:
    
    time = np.arange(len(data)) * time_step
    
    # Determine axis limits with margins
    y_min, y_max = np.min(data), np.max(data)
    y_margin = (y_max - y_min) * margin_ratio if y_max != y_min else 1
    x_min, x_max = time[0], time[-1]
    x_margin = (x_max - x_min) * margin_ratio if x_max != x_min else 1
    
    fig, ax = plt.subplots()
    ax.plot(time, data, marker=marker)
    ax.title(title)
    ax.xlabel(xlabel)
    ax.ylabel(ylabel)
    ax.xlim(x_min - x_margin, x_max + x_margin)
    ax.ylim(y_min - y_margin, y_max + y_margin)
    ax.grid(True)
    fig.show()