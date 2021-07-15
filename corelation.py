import pandas as pd
from pandas.core.frame import DataFrame
import plotly.express as pl
import numpy as np

import csv

days = []
marks = []

with open('daysData.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        days.append(float(row['days']))
        marks.append(float(row['marks']))

dataFrame = {'x':days,'y':marks}
corelation = np.corrcoef(dataFrame['x'],dataFrame['y'])

print(corelation[0,1])