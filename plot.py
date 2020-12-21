import re
import numpy as np
from matplotlib import pyplot as plt

ping_c = []
ping_python = []
with open("c.csv","r") as f:
    for line in f:
        print(line)
        a = re.search(r'\b(time=)\b', line)
        ping_time = line[a.end():a.end()+5]
        print(a.start(),a.end())
        print(ping_time)
        time = line[11:19]
        print(time)
        ping_c.append(ping_time)



with open("python.csv","r") as f:
    for line in f:
        print(line)
        a = re.search(r'\b(time=)\b', line)
        ping_time = line[a.end():a.end()+5]
        print(a.start(),a.end())
        print(ping_time)
        time = line[11:19]
        print(time)
        ping_python.append(ping_time)

font = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 16,
        }
np_arr_c = np.array(ping_c).astype('float64')
np_arr_python = np.array(ping_python).astype('float64')

plt.yticks(np.arange(min(np_arr_c), max(np_arr_c), 1))
plt.title( "python and c compression", fontdict=font)
h = plt.ylabel('time')
x_axis_python = np.arange(0, len(ping_python),1)
x_axis_c = np.arange(0, len(ping_c),1)
plt.margins(x=0.3, y=0.0)   # Values in (-0.5, 0.0) zooms in to center
plt.plot(x_axis_c,np_arr_c,x_axis_python,np_arr_python)
plt.show()

plt.title('C', fontdict=font)
plt.plot(x_axis_c,np_arr_c)
plt.show()

plt.title('Python', fontdict=font)
plt.plot(x_axis_python,np_arr_python)
plt.show()
