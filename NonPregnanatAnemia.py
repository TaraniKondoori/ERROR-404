districts = ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Non Pregnant women age 15-49 years who are anaemic(%)"
data = [55.4,57.8,57.3,66.4,61.1,57.1,57.4,58.1,56.9,58.1]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( non-pregnant women(%)')
ax.set_xlabel('x-axis (Districts)')
ax.set_title('Non Pregnant women age 15-49 years who are anaemic(%)')
ax.bar(districts,data)
plt.show()
