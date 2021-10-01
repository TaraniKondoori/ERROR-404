states = ['AP','ANP','Goa','gujarat','HYNA','hp','KN','kerala','MR','PNB','RJ','TN']
### Visualizing ABC Feature
feature = "Breast Cancer Screening"
data = [8.3,24.2,0.8,0.5,0.8,2.6,0.3,0.8,1.7,0.4,0.1,0.8]
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('y-axis (oral cancer screening population)')
ax.set_xlabel('x-axis (States)')
ax.set_title('Oral Cancer')
ax.bar(states,data)
plt.show()
