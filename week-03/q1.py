from itertools import count
from re import I
import numpy as np
import matplotlib.pyplot as plt

N = int(input())

results = np.random.randint(0, 100, N)

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].set(title='Passed and not passed')
axes[0, 0].bar(
    ['Passed', 'Not passed'],
    [len([i for i in results if i >= 60]),
     len([i for i in results if i < 60])],
    width=1
)

axes[0, 1].set(title='Plot')
axes[0, 1].plot(sorted(results))
axes[0, 1].set_yticks(np.arange(0, 105, 5))

axes[1, 0].set(title='Scatter')
axes[1, 0].scatter(np.arange(0, len(results)), results, marker='+')
axes[1, 0].set_yticks(np.arange(0, 105, 10))

axes[1, 1].set(title='Pie')
axes[1, 1].pie(
    [len([i for i in results if i > 80]),
     len([i for i in results if i > 60 and i <= 80]),
     len([i for i in results if i <= 60])],
    labels=['81~100', '60~80', '0~59'],
    colors=['yellowgreen', 'gold', 'lightskyblue']
)

plt.show()
