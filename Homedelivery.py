districts= ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Home births that were conducted by skilled health personnel(%)"
data = [1.8,0,1.6,0.5,1,1.7,1,1.2,0,0]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis(home births(%))')
ax.set_xlabel('x-axis (Districts)')
ax.set_title('Home births that were conducted by skilled health personnel(%)')
ax.bar(districts,data)
plt.show()
