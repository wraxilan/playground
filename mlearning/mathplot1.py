#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
# Create a second array using sine
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.figure(1)
plt.plot(x, y, marker="x")

z = np.cos(x)
plt.figure(2)
plt.plot(x, z, marker="x")
plt.show(1)
