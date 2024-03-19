import pandas as pd

from datetime import date
from datetime import timedelta

# Create dataframe
# Set the max number of rows
pd.options.display.max_rows = 9999

# Create dataframe from csv, set first column as the index
df = pd.read_csv('csv/support_requests_mar24.csv', index_col='Request Type')

#print (f'dataframe = {df}')

#sr = pd.DataFrame(df)       #convert series into a Dataframe - attempt to fix 'No axis named 2024-03-12 for object type dataframe' error
                            #print(df.columns.values) returns columns labelled with '2024-03-12' etc (for whole month)


# Define yesterdays date
today = date.today()
yesterday = today - timedelta(days = 1)

st_yesterday = str(yesterday)

#print(st_yesterday)

#print (f'Yesterdays date = {yesterday}')

#print(df[['2024-03-11']])

output = df[st_yesterday].sum()

print(f'Yesterday we recieved {output} Support Requests')

#print(yesterday)        # = 2024-03-11


#df.groupby([yesterday]).sum()

#st_yesterday = str(yesterday)

#print(df.columns.values)    #shows all columns as '2024-03-01'.. etc

#output = df.sum(st_yesterday)


# Print Dataframe

#print(df.info())


#df.groupby([yesterday])

#df = df.sum(axis=yesterday)
#print (f'Yesterdays support requests = {df}')

# sum rows by column
#df = df.sum(axis=1)

# Show dataframe
#print(df.to_string())