from matplotlib import pyplot as plt
c_r=open("C:/Users/Fissha/Desktop/tech/Python/python_part5_data/coordinates.txt", "r")
c_r_f=c_r.read().split('\n')
x=[]
y=[]
val=[]
for i in c_r_f:
	val=i.split(',')
	x.append(val[0])
	y.append(val[1])

for i in range(0,1):
	print(x)
	print(y)

##plot([],[])
plt.plot(x,y)
plt.title('Growup')
plt.xlabel("The x axis")
plt.xlabel("The Y axis")
###now if you call plt.show() it will show the graph
plt.show()
### let us use an instance of figure and draw a customized graph using it
fig_ist=plt.figure()
###use the patch() method using fig_ist and have control how the outside shade looks like
outer_rec_region=fig_ist.patch
outer_rec_region.set_facecolor('green')
### now add graph into the figure
###in this case let us add to graphs
x=[1,2,3,4,5]
y=[77,88,99,110,121]
xx=[5,4,3,2,1]
###yy=[121,111,99,88,77]
yy=[77,88,99,110,121]
###first parameter is height, then width then number of graphs then, color
graph_1xy=fig_ist.add_subplot(1,1,1,facecolor='black')
graph_1xy.plot(x,y,'red',linewidth=8.0)
graph_2xy=fig_ist.add_subplot(1,1,1,facecolor='black')
graph_2xy.plot(xx,yy,'yellow',linewidth=2.0)
###now you shall have control over the params or the x,y axis number dot|line bars
graph_1xy.tick_params(axis='x', color='white')
graph_1xy.tick_params(axis='y', color='white')
###now here you can have control over the spines of the frames
graph_1xy.spines['top'].set_color('w')
graph_1xy.spines['bottom'].set_color('w')
graph_1xy.spines['right'].set_color('w')
graph_1xy.spines['left'].set_color('w')
graph_1xy.set_title('Practice practice and practice')
graph_1xy.set_xlabel('x values')
graph_1xy.set_ylabel('y values')
#######do the same for graph 2 but not important since we are using same canvas area 
fig_ist.show()
