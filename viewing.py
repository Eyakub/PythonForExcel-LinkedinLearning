import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Extra']

wanted_values = df[['First', 'Last', 'State']]
stored = wanted_values.to_excel('State_location.xlsx', index=None)
# print(df[['State', 'Area Code']])
# print(df['First'][0:3])
print(df.iloc[1])