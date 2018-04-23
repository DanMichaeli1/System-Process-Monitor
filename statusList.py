__author__ = 'Dan'

import time
import datetime


class StatusList:

    def __init__(self, log_folder_path):
        self.__log_folder_path = log_folder_path

    # Status_Log.txt writing function
    def write_status_log(self, new_process_list, stopped_process_list):
        filename = self.__log_folder_path + '\\Status_Log.txt'
        separator = "-" * 80
        format = "%16s (%s) %30s, %10d %30s"
        format2 = "(%s) %30s, %10d %30s"
        with open(filename, "a") as f:
            f.write(separator + "\n")
            f.write(time.ctime() + "\n")
            f.write("New processes:\n")
            for p in new_process_list:
                start_time = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
                with p.oneshot():
                    try:
                        exe = p.exe()
                        uname = p.username()
                    except:
                        exe = ""
                        uname = "-"
                        pass
                    f.write(format % (start_time, uname, p.name(), p.pid, exe))
                f.write("\n")

            f.write("\n\nStopped processes:\n")
            for p in stopped_process_list:
                with p.oneshot():
                    try:
                        exe = p.exe()
                        uname = p.username()
                    except:
                        exe = ""
                        uname = "-"
                        pass
                    f.write(format2 % (uname, p.name(), p.pid, exe))
                f.write("\n")