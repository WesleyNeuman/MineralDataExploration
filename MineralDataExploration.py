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
print()
pw.df_initialoverview(mineral1.mineral_data)
print()

# Process data based on explorations
#mineral1.correct_commodity()
#mineral1.correct_ore()
#mineral1.correct_gangue()
print(mineral1.mineral_data['work_type'].unique())
mineral1.correct_worktype()
print(mineral1.mineral_data.head())

# Exploring Processed Data
