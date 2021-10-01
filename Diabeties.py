states=['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']

feature="Blood sugar level(high)-WOMEN"

data=[7.3,4.8,8.9,5.8,6.3,5.9,6.3,8.7,5,6.1,3.5,7.1]
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_ylabel("Blood Sugar Level(high)-WOMEN")
ax.set_xlabel("states")
ax.set_title("Diabetes")

ax.bar(states,data)
plt.show()
