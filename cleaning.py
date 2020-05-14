import pandas as pd
import numpy as np
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

# getting rid of unnecessary column by to_drop
df.drop(columns='Address', inplace=True)

df = df.set_index('Area Code')
df.First = df.First.str.split(expand=True)

df = df.replace(np.nan, 'N/A', regex=True)

to_excel = df.to_excel('modified.xlsx')