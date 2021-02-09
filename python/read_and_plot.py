#! /usr/bin/env python

# imports of external packages to use in our code

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


# read from generated random number txt file
print("\nReading the file..." )

out =[]
with open('random_numbers.txt') as f:
    for line in f:
        out.append(float(line))

print("\nPlotting..." )
# create histogram of our data
plt.figure(figsize=[10,8])
plt.style.use('ggplot')
n, bins, patches = plt.hist(out, 50, density=True, facecolor='c', alpha=0.75)

# plot formating options
plt.xlabel('Data')
plt.ylabel('Probability')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Histogram of Uniform random number')
plt.grid(True)

# show figure (program only ends once closed
plt.show()
