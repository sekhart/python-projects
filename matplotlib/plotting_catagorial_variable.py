import matplotlib.pyplot as plt

import numpy as np

names = ['group_a', 'group_b', 'group_c']
values = [10, 50, 100]


plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values, linewidth=2.0)
plt.subplot(132)
plt.scatter(names, values, linewidth=5.0)
plt.subplot(133)
plt.plot(names, values, linewidth=5.0)
lines = plt.plot(names, values, names, values)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 3.0)
plt.suptitle('Categorical Plotting')
plt.show()


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()