states=['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']

feature="Blood Sugar level-MEN"

data=[5.9,3.3,7.3,3.5,2.1,2.6,3.7,0.7,2.5,2.9,2.4,1.2]
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_ylabel("Blood Sugar Levels MEN")
ax.set_xlabel("States")
ax.set_title("Diabetes")

ax.bar(states,data)
plt.show()
