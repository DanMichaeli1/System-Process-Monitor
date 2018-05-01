__author__ = 'Dan'

import time
from datetime import datetime

def fill_process_arr(processes_array, data, index):
    for line in data[index:]:
        if line == "-" * 80:
            break
        processes_array.append(line)
    enumerate(processes_array)
    return len(processes_array)



def compare_two_samples_by_time(processList, time1, time2, time_variance = 0):
    processesTime1 = []
    processesTime2 = []
    line_index = 0
    with open(processList + "\\processList.txt", 'r') as myfile:
        data = myfile.read().splitlines()
        for linenum, line in enumerate(data[line_index:]):
            if line == time1:
               line_index = fill_process_arr(processesTime1, data, linenum+2)
            if line == time2:
                fill_process_arr(processesTime2, data, linenum)



