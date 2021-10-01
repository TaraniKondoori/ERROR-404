states = ['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']
### Visualizing ABC Feature
feature = "Institutional births"
data = [91.5,52.2,96.9,88.5,80.4,76.4,94,99.8,90.3,90.5,84,98.9]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( Institutional births )')
ax.set_xlabel('x-axis (States)')
ax.set_title('Delivery Care (for births in the 5 years before the survey)')
ax.bar(states,data)
plt.show()
