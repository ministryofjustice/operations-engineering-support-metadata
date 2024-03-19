import pandas as pd

from datetime import date
from datetime import timedelta

# Create dataframe from csv and set max rows
df = pd.read_csv('csv/support_requests_mar24.csv')
pd.options.display.max_rows = 9999

# Set the index to Request Type column
df.set_index(['Request Type'])

# Define yesterdays date
today = date.today()
yesterday = today - timedelta(days=1)

# Convert date to string
str_yesterday = str(yesterday)

# Count requests in column that matches yesterdays date and print the result
total = df[str_yesterday].sum()
print(f'Yesterday we received {total} Support Requests')

# Create mask to remove NaN fields from 'str_yesterday' (none) and return Request Types and amount
notna_msk = df[str_yesterday].notna()
cols = ['Request Type', str_yesterday]
sr_types = df.loc[notna_msk, cols]

print(f'This is a breakdown of yesterdays Support Requests: \n {sr_types}')


# print(yesterday)        # = 2024-03-11


# df.groupby([yesterday]).sum()

# st_yesterday = str(yesterday)

# print(df.columns.values)    #shows all columns as '2024-03-01'.. etc

# output = df.sum(st_yesterday)


# Print Dataframe

# print(df.info())


# df.groupby([yesterday])

# df = df.sum(axis=yesterday)
# print (f'Yesterdays support requests = {df}')

# sum rows by column
# df = df.sum(axis=1)

# Show dataframe
# print(df.to_string())

# print (f'dataframe = {df}')

# sr = pd.DataFrame(df)       #convert series into a Dataframe - attempt to fix 'No axis named 2024-03-12 for object type dataframe' error
# print(df.columns.values) returns columns labelled with '2024-03-12' etc (for whole month)

# print(st_yesterday)

# print (f'Yesterdays date = {yesterday}')

# print(df[['2024-03-11']])

# for col in df.columns:
#    print(col)

# Print 2 columns to test working
# print(df[['Request Type',str_yesterday]].to_string(index=False))
