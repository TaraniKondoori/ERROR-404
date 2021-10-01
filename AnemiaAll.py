states=['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']

feature=" All women age 15-49 years who are anaemic"

data=[0.58,0.56,0.31,0.54,0.5,0.5,0.6,0.1,0.4,0.53,0.46,0.55]
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_ylabel(" All women age 15-49 years who are anaemic")
ax.set_xlabel("States")
ax.set_title("Anemia")

ax.bar(states,data)
plt.show()
