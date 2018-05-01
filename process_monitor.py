from processList import ProcessList
from manualMode import compare_two_samples_by_time

__author__ = 'Dan'

#interval = float(raw_input("Please input log update interval (in seconds): "))
p = ProcessList(5)
#p.write_log()

compare_two_samples_by_time(p.get_log(), "2018-05-01 13:28:45", "2018-05-01 13:28:51")
