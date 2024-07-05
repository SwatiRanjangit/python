from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,3,6,7]

plt.scatter(x,y,color='r',s=80,marker='*')

plt.title("Scatter graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
# plt.legend()
plt.show()