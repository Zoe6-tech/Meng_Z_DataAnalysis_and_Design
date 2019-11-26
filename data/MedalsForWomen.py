import matplotlib.pyplot as plt

Medals=[6,6,6,9,15,18,27,39,46,46,45,51,51,54,63,99,111,189,208,232,233,272]
year=[1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]

plt.plot(year,Medals,linewidth=4.0,color='r',marker='o',markerfacecolor='blue',markersize=10)
plt.xlabel('Year of Winter Olympics')
plt.ylabel('Amount of Medals Win by Women')
plt.title('Medals Counts for Women of different Years')
plt.show()