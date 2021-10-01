states=['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']

feature=" Pregnant women age 15-49 years who are anaemic (<11.0 g/dl)"

data=[52.90,33.80,26.70,51.30,55,50,45.40,22.60,49.30,42.60,46.60,44.40]
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.set_ylabel("  Pregnant women age 15-49 years who are anaemic (%)")
ax.set_xlabel("States")
ax.set_title("Anemia")

ax.bar(states,data)
plt.show()
