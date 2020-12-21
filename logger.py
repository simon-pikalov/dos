# import subprocess
# result = subprocess.check_output(['ping', '127.0.0.1'])
# with open("new.txt", "a") as myfile:
#     myfile.write(result)
import subprocess
import time
import threading
from datetime import datetime
from time import gmtime, strftime

import csv


class Log(threading.Thread):

    def __init__(self,ip):
        threading.Thread.__init__(self)
        self.timestr = time.strftime("syn_log_%d%m%Y-%H%M%S")
        self.file_name = self.timestr + ".csv"
        self.file = open(self.file_name, "a")
        self.init_time = time.time()
        self.ip = ip
        self.sleep_time = 0.001

    def write_to_log(self,result):
        line_str =str(time.ctime())+","+ str(result)+"\n"
        self.file = open(self.file_name, "a")
        self.file.write(line_str)
        self.file.close()

    def run(self):
        while (True):
            try:
                time.sleep(self.sleep_time)
                time_str = str(datetime.now().strftime("%H:%M:%S.%f"))
                result = subprocess.check_output(['ping', '-c 1', self.ip])
                result = time_str+" "+str(result)
                self.write_to_log(result)
                print(result)
            except:
                print("exeption")


if __name__ == '__main__':
    log = Log("10.0.2.5")
    log.start()
    # result = subprocess.check_output(['ping','-c 1', '10.0.2.5'])
    # print(result)
