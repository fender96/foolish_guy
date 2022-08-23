import pandas as pd
from support_files import decorators

errordecorator = decorators.catchErrors((KeyError, NameError), default_value='default')


def setInputFilePath(input_path):
    input_data_path = input_path
    return

class Importer:

    def __init__(self, input_data_path):
        self.input_data_path = input_data_path
        self.output_data_path = ''
        self.dataframestats = ''
        self.raw_data = None
        self.raw_data_df = None
        return

    @errordecorator

    @errordecorator
    def readCsv(self):
        self.raw_data = pd.read_csv(self.input_data_path)
        return self.raw_data
    @errordecorator
    def raw2dataframe(self):
        self.raw_data_df = pd.DataFrame(self.raw_data)
        return self.raw_data_df
    @errordecorator
    def dataframeStatistics(self):
        self.dataframestats = self.raw_data_df.describe()
        return self.dataframestats

