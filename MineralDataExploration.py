# External Modules
import pandas as pd
import numpy as np
import WesleysPythonToolkit.PandasWrappers as pw

# Internal Modules
import DataProcessing.MineralHandling as mineral
import DataAnalysisAndVisualization.RawDataExploring as rExp
import DataAnalysisAndVisualization.ProcessedDataExploring as pExp
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
#mineral1.correct_worktype()

# Exploring Processed Data
pExp.play_with_graphs(mineral1.mineral_data)