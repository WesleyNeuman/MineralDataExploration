# External Modules
import pandas as pd
import numpy as np
import PandasWrappers as pw

# Internal Modules
import DataProcessing.MineralHandling as mineral
import DataAnalysisAndVisualization.RawDataExploring as explorer
import Misc.SettingsMethods as settings

# Initialize Environment
settings.PandasInit()

# Import and Explore Raw Data
mineral1 = mineral.MineralData(r"C:\Users\wesley.neuman\PycharmProjects\MineralDataExploration\RawData\Mineral ores round the world.csv")
print(mineral1.mineral_data.head())
pw.df_initialoverview(mineral1.mineral_data)

# Process data based on explorations
#mineral1.correct_commodity()
#mineral1.correct_ore()
#mineral1.correct_gangue()

# Exploring Processed Data
