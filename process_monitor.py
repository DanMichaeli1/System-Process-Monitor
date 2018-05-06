import time

__author__ = 'Dan'

from processList import ProcessList
from manualMode import compare_two_samples_by_time


# interval = float(raw_input("Please input log update interval (in seconds): "))


# compare_two_samples_by_time(p.get_log(), "2018-05-01 16:35:31", "2018-05-01 16:35:43")
def monitor_mode(processlist):
    print '--Stop monitor mode at any time with CTRL-C.'
    processlist.set_interval(float(raw_input('Logs update interval (seconds):')))
    processlist.write_log()


def manual_mode(processlist):
    print 'Scan for two samples and compare them:\n'
    correctformat = False
    while not correctformat:
        time1 = raw_input('Enter time for sample 1 (YYYY-MM-DD HH:MM:SS):')
        time2 = raw_input('Enter time for sample 2 (YYYY-MM-DD HH:MM:SS):')
        try:
            time.strptime(time1, '%Y-%m-%d %H:%M:%S')
            time.strptime(time2, '%Y-%m-%d %H:%M:%S')
            correctformat = True
        except ValueError:
            correctformat = False
            print("Incorrect date format")
    compare_two_samples_by_time(processlist.get_log(), time1, time2)


def change_logs_folder(processlist):
    p.set_log_folder(raw_input('Select logs folder:'))


def change_interval(p):
    p.set_interval(float(raw_input('Logs update interval (seconds):')))


def exit_program():
    print 'Exiting.'
    exit(0)


if __name__ == '__main__':
    print '-------------------- Process Monitor --------------------\n'
    logfolder = raw_input('Select log folder:')
    print '\n'
    p = ProcessList(logfolder, 5)
    while True:
        userinput = float(
            raw_input('\nTo select a function, input the corresponding number:\nMonitor mode(1)\nManual mode('
                      '2)\nChange logs folder(3)\nExit(5)\n'))

        if userinput == 1:
            monitor_mode(p)
        elif userinput == 2:
            manual_mode(p)
        elif userinput == 3:
            change_logs_folder(p)
        elif userinput == 5:
            exit_program()
        else:
            print 'incorrect input!'
