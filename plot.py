import re

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

ping_c_rtt = [] # rtt from the monitor
ping_python_rtt = [] # rtt from the monitor
python_dict = {} # key = attacker time , value =num of pakets
c_dict = {} # key = attacker time , value =num of pakets


with open("pings_results_c.txt", "r") as f:
    for line in f:
        # print(line)
        a = re.search(r'\b(time=)\b', line)
        ping_time = line[a.end():a.end()+5]
        time = line[11:19]
        ping_c_rtt.append(ping_time)



with open("pings_results_p.txt", "r") as f:
    for line in f:
        a = re.search(r'\b(time=)\b', line)
        ping_time = line[a.end():a.end()+5]
        time = line[11:19]
        ping_python_rtt.append(ping_time)


with open("syns_results_c.txt", "r") as f:
    for line in f:
        time , paket = line.split(",")
        time.replace(" ","")
        c_dict[time] = c_dict.get(time, 0) + 1


with open("syns_results_p.txt", "r") as f:
    for line in f:
        time , paket = line.split(",")
        time.replace(" ","")
        python_dict[time] = python_dict.get(time, 0) + 1



font = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 16,
        }
np_arr_c = np.array(ping_c_rtt).astype('float64')
np_arr_python = np.array(ping_python_rtt).astype('float64')
std_c = np.std(np_arr_c)
avarage_c = np.average(np_arr_c)
print(f"average for c is {avarage_c} and std is {std_c}")

std_python = np.std(np_arr_python)
avarage_python = np.average(np_arr_python)
print(f"average for c is {avarage_python} and std is {std_python}")


plt.yticks(np.arange(min(np_arr_c), max(np_arr_c), 1))
plt.title( "python and c compression", fontdict=font)
y_axis_python = np.arange(0, len(ping_python_rtt), 1)
x_axis_c = np.arange(0, len(ping_c_rtt), 1)
plt.margins(x=0.3, y=0.0)   # Values in (-0.5, 0.0) zooms in to center
plt.plot(x_axis_c, np_arr_c, y_axis_python, np_arr_python)
plt.show()

plt.title('C', fontdict=font)

plt.plot(np_arr_c)

plt.show()

plt.title('Python', fontdict=font)
plt.plot( np_arr_python)
plt.show()



plt.title('Python attacker', fontdict=font)

plt.plot(python_dict.keys(),python_dict.values())
x_ticks = np.arange(0, 100, 40)
plt.xticks(x_ticks)
plt.show()


plt.title('C attacker', fontdict=font)

plt.plot(c_dict.keys(),c_dict.values())
x_ticks = np.arange(0, 100, 40)
plt.xticks(x_ticks)
plt.show()


