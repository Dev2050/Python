###This lesson is about multiple graph
from matplotlib import pyplot as plt
##create figure instance
fig_inst=plt.figure()
rec=fig_inst.patch
rec.set_facecolor('green')
x1=[1,3,5,7,9]
y1=[7,27,47,67,87]
x2=[2,4,6,8,10]
y2=[17,37,57,77,97]
x3=[1.5,2.5,5.5,7.5,9.5]
y3=[12.5,32,52,72,92]
## first set sub-canvas inside the major canvas and create graph
###since we going to add a number of graph let us make the height of the
###major canvas longer and tell the order of the graphs as 3rd parameter
graph1=fig_inst.add_subplot(2,2,1,facecolor='black')
graph1.plot(x1,y1,'red', linewidth=2.0)
###next control the barlines
graph1.tick_params(axis='x', color='white')
graph1.tick_params(axis='y', color='white')
###next make the spines white they are the top, bottom, left, right outer grids
graph1.spines['top'].set_color('w')
graph1.spines['bottom'].set_color('w')
graph1.spines['left'].set_color('w')
graph1.spines['right'].set_color('w')
##write the title, xlabel, and ylabel
graph1.set_title('It needs practice', color="white")
graph1.set_xlabel('x values', color="white")
graph1.set_ylabel('y values', color="white")
###now test by show NB: you use the figure instance

########the second graph starts here Now since you want
##to draw 3 graphs then it should be height=2
##and width =2 and the number of the graph in its preceeding order
graph2=fig_inst.add_subplot(2,2,2,facecolor='black')
graph2.plot(x2,y2,'blue', linewidth=4.0)
###next control the barlines
graph2.tick_params(axis='x', color='white')
graph2.tick_params(axis='y', color='white')
###next make the spines white they are the top, bottom, left, right outer grids
graph2.spines['top'].set_color('w')
graph2.spines['bottom'].set_color('w')
graph2.spines['left'].set_color('w')
graph2.spines['right'].set_color('w')
##write the title, xlabel, and ylabel
graph2.set_title('It needs practice and more practice', color="white")
graph2.set_xlabel('x values', color="white")
graph2.set_ylabel('y values', color="white")

###########
####the third graph starts here here the 3rd
##parameter is not 3 but 1 it must be reset as it is on new column of the major canvas
graph3=fig_inst.add_subplot(2,2,3,facecolor='blue')
graph3.plot(x3,y3,'white',linewidth=6.0)
graph3.tick_params(axis='x', color='white')
graph3.tick_params(axis='y', color='white')
graph3.spines['top'].set_color('w')
graph3.spines['bottom'].set_color('r')
graph3.spines['left'].set_color('y')
graph3.spines['right'].set_color('b')
graph3.set_title('The practice is important', color="white")
graph3.set_xlabel('x values', color="white")
graph3.set_ylabel('y values', color="white")
####The fourth graph
###fig_inst=plt.figure()
x4=[0,0.52,0.79,1.1,1.6,2.1,2.4,2.62,3.14]
y4=[1,0.56,0.7, 0.5,0,-0.5,-0.7,-0.56,-1]
graph4=fig_inst.add_subplot(2,2,4,facecolor='orange')
graph4.plot(x4,y4,'red',linewidth=8.0)
graph4.tick_params(axis='x',color='white')
graph4.tick_params(axis='y',color='white')
graph4.spines['top'].set_color('w')
graph4.spines['bottom'].set_color('w')
graph4.spines['left'].set_color('w')
graph4.spines['right'].set_color('w')
graph4.set_title("Obeying God will make sure your safety.", color="White")
graph4.set_xlabel("'x' said: The source of any True and Holy moral is God himself.", color="white")
graph4.set_ylabel("'y' said: Any virtue that is Holy and True does not disrupt the natural order. For the source of such virtue is none other than God himself.", color="white")

###now test by show NB: you use the figure instance
fig_inst.show()
