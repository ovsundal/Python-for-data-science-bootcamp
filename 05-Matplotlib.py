import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# FUNCTIONAL method for creating a matplotlib plot
# basic plotting
# plt.plot(x, y)

# set labels / title
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')

# plt.show()

# add subplot (several plots per page)
# plt.subplot(1, 2, 1)
# plt.plot(x, y, 'r')

# plt.subplot(1, 2, 2)
# plt.plot(y, x, 'b')

# plt.show()

# OBJECT-ORIENTED method for creating a matplotlib plot

# fig = plt.figure()
# 10% in from left, 10% up from bottom, takes 80% of canvas size width, 80% of canvas size height
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#
# axes.plot(x, y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Set Title')

# fig = plt.figure()

# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# 20% in from left, 50% up from bottom, takes 40% of canvas size width, 30% of canvas size height
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

# axes1.plot(x, y)
# axes2.plot(y, x)
#
# axes1.set_title('LARGER PLOT')
# axes2.set_title('SMALLER PLOT')

# make several plots
# fig, axes = plt.subplots(nrows=1, ncols=2)
#
# axes[0].plot(x, y)
# axes[0].set_title('First Plot')
#
# axes[1].plot(y, x)
# axes[1].set_title('Second Plot')

# iterate over plots
# for current_ax in axes:
#     current_ax.plot(x, y)


# axes.plot(x, y)

# Figure Size and DPI
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))

# ax = fig.add_axes([0, 0, 1, 1])
# axes[0].plot(x, y)
#
# axes[1].plot(y, x)

# save picture as file
# fig.savefig('my_picture.png', dpi=200)

# fig = plt.figure()
#
# ax = fig.add_axes([0, 0, 1, 1])
# ax.plot(x, x**2, label='X Squared')
# ax.plot(x, x**3, label='X Cubed')

# add legend
# ax.legend(loc=0)

# Setting colors
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
# lw = line width, alpha = opacity, ls = line style, marker marks each datapoint
ax.plot(x, y, color='purple', lw=1, alpha=.5, ls='--', marker='o', ms=20,
        markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='green')  # takes both string and hex

# show subset of x-axis, upper bound, lower bound
ax.set_xlim([0, 1])
ax.set_ylim([0, 2])


# prevent overlapping
plt.tight_layout()

plt.show()
