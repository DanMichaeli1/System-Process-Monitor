__author__ = 'Dan'


from processList import ProcessList
from manualMode import compare_two_samples_by_time


#interval = float(raw_input("Please input log update interval (in seconds): "))
p = ProcessList(2)
p.write_log()

#compare_two_samples_by_time(p.get_log(), "2018-05-01 16:35:31", "2018-05-01 16:35:43")
