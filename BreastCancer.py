states = ['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']
### Visualizing ABC Feature
feature = "Breast Cancer Screening"
data = [0.7,7.2,1.3,0.1,0.1,1.5,0.4,2.8,1.6,4.2,4.8,0.15]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis (breast screening population)')
ax.set_xlabel('x-axis (States)')
ax.set_title('Breast Cancer')
ax.bar(states,data)
plt.show()
