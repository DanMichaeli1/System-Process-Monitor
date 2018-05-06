__author__ = 'Dan'

import time
from datetime import datetime


def fill_process_arr(processes_array, data, index):
    for line in data[index:]:
        if line == "-" * 80:
            break
        processes_array.append(line)
    enumerate(processes_array)


def compare_two_samples_by_time(processList, time1, time2, time_variance=0):
    time1_datetime = datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    time2_datetime = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    processesTime1 = []
    processesTime2 = []
    sampletime1 = ''
    sampletime2 = ''
    with open(processList + "\\processList.txt", 'r') as myfile:
        data = myfile.read().splitlines()
        lasttimeline = 0
        for linenum, line in enumerate(data):
            try:#2018-05-03 15:06:14
                time.strptime(line, '%Y-%m-%d %H:%M:%S')
                linetime = datetime.strptime(line, '%Y-%m-%d %H:%M:%S')
                lasttimeline = linenum
                if linetime == time1_datetime or (linetime > time1_datetime and len(processesTime1) == 0):
                    sampletime1 = line
                    fill_process_arr(processesTime1, data, linenum + 2)
                if linetime == time2_datetime or (linetime > time2_datetime and len(processesTime2) == 0):
                    sampletime2 = line
                    fill_process_arr(processesTime2, data, linenum + 2)
            except ValueError:
                pass
        if not processesTime2:
            sampletime2 = data[lasttimeline]
            fill_process_arr(processesTime2, data, lasttimeline + 2)
    stopped_process_list = [p for p in processesTime1 if p not in processesTime2]
    new_process_list = [p for p in processesTime2 if p not in processesTime1]

    if new_process_list:
        print '-----------------------Started processes-----------------------\n'
        print '------------------Sample ' + str(sampletime2) + '-------------------\n'
        for line in new_process_list:
            print(line + '\n')
    if stopped_process_list:
        print '-----------------------Stopped processes-----------------------\n'
        print'------------------Sample ' + str(sampletime1) + '-------------------\n'
        for line in stopped_process_list:
            print(line + '\n')
    if not new_process_list and not stopped_process_list:
        print 'No changes between samples!'
