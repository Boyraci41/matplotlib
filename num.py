import matplotlib.pyplot as plt


days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]


slices=[7,2,2,13]
activies=["sleeping","eating","working","playing"]
cols=["c","m","r","k"]
plt.pie(slices,labels=activies,colors=cols,startangle=90,explode=(0,0.3,0,0))





plt.xlabel=('x')
plt.ylabel("y")
plt.title("Interisting Graph\nCheck it Out")
plt.legend()
plt.show()