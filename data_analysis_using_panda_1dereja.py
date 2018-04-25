### data anaysis
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import numpy as npm
import matplotlib.pyplot as plt

users=pd.read_csv("c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.user", sep='|', names=['Id','Age','Gender','Occupation','ZipCode'])
print(users)
figure=plt.figure()
##graph=figure.add_subplot(1,1,1, facecolor='black')

d3plot=figure.add_subplot(1,1,1,projection='3d')
rectangle=d3plot.patch
rectangle.set_facecolor('green')
def makeX():
    x=[]
    count=0
    for i in users.Id:
        while count<9:
            x.append(i)
            count=count+1
    return x
def makeY():
    y=[]
    for i in range(0,9):
      y.append(i)
    return y
def makeZ():
    z=[]
    count=0
    for i in users.Age:
        while count<9:
            z.append(i)
            count=count+1
    return z
x=makeX()
print(x)
y=makeY()
print(y)
z=makeZ()
print(z)
##d3plot.plot3D(x,y,z)
dx=npm.ones(9)
dy=npm.ones(9)
dz=[1,0,1,0,1,0,1,0,1]
d3plot.bar3d(x,y,z,dx,dy,dz)
##d3plot.tick_params(axis='x', color='red')
##d3plot.tick_params(axis='y', color='red')
##d3plot.tick_params(axis='z', color='red')
#d3plot.spines['top'].set_color('w')
#d3plot.spines['bottom'].set_color('w')
#d3plot.spines['left'].set_color('w')
#d3plot.spines['right'].set_color('w')
d3plot.set_title('Jesus Christ is Lord Every where')
d3plot.set_xlabel('User Id')
d3plot.set_zlabel('Age')
d3plot.set_ylabel('Equalizer')
plt.show()
###displays the first four rows
#users.head(4)
users.head()
###the very bottom ones perhaps four rows or you can specify
#users.tail(3)
users.tail()
#others treat it as array
users[1:20]
users[:90]
users[90:]
users[:-2]
#### This is about data manipulation
users['Id'].head(10)
