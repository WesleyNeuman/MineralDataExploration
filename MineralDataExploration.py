# External Modules
import pandas as pd
import numpy as np

# Internal Modules
import DataProcessing.MineralHandling as mineral
import DataAnalysisAndVisualization.RawDataExploring as explorer
import Misc.SettingsMethods as settings

# Initialize Environment
settings.PandasInit()

# Import and Explore Raw Data
mineral1 = mineral.MineralData(r"C:\Users\wesley.neuman\PycharmProjects\MineralDataExploration\RawData\Mineral ores round the world.csv")

mineral1.correct_commodity()
