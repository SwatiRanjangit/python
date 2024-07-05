from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label='bar1',color='m')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='bar2',color='y')
plt.title("Bar graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()