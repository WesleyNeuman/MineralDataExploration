import sys

import pandas as pd
import numpy as np
import time
import PandasWrappers as pw

class MineralData(object):

    # This dataframe will be constantly modified throughout this object as an exercise in conserving memory
    mineral_data = pd.DataFrame()

    # I also want to save some intermediate parts of calculations for use later
    commodity_list = []

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
