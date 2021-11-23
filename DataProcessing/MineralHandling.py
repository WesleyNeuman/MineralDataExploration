import sys

import pandas as pd
import numpy as np
import time
import WesleysPythonToolkit.PandasWrappers as pw

class MineralData(object):

    # This dataframe will be constantly modified throughout this object as an exercise in conserving memory
    mineral_data = pd.DataFrame()

    # I also want to save some intermediate parts of calculations for use later
    commodity_list = []
    ore_list = []
    gangue_list = []
    work_type_list = []

    def __init__(self, address):
        self.mineral_data = pd.read_csv(address)

    def correct_commodity(self):
        """Converts the commodity variables to a set of binary variables for each material"""
        df = self.mineral_data

        # Break apart commodity columns
        df = pw.df_stringsplit(df, 'commod1', ',')
        df = pw.df_stringsplit(df, 'commod2', ',')
        df = pw.df_stringsplit(df, 'commod3', ',')

        newcols = df[list(set(df.columns.to_numpy()).difference(set(self.mineral_data.columns.to_numpy())))]

        # Find all unique commodities
        unique_commods = []
        for i in range(0, len(newcols.columns)):
            s = newcols.iloc[:,i]
            s = s.loc[s.notnull()].unique().tolist()
            unique_commods = list(set().union(unique_commods, s))
        self.commodity_list = unique_commods

        # Refresh df to remove temporary commodity columns
        df = self.mineral_data
        for commodity in unique_commods:
            df[commodity] = np.where((df['commod1'].str.contains(commodity)) | (df['commod2'].str.contains(commodity)) | (df['commod3'].str.contains(commodity)), True, False)

        self.mineral_data = df.drop(columns=['commod1','commod2','commod3'])


    def correct_ore(self):
        """Converts ore to a set of variables for each group"""
        df = self.mineral_data

        df = pw.df_stringsplit(df, 'ore', ',')

        newcols = df[list(set(df.columns.to_numpy()).difference(set(self.mineral_data.columns.to_numpy())))]

        # Find Unique Ores
        unique_ores = []
        for i in range(0, len(newcols.columns)):
            s = newcols.iloc[:, i]
            s = s.loc[s.notnull()].unique().tolist()
            unique_ores = list(set().union(unique_ores, s))
        self.ore_list = unique_ores

        # Refresh df to remove temporary ore columns
        df = self.mineral_data
        for ore in unique_ores:
            df[ore] = np.where(df['ore'].str.contains(ore), True, False)

        self.mineral_data = df.drop(columns=['ore'])


    def correct_gangue(self):
        """Converts ore to a set of variables for each group"""
        df = self.mineral_data

        df = pw.df_stringsplit(df, 'gangue', ',')

        newcols = df[list(set(df.columns.to_numpy()).difference(set(self.mineral_data.columns.to_numpy())))]

        # Find Unique Ores
        unique_gangue = []
        for i in range(0, len(newcols.columns)):
            s = newcols.iloc[:, i]
            s = s.loc[s.notnull()].unique().tolist()
            unique_gangue = list(set().union(unique_gangue, s))
        self.gangue_list = unique_gangue

        # Refresh df to remove temporary ore columns
        df = self.mineral_data
        print(df)
        for gangue in unique_gangue:
            df[gangue] = np.where(df['gangue'].str.contains(gangue), True, False)

        self.mineral_data = df.drop(columns=['gangue'])


    def correct_worktype(self):
        """Converts work type to a set of variables for each group"""
        df = self.mineral_data

        # Break apart work_type
        df = pw.df_stringsplit(df, 'work_type', splitchar=r'[,/]')

        newcols = df[list(set(df.columns.to_numpy()).difference(set(self.mineral_data.columns.to_numpy())))]

        # Find all unique commodities
        unique_work_types = []
        for i in range(0, len(newcols.columns)):
            s = newcols.iloc[:, i]
            s = s.loc[s.notnull()].unique().tolist()
            unique_work_types = list(set().union(unique_work_types, s))
        self.work_type_list = unique_work_types

        # Refresh df to remove temporary commodity columns
        df = self.mineral_data
        for work_type in unique_work_types:
            df[work_type] = np.where(
                df['work_type'].str.contains(work_type), True, False)

        self.mineral_data = df.drop(columns=['work_type'])
