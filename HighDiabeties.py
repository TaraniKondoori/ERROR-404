districts= ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Blood sugar level - high (141-160 mg/dl)23 (%)-WOMEN"
data = [4.7,5.4,6.2,6.9,4.9,5.9,5.1,5.2,6.6,7.7]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( diabetes in WOMEN(%))')
ax.set_xlabel('x-axis (Districts)')
ax.set_title(' Blood sugar level - high (141-160 mg/dl)23 (%)-WOMEN')
ax.bar(districts,data)
plt.show()
