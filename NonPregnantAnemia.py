states=['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']

feature="  Non-pregnant women age 15-49 years who are anaemic "

data=[60.2,43.5,31.4,53,63.1,53,47.80,2.5,47.9,54,46.8,55.4]
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_ylabel(" Non-pregnant women age 15-49 years who are anaemic (%)")
ax.set_xlabel("States")
ax.set_title("Anemia")

ax.bar(states,data)
plt.show()
