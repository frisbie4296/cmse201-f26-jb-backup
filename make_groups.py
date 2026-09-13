#
# Makes random groups given a classlist ("CMSE201.csv") downloaded from the 
# registrar's page.
#

import pandas as pd
from numpy.random import shuffle

def reformat_name(name):
    arr = name.split(',')
    ln = arr[0]
    fn = arr[1].split(' ')[1]
    return f'{fn} {ln}'

df = pd.read_csv('CMSE201.csv')

names = df['Student_ID'].values
shuffle(names)

ngroups = 10

for i in range(ngroups):
    print(f'Group {i+1}')
    n = i
    while n < len(names):
        print(reformat_name(names[n]))
        n += ngroups
    print()
