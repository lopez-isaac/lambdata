""" lambdata - a collection of data science helper functions """

import numpy as np
import pandas as pd
import lambdata_lopez_isaac.class_example as ce
#sample code

#sample dataset
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(10))

#simple function


def increment(x):
    return(x + 1)
