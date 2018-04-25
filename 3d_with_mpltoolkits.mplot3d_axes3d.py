#Draw some 3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
##first create figure 
figure=plt.figure()
###then plot a chart on the figure by specifing the height and width etc...
chart=figure.add_subplot(1,1,1,projection='3d')
X=[1,2,3,4,5,6,7,8]
Y=[2,5,3,8,9,5,6,1]
Z=[3,6,2,7,5,4,5,6]
chart.plot_wireframe(X,Y,Z)
plt.show()
