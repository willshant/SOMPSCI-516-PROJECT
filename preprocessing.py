import datetime
import pandas as pd
import numpy as np

num_cols = 23


# Function that convert the 'HHMM' string to datetime.time
def format_heure(chaine):
    if pd.isnull(chaine):
        return np.nan
    else:
        if chaine == 2400: chaine = 0
        chaine = "{0:04d}".format(int(chaine))
        heure = datetime.time(int(chaine[0:2]), int(chaine[2:4]))
        return heure


infile_name = "../flights.csv"
outfile_name = "../cleaned_flights.csv"

df = pd.read_csv(infile_name, low_memory=False, usecols=range(0, num_cols))
df = df.dropna(subset=['DEPARTURE_DELAY', 'ARRIVAL_DELAY'])
for col in range(9, num_cols):
    df[df.columns[col]] = df[df.columns[col]].astype(int)

df['DATE'] = pd.to_datetime(df[['YEAR','MONTH', 'DAY']])
df.loc[:, 'DEPARTURE_TIME'] = df['DEPARTURE_TIME'].apply(format_heure)
df.loc[:, 'ARRIVAL_TIME'] = df['ARRIVAL_TIME'].apply(format_heure)
print(df.columns)

col_filter = [num_cols, 4, 7, 8, 17, 10, 11, 21, 22]
# col_filter = [num_cols] + list(range(3, num_cols))
cols = df.columns[col_filter]
print(cols)
df = df[cols]

df.to_csv(outfile_name, sep=',', index=False)
