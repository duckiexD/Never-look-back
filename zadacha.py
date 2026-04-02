import numpy as np
import matplotlib.pyplot as plt



l1 = 20
l2 = 18
l3 = 16
 
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot()

y = [l1, l2, l3]
x = [1, 2, 3]
 

ax.step(x, x)
ax.grid()
 
plt.show()