districts = ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Pregnant women age 15-49 years who are anaemic(%)"
data = [50.4,53.2,0,0,61,0,0,47.2,0,39.8]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( [pregnant women(%)')
ax.set_xlabel('x-axis (Districts)')
ax.set_title(' Pregnant women age 15-49 years who are anaemic(%)')
ax.bar(districts,data)
plt.show()
