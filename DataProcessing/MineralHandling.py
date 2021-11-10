import pandas as pd

class MineralData(object):

    # This dataframe will be constantly modified throughout this object as an exercise in conserving memory
    mineral_data = pd.DataFrame()

    def __init__(self, address):
        self.mineral_data = pd.read_csv(address)
        print(self.mineral_data.head())

    def process_data(self):
        df = self.mineral_data

        # Break apart commodities into singular levels


