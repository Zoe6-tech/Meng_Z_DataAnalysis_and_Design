import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

labels=['Medals For Women','Medals For Men']
colors=['red','blue']
x=[6,112]

plt.pie(x,labels=labels,colors=colors,autopct='%1.2f%%')
plt.title('Medal counts for women and men at the 1924 Winter Olympics')
plt.show()