states = ['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']
### Visualizing ABC Feature
feature = " Births in a public health facility that were delivered by caesarean section  "
data = [25.5,12.5,19.9,10.8,8.6,16.4,16.9,31.4,13.1,17.8,6.1,26.3]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( Births in a public health facility that were delivered by caesarean section)')
ax.set_xlabel('x-axis (States)')
ax.set_title('Delivery Care (for births in the 5 years before the survey)')
ax.bar(states,data)
plt.show()
