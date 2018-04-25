###draw pie
import matplotlib.pyplot as plt
pie_value=[7,7,7,7,7,7,7]
###adding new features like specifing the color type
label=["Paient","Loving","Powerful***","Generous","Kind","Almighty","AllKnowing"]
colors=['orange','cyan','green','yellow','magenta','purple','blue']
#plt.pie(pie_value, colors=colors)
##change the orientation
plt.title('Geuss What is the issue here')
plt.pie(pie_value, colors=colors, startangle=90, labels=label)
###make shep circuar by changing the ridus using the key word equal
plt.axis('equal')
plt.legend(title='The Legendary', loc='upper left')
plt.show()
