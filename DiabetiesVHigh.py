states=['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']

feature="Blood sugar level(very high)-WOMEN"

data=[10.4,1.8,5.2,2.7,3.2,3.0,3.2,4.8,2.3,2.6,1.2,3.9]
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_ylabel("Blood Sugar Level( very high)-WOMEN")
ax.set_xlabel("states")
ax.set_title("Diabetes")

ax.bar(states,data)
plt.show()
