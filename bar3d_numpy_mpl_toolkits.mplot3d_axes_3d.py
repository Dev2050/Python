##A bar3d story
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as nplt

##create figure
figure=plt.figure()
###plot a chart inside the figure and set it to chart variable
chart=figure.add_subplot(1,1,1,projection='3d')
###set values
###X and Y values tell where in the graph to plot it, while the
##Z value controls to what height the bars are levitated 
X,Y,Z=[1,2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,2,1],[0,0,0,0,7,0,0,0,0]
dx=nplt.ones(9)
dy=nplt.ones(9)
#the delta zed is height controller
##setting the values of dz to [0,0,0,0,0,0,0,0,0] will make the height to be zero 
dz=[1,2,3,4,5,6,7,8,9]
##draw the chart
chart.bar3d(X,Y,Z,dx,dy,dz, color='red')
##put labels 
chart.set_xlabel('x label')
chart.set_ylabel('y label')
chart.set_zlabel('z label')

plt.show()
