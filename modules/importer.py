import pandas as pd
from support_files import decorators

errordecorator = decorators.catchErrors((KeyError, NameError), default_value='default')


class Importer:

    def __init__(self, input_data_path):
        self.input_data_path = input_data_path
        self.dataframestats = None
        self.raw_data = None
        self.raw_data_df = None
        return

    @errordecorator
    def readCsv(self):
        self.raw_data = pd.read_csv(self.input_data_path, header=1)
        return self.raw_data

    @errordecorator
    def raw2dataframe(self, df):
        self.raw_data_df = pd.DataFrame(df)
        return self.raw_data_df

    @errordecorator
    def dataframeStatistics(self):
        self.dataframestats = self.raw_data_df.describe()
        return self.dataframestats

