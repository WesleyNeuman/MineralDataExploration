import pandas as pd
import numpy as np
import PandasWrappers as pw

class MineralData(object):

    # This dataframe will be constantly modified throughout this object as an exercise in conserving memory
    mineral_data = pd.DataFrame()

    def __init__(self, address):
        self.mineral_data = pd.read_csv(address, nrows=200)

    def correct_commodity(self):
        """I want to have a variable for each commodity showing what each location produces"""
        df = self.mineral_data

        # Break apart commodity columns
        df = pw.df_stringsplit(df, 'commod1', ',')
        df = pw.df_stringsplit(df, 'commod2', ',')
        df = pw.df_stringsplit(df, 'commod3', ',')

        newcols = df[list(set(df.columns.to_numpy()).difference(set(self.mineral_data.columns.to_numpy())))]
        unique_commods = []
        for i in range(0, len(newcols.columns)):
            s = newcols.iloc[:,i]
            s = s.loc[s.notnull()].unique().tolist()
            unique_commods = list(set().union(unique_commods, s))

        df = self.mineral_data
        print(newcols)
        for commodity in unique_commods:
            df[commodity] = False
            for column in newcols.columns:
                df['comparer'] = newcols[column].str.contains(commodity)
                df[commodity] = np.where(df['comparer'] == True, True, df[commodity])
        print(df.head())
