from statusList import StatusList

__author__ = 'Dan'

# logFolderPath = 'C:\Users\Dan\Desktop\New Folder'

import os
import psutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class ProcessList:
    __log_folder_path = ""
    __interval = 0

    def __init__(self, interval):
        self.__log_folder_path = raw_input("log folder address: ").strip()
        self.__interval = interval
        self.status_list = StatusList(self.__log_folder_path)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    # processList.txt writing function
    def write_log(self):
        if not os.path.exists(self.__log_folder_path):
            os.mkdir(self.__log_folder_path)

        separator = "-" * 80
        format = "%30s %10s %s"
        format2 = "(%s) %30s, %10d, %s"
        while 1:
            procs_list = list(psutil.process_iter())
            procs_list = sorted(procs_list, key=lambda procList: procList.name)

            log_path = self.__log_folder_path + '\\processList.txt'
            with open(log_path, "a") as f:
                f.write(separator + "\n")
                f.write(time.ctime() + "\n")
                f.write(format % ("NAME", "PID", "PATH"))
                f.write("\n")

                for p in procs_list:
                    with p.oneshot():  # faster than pulling info from p a variable at a time

                        try:
                            exe = p.exe()
                            uname = p.username()
                        except:
                            exe = ""
                            uname = "-"
                            pass
                        f.write(format2 % (uname, p.name(), p.pid, exe))
                    f.write("\n\n")
            print "Finished log update!"
            event_handler = LoggingEventHandler()
            observer = Observer()
            observer.schedule(event_handler, path=self.__log_folder_path, recursive=False)
            observer.start()
            time.sleep(self.__interval)
            observer.stop()
            self.check_for_process_changes(procs_list)
            print "writing new log data!"


# checks for process changes in the system by creating a new process list and comparing it to procs (old list)
    def check_for_process_changes(self, procs):
        print "Checking for process changes..."
        new_procs_list = list(psutil.process_iter())  # creating a new processes list
        new_procs_list = sorted(new_procs_list, key=lambda proc: proc.name)
        s = set(new_procs_list)
        ''' if p is is procs(old list) and is not in s(newProcsList) then the process stopped in the interval time '''
        stopped_process_list = [p for p in procs if p not in s]
        new_process_list = [p for p in s if p not in procs]  # same logic as above but in reverse

        if len(new_process_list) > 0 or len(stopped_process_list) > 0:
            self.status_list.write_status_log(new_process_list, stopped_process_list)
