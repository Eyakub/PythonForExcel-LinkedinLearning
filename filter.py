import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address',
              'City', 'State', 'Area Code', 'Income']

# get the location who lives in river side
# print(df.loc[df['City'] == 'Riverside'])
# print(df.loc[ (df['City'] == 'Riverside') & (df['First'] == 'Jhon')])

df['Tax %'] = df['Income'].apply(
    lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)

# total amount of tax
df['Taxes Owed'] = df['Income'] * df['Tax %']
# print(df['Taxes Owed'])

to_drop = ['Area Code', 'First', 'Address']
df.drop(columns=to_drop, inplace=True)
# print(df)

# False value
df['Test Col'] = False
df.loc[df['Income'] < 60000, 'Test Col'] = True
print(df.groupby(['Test Col']).mean().sort_values('Income'))