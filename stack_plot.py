from matplotlib import pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]

plt.plot([],[],color='m',label='sleeping',linewidth=4)
plt.plot([],[],color='g',label='eating',linewidth=4)
plt.plot([],[],color='r',label='working',linewidth=4)

plt.stackplot(days,sleeping,eating,working,color=['m','g','r'])

plt.title("Stack graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()