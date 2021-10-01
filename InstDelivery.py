districts= ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Institutional births"
data = [94.1,98.3,98.4,97.9,98.1,98.3,97.3,97.2,100,99.7]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis(institutional births(%))')
ax.set_xlabel('x-axis (Districts)')
ax.set_title('Institutional births (%)')
ax.bar(districts,data)
plt.show()
