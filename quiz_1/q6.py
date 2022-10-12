import numpy as np
import matplotlib.pyplot as plt

height = np.random.normal(170, 10, 1000)

fig, axes = plt.subplots(nrows=2)

axes[0].set(title='height line chart')
axes[0].plot(sorted(height))
axes[0].set_yticks(np.arange(141, 201, 5))

axes[1].set(title='height pie chart')
axes[1].pie(
    [
        len([i for i in height if i > 141 and i <= 150]),
        len([i for i in height if i > 151 and i <= 160]),
        len([i for i in height if i > 161 and i <= 170]),
        len([i for i in height if i > 171 and i <= 180]),
        len([i for i in height if i > 181 and i <= 190]),
        len([i for i in height if i > 191 and i <= 200])
    ],
    labels=["141-150", "151-160", "161-170", "171-180", "181-190", "191-200"],
)

plt.show()
