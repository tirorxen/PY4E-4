import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
rand = np.random.random
from itertools import product
tuples = list(product(['Inadequate', 'Adequate', 'Confortable'], ['Convictions', 'No Convictions']))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
data = pd.Series(rand(6), index=index)
mosaic(data, title='mosaic plot')
plt.show()
