import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('csv/support_requests_feb24.csv')

print(df.to_string())