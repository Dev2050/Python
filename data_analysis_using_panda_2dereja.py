###More on data
import pandas as pd
data=pd.read_csv("c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.user", sep='|',names=['Id','Age','Gender','Occupation', 'ZipCode'])
print(data['Gender'].head(30))
##the following is as if you are telling the index number of the values in the array
columns_i=['Id','Age','Gender']
print(data[columns_i].tail(17))
print(data[data.Age>25].tail(10))
print("2nd tiME WE ARE PRINTING NEW ****************************************************************************************************************")
data.set_index('Id', inplace=True)
def theWriters():
    writers=[]
    for i in data:
        writers.append(data[((data.Age<35)&(data.Gender=='M')&(data.Occupation=='writer'))])
    return writers
writers_mined=theWriters()
c=1
for i in writers_mined:
    while c<2:
        print(i)
        c=c+1
print(len(writers_mined))
##describe data
print(data.describe())
print(data.dtypes)
##selecting specfic rows is using ix is used as index 
print(data.ix[[1,17,77]])
