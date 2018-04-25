#draw bar charts
import matplotlib.pyplot as plt
##OR from matplotlib import pyplot as plt
###next import numpy for charts
import numpy as barpy
###next create the design pattern for the bar chart
###below you are arranging 7 bars while keeping 0.7 distnace
##between each bars 
design_pattern=barpy.arange(7)+0.7
###next plot it using the plt.bar method
plt.bar(design_pattern, (1,2,3,4,5,6,7),align='center', color='blue')
###try adding title and labels and color them
creation=["Light_Darkness(=>)Day_Night","Firmament is Heaven","Earth('Yebs')_Sea_Grass_Herb(w)Fruits(w)Seeds","LIGHTS(Sun_Moon_Stars)","Water_Life(+)_Fowl","LIVINGCREATURE(Cattle_Creeping.Thing_Beasts)/===/'God created man in his image'", "SENBET"]
#string="Creation: "
def printCreation():
    for i in creation:
        print(i)
printCreation()
#plt.title(print('''"Light_Darkness(=>)Day_Night","Firmament is Heaven","Earth('Yebs')_Sea_Grass_Herb(w)Fruits(w)Seeds","LIGHTS(Sun_Moon_Stars)","Water_Life(+)_Fowl","LIVINGCREATURE(Cattle_Creeping.Thing_Beasts)/===/'God created man in his image'", "SENBET"'''))
plt.xlabel("x values", color="black")
plt.ylabel("y values", color="black")
##give names to your bar values
##name=["Light_Darkness(=>)Day_Night","Firmament is Heaven","Earth('Yebs')_Sea_Grass_Herb(w)Fruits(w)Seeds","LIGHTS(Sun_Moon_Stars)","Water_Life(+)_Fowl","LIVINGCREATURE(Cattle_Creeping.Thing_Beasts)/===/'God created man in his image'", "SENBET"]
name=["Day-One", "Day-Two", "Day-Three", "Day-Four", "Day-Five", "Day-Six", "Day-Seven"]
###now control how your params looks like, let it stay black
plt.tick_params(axis="x", color="black")
plt.tick_params(axis="y", color="black")
###use the xticks method
plt.xticks(design_pattern, name)
##use subplots_adjust to control the outer grids
plt.subplots_adjust(left=0.11, bottom=0.12, right=0.94, top=0.51)
##have control of the background
##try showing what if you achieved anything up onto this moment
plt.show()
