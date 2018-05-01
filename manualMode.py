__author__ = 'Dan'


def compare_two_samples_by_time(processList, time1, time2):
    processesTime1 = []
    processesTime2 = []
    with open(processList, 'r') as myfile:
        data = myfile.read().replace('\n', '')
    for line in data:
        if line == time1:
            fill_process_arr(processesTime1, data)


