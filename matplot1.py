from matplotlib import pyplot as plt

x = [5,3,2,1,7]
y = [10,5,8,4,2]

x1 = [10,20,30]
y1 = [5,9,10]

plt.plot(x,y,marker='o',color='g',label='plot1')
plt.plot(x1,y1,marker='D',color='r',label='plot2')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Simple graph")
plt.legend()
plt.grid(color='m')
plt.show()
