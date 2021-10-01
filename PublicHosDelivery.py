districts = ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Births in a public health facility that were delivered by caesarean section (%)"
data = [30.6,35.4,66.8,59.7,25.9,50.4,45,42.9,64.6,44.2]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis(births in public health facility(%))')
ax.set_xlabel('x-axis (Districts)')
ax.set_title('Births in a public health facility that were delivered by caesarean section (%)')
ax.bar(districts,data)
plt.show()
