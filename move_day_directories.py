import os
import pandas as pd
from os import listdir
from os.path import isfile, join
import sys

day_int = float(sys.argv[1])
# print(next(os.walk('.'))[1])

dir_list = next(os.walk('.'))[1]
dir_string_starter = 'Day-'
list_of_dir_nums = []

for jj in range(len(dir_list)):
    temp_dir = dir_list[jj]
    if dir_string_starter in temp_dir:
        try: 
            temp_num = temp_dir.split('-',1)[1]
            list_of_dir_nums.append([float(temp_num),temp_num])
        except:
            print("Issue with ",temp_dir)



list_of_dir_nums_srt_rev = sorted(list_of_dir_nums,reverse=True)
max_val = list_of_dir_nums_srt_rev[0][0]

for jj in range(len(list_of_dir_nums_srt_rev)):
    if list_of_dir_nums_srt_rev[jj][0] > day_int:
        orig_name = "Day-"+list_of_dir_nums_srt_rev[jj][1]
        new_name = "Day-"+str(int(list_of_dir_nums_srt_rev[jj][0]+1))
        print(orig_name,new_name)
        os.system(f'mv {orig_name} {new_name}')
