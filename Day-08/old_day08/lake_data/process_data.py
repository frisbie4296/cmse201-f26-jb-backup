import pandas as pd
import numpy as np

# read data frame (ignoring header)
df = pd.read_csv('GLHYD_data_metric.csv',delimiter=',',skiprows=11)

# set column names
df = df.rename(columns=df.iloc[0]).drop(df.index[0])

# extract water levels
sup = np.array(df['Superior'].values,dtype=float)
mh = np.array(df['Michigan-Huron'].values,dtype=float)
stc = np.array(df['St. Clair'].values,dtype=float)
erie = np.array(df['Erie'].values,dtype=float)
ont = np.array(df['Ontario'].values,dtype=float)

# create a numeric tag that encodes the data (month and year)
month_incr = [float(i)/12 for i in range(12)]
months = df['month'].values[0:12]  # just a list of the months (e.g. 'jan')
month_incr_dict = {}
for i in range(12):
    month_incr_dict[months[i]] = month_incr[i]

# converting the month, year info to a numeric date
date_num = np.array([month_incr_dict[df['month'].values[i]] + int(df['year'].values[i]) for i in range(len(df))])

# saving each dataset to a csv file
np.savetxt('lake_superior.csv',np.stack((date_num,sup)).T)
np.savetxt('lake_ontario.csv',np.stack((date_num,mh)).T)
np.savetxt('lake_stclair.csv',np.stack((date_num,stc)).T)
np.savetxt('lake_erie.csv',np.stack((date_num,erie)).T)
np.savetxt('lake_michigan_huron.csv',np.stack((date_num,ont)).T)

