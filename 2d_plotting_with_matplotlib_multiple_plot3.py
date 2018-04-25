from matplotlib import pyplot as plt
fig_inst=plt.figure()
##the outer border set to green color
outer_rect=fig_inst.patch
outer_rect.set_facecolor('green')
###create a graph in a specified canvas area add_subplot(height,width,number of graphs, background_color)
graph=fig_inst.add_subplot(1,1,1,facecolor="black")
###assign values to x and y coordinates of the first graph
x1=[1,3,5,7]
y1=[7,27,47,67]
x2=[2,4,6]
y2=[17,37,57]
x3=[1,4,7]
y3=[21,41,51]

###draw the graph using the given coordinates on the specified canvas  using red color with line tickness 4.0
graph.plot(x1,y1,'red',linewidth=3.0)
graph.plot(x2,y2,'yellow',linewidth=6.0)
graph.plot(x3,y3,'blue',linewidth=7.0)
###control how the params line|bars look for the x,y-axis values
graph.tick_params(axis='x', color='white')
graph.tick_params(axis='y',color='white')
###now use spines method to control the outer top, bottom, left, right borders
graph.spines['top'].set_color('w')
graph.spines['bottom'].set_color('w')
graph.spines['right'].set_color('w')
graph.spines['left'].set_color('w')
###set title and labels
graph.set_title('Practice practice practice')
graph.set_xlabel('x values')
graph.set_ylabel('y values')
##now it is time to show the graph but you use the container which is the figure instance it does make sense
fig_inst.show()


