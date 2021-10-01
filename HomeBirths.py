states = ['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']
### Visualizing ABC Feature
feature = "Home births that were conducted by skilled health personnel "
data = [3.7,2.1,1.8,2.2,5.8,3.4,3.1,0.1,3.6,4.5,3.2,0.6]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis (Home births that were conducted by skilled health personnel)')
ax.set_xlabel('x-axis (States)')
ax.set_title('Delivery Care (for births in the 5 years before the survey)')
ax.bar(states,data)
plt.show()
