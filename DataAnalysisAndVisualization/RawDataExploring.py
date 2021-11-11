import DataProcessing.MineralHandling as min

def CheckCommodityMissings(mineral: min.MineralData) -> None:
    """Understanding missing values with this function drives corrections to commodity"""
    df = mineral.mineral_data

    print('Total Length')
    print(len(df))

    print('Number of each missing commodity')
    print(df[['commod1','commod2','commod3']].isnull().sum())

    print("Number of missing commod1 but either 2 or 3 isn't missing")
    print(len(df.loc[(df['commod1'].isnull()) & ((df['commod2'].notnull()) | (df['commod3'].notnull()))]))

    print('Number of all missing commodities')
    print(len(df.loc[(df['commod1'].isnull()) & (df['commod2'].isnull()) & (df['commod3'].isnull())]))