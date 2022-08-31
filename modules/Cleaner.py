import pandas as pd
from support_files import decorators

errordecorator = decorators.catchErrors((KeyError, NameError), default_value='default')


class Cleaner:

    def __init__(self, df):
        self.columns_to_drop = []
        self.rows_to_drop = []
        self.duplicates = None
        self.rows_to_skip = []
        self.df = df
        return

    @errordecorator
    def setColumnsToDrop(self, columns_to_drop):
        self.columns_to_drop = columns_to_drop
        return

    @errordecorator
    def removeColumns(self):
        self.df.drop(columns=self.columns_to_drop, inplace=True)
        return self.df

    @errordecorator
    def setRowsToDrop(self, rows_to_drop):
        self.rows_to_drop = rows_to_drop
        return

    @errordecorator
    def removeRows(self):
        self.df.drop(index=self.rows_to_drop, inplace=True)
        return self.df




