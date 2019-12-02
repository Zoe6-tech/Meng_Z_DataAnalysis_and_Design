import matplotlib.pyplot as plt

Medals=[5,7,5,8,11,13,18,27,25,23,23,24,23,24,24,30,32,42,43,44,44,44]
year=[1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]

plt.plot(year,Medals,linewidth=4.0,color='r',marker='o',markerfacecolor='r',markersize=10)
plt.xlabel('Year of Winter Olympics')
plt.ylabel('Proportion of  Medals Win by Women(%)')
plt.title('Proportion of Total Medals for Women Medalist Over Years')
plt.show()