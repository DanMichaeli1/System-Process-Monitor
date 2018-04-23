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
            print(separator)
            print(time.ctime() + "\n")
            if new_process_list:
                f.write("New processes:\n")
                print "New Processes:\n"
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
                        print(format % (start_time, uname, p.name(), p.pid, exe))
                        f.write(format % (start_time, uname, p.name(), p.pid, exe))
                f.write("\n")
                print "\n"
            if stopped_process_list:
                f.write("Stopped processes:\n")
                print "Stopped processes:\n"
                for p in stopped_process_list:
                    with p.oneshot():
                        try:
                            exe = p.exe()
                            uname = p.username()
                        except:
                            exe = ""
                            uname = "-"
                            pass
                        print(format2 % (uname, p.name(), p.pid, exe))
                        f.write(format2 % (uname, p.name(), p.pid, exe))
                f.write("\n")
            print(separator)