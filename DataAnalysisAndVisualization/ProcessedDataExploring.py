import DataProcessing.MineralHandling as min

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def play_with_graphs(df: pd.DataFrame) -> None:
    """This function only contains graphs that I'm using to play around with matplotlib for learning"""

    # Plot Latitude and Longitude
    df.plot.scatter(x='longitude', y='latitude')
    plt.show()
