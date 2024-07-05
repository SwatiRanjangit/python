from matplotlib import pyplot as plt

parts = [8,2,10,4]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(
    parts,
    labels=activities,
    colors = cols,
    explode=(0,0.2,0,0),
    shadow = True,
    startangle=180,
    autopct= '%1.1f%%'

)

plt.title("Pie graph")
plt.show()