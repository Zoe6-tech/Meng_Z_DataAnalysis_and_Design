import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

labels=['Medals For Women','Medals For Men']
colors=['red','blue']
x=[1826,3944]

plt.pie(x,labels=labels,colors=colors,autopct='%1.2f%%')
plt.title('Proportion of Total Medal')
plt.show()