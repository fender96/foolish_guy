import pandas as pd
from support_files import decorators

errordecorator = decorators.catchErrors((KeyError, NameError), default_value='default')

class Importer:

    def __init__(self):
        self.input_data_path = ''
        self.output_data_path = ''
        self.dataframestats = ''

    @errordecorator
    def setInputFilePath(self, input_path):
        self.input_data_path = input_path
        return
    @errordecorator
    def readCsv(self):
        raw_data = pd.read_csv(self.input_data_path)
        return raw_data
    @errordecorator
    def raw2dataframe(self, raw_data):
        raw_data_df = pd.DataFrame(raw_data)
        return raw_data_df
    @errordecorator
    def dataframeStatistics(self, raw_data_df):
        self.dataframestats = raw_data_df.describe()
        return
