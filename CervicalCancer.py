states = ['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']
### Visualizing ABC Feature
feature = "Cervical Cancer screening "
data = [4.3,0.1,1.6,0.3,0.4,3.4,0.6,3.8,2.5,0.5,0.2,0.3]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis (cervical screening population)')
ax.set_xlabel('x-axis (States)')
ax.set_title('Cervical Cancer')
ax.bar(states,data)
plt.show()
