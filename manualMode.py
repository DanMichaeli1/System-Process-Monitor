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
    date1 = time1[:10]
    date2 = time2[:10]
    hour1 = time1[11:]
    hour2 = time2[11:]
    processesTime1 = []
    processesTime2 = []
    with open(processList + "\\processList.txt", 'r') as myfile:
        data = myfile.read().splitlines()
        for linenum, line in enumerate(data):
            if line == time1:
                fill_process_arr(processesTime1, data, linenum+2)
            if line == time2:
                fill_process_arr(processesTime2, data, linenum+2)
       # if len(processesTime1) == 0:


    stopped_process_list = [p for p in processesTime1 if p not in processesTime2]
    new_process_list = [p for p in processesTime2 if p not in processesTime1]
    print 'Finished saving samples'




