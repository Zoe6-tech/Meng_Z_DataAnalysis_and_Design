import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


year=['1924','1928','1932','1936','1948','1952','1956','1960','1964','1968','1972','1976','1980','1984','1988','1992','1994','1998','2002','2006','2010','2014']
y_Women=[6,6,6,9,15,18,27,39,46,46,45,51,51,54,63,99,111,189,208,232,233,272]
y_Men=[112,83,110,99,125,118,123,108,139,153,155,159,167,168,201,226,232,258,273,299,296,340]
bar_width=0.3

plt.bar(x=range(len(year)),height=y_Women,label="Women",alpha=0.8,color="red",width=bar_width)
plt.bar(x=np.arange(len(year))+bar_width,height=y_Men,label="Men",alpha=0.8,color="blue",width=bar_width)



for x,y in enumerate(y_Men):
	plt.text(x,y,'%s' % y,ha='center',va='top')
for x,y in enumerate(y_Women):
	plt.text(x,y,'%s' % y,ha='center',va='bottom')
plt.xticks(np.arange(len(year))+bar_width/2,year)
plt.xlabel('Year of Winter Olympics')
plt.ylabel('Number of Medals ')
plt.title('Number of Medals For Women and Men of Different Years')
plt.legend()
plt.show()