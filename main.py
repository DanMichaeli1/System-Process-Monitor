from processList import ProcessList
#import logsWatcher

__author__ = 'Dan'

interval = float(raw_input("Please input log update interval (in seconds): "))
p = ProcessList(interval)
p.write_log()
