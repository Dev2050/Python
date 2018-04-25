### using axes 3d test data to plot charts
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as nplot


figure=plt.figure()
chart=figure.add_subplot(1,1,1,projection='3d')
###get a sample data of delta 0.05
x,y,z=axes3d.get_test_data(0.05)
chart.plot(x,y,z, rstride=10,cstride=10)
chart.show()
