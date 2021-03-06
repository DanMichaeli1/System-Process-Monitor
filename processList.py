__author__ = 'Dan'


from statusList import StatusList
# logFolderPath = 'C:\Users\Dan\Desktop\New Folder'

import os
import psutil
import time
import logging
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class ProcessList:
    __log_folder_path = ""
    __interval = 0

    def __init__(self, logfolder, interval):
        self.__log_folder_path = 'C:\Users\USER\Desktop\Process logs' #raw_input("log folder address: ").strip()
        self.__interval = interval
        self.__sample_list = []
        self.status_list = StatusList(self.__log_folder_path)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def get_log(self):
        return self.__log_folder_path

    def set_log_folder(self, logfolder):
        self.__log_folder_path = logfolder

    def set_interval(self, interval):
        self.__interval = interval

    # processList.txt writing function
    def write_log(self):
        if not os.path.exists(self.__log_folder_path):
            os.mkdir(self.__log_folder_path)

        separator = "-" * 80
        format2 = "(%s), %30s, %10d, %s"
        try:
            while True:
                procs_list = list(psutil.process_iter())
                procs_list = sorted(procs_list, key=lambda procList: procList.name)

                log_path = self.__log_folder_path + '\\processList.txt'
                with open(log_path, "a") as f:
                    sample_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    self.__sample_list.append(sample_time)
                    f.write(sample_time + "\n")
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
                        f.write("\n")
                    f.write(separator + "\n")
                print "Finished log update!"
                event_handler = LoggingEventHandler()
                observer = Observer()
                observer.schedule(event_handler, path=self.__log_folder_path, recursive=False)
                observer.start()
                time.sleep(self.__interval)
                observer.stop()
                self.check_for_process_changes(procs_list)
                print "writing new log data!"
        except KeyboardInterrupt:
            print('Logging stopped!')



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
