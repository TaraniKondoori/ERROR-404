states = ['AD','HYD','KNR','KHM','MAH','NAL','NIZ','RAN','WAR-R','WAR-U']
### Visualizing ABC Feature
feature = "Blood sugar level - very high (>160 mg/dl) (%) -MEN)"
data = [2.8,7,5.9,4.8,3,2.6,3.8,3.6,4.9,3]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis( diabetes in MEN(%))')
ax.set_xlabel('x-axis (States)')
ax.set_title(' Blood sugar level - very high (>160 mg/dl) (%) -MEN)')
ax.bar(states,data)
plt.show()
