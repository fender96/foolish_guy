import pandas as pd
import sys
from support_files import decorators

errordecorator = decorators.catchErrors((KeyError, NameError), default_value='default')


class Exporter:

    def __init__(self, output_data_path):
        self.cleaned_df_status = None
        self.output_data_path = output_data_path
        self.maximum_output_file_size = None
        self.output_data_format = None
        self.output_data_name = None
        return

    @errordecorator
    def setMaximumOutputSize(self, maximum_size):
        self.maximum_output_file_size = maximum_size
        return

    @errordecorator
    def checkMaximumOuputSise(self, df):
        dimension = sys.getsizeof(df)
        if dimension < self.maximum_output_file_size:
            print('Output file size within specification!')
            self.cleaned_df_status = True
        else:
            print('Output file size outside specification!')
            self.cleaned_df_status = False
        return

    @errordecorator
    def setOutputDataFormat(self, format):
        self.output_data_format = format
        return

    # @errordecorator
    # def writeOutputDataFormat(self):
    #     self.output_data_path = self.output_data_path + self.output_data_format
    #     return

    @errordecorator
    def exportFile(self, df):
        if self.output_data_name:
            df.to_csv(self.output_data_name, index=False)
        else:
            df.to_csv(self.output_data_path, index=False)
        return

    @errordecorator
    def appendOutputFileName(self, NametoAppend):
        self.output_data_name = self.output_data_path[:-4] + str(NametoAppend) + self.output_data_format
        return


