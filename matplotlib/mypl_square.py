import matplotlib.pyplot as plt

import numpy as np

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b')
plt.axis([0, 6, 0, 30])
plt.title('Square Numbsers', fontsize=15)
plt.xlabel('Values', fontsize=10)
plt.ylabel('Squares', fontsize=10)
plt.show()
