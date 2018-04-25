###data and the panda

import pandas as pd
import numpy as npm
##create a data structure
data={
    'Students':["Tewodro","Menelik","Jhon","Markos"],
    'Mathematics':[100,100,100,100],
    'Physics':[100,100,100,100],
    'Sport':[100,100,100,100]
}
d_struct=pd.DataFrame(data,columns=['Students','Mathematics','Physics','Sport'])
print(d_struct)
cities= {'Addis':100, 'Helsinki':100, 'NewYork': 100, 'Jerusalem': 100}
ext=pd.Series(cities)
extract=npm.sqrt(ext)
print(extract)
