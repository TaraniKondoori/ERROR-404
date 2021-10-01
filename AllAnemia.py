Districts = ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Institutional births"
data = [55.2,57.6,57.5,65.9,61.1,56.7,56.8,57.7,56.7,57.5]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( aneamic patients(%)')
ax.set_xlabel('x-axis (States)')
ax.set_title(' All women age 15-49 years who are anaemic22 (%) ')
ax.bar(Districts,data)
plt.show()
