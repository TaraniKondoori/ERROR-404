districts = ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Blood sugar level - very high (>160 mg/dl) (%) -WOMEN)"
data = [4.5,11.4,8.5,8.3,4.7,6.5,6.1,8.3,7.6,7.3]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( diabetes in WOMEN(%))')
ax.set_xlabel('x-axis (Districts)')
ax.set_title(' Blood sugar level - very high (>160 mg/dl) (%) -WOMEN)')
ax.bar(districts,data)
plt.show()
