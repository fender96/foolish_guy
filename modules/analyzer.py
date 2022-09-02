import sys

import pandas as pd
from support_files import decorators

errordecorator = decorators.catchErrors((KeyError, NameError), default_value='default')


class Analyzer:

    def __init__(self):
        self.reduction_factor = None
        return

    @errordecorator
    def calculateReductionFactor(self, original_df, final_df):
        original_dimension = sys.getsizeof(original_df)
        final_dimension = sys.getsizeof(final_df)
        self.reduction_factor = round((original_dimension - final_dimension) / original_dimension, 3) * 100
        return self.reduction_factor
