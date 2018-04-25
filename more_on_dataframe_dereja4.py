###more on data
import pandas as pd
import numpy as nmp
import matplotlib.pyplot as plt

headers=['Name','JobTitles','Department','FullPartTime','SalaryHourly','TypicalHours','AnnualSalary','HourlyRate']
data=pd.read_csv("c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/Employee.csv",header=None,names=headers)
print(data)
#data.head()
###this will sort the dataframe using the department key word and returns a not null value
sort_by_dept=data.groupby('Department')
print("DEPARTMENT STRATS HERE *******************************************")
print(sort_by_dept)
print(sort_by_dept.count().head())
print(sort_by_dept.size().head())
headers1=['user_id','movie_id','rating','unix_timestamp']
dataframe=pd.read_csv("c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.data", sep="\t", names=headers1)
print(dataframe.head())
m_names=['mov_id','title','re_date','video_date','url']
moviedata=pd.read_csv('c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.item', sep='|', names=m_names, usecols=range(5), encoding='ISO-8859-1')
print(moviedata.head(10))
#print(moviedata.groupby('title').size().order(ascending=False)[:20])
print(moviedata.title.value_counts()[:20])
#y=pd.merge(dataframe,moviedata,)
#print(y.groupby('title').agg({'rating':[nmp.size,nmp.mean]}))
usersdata=pd.read_csv("c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.user", sep='|',names=['Id','Age','Gender','Occupation', 'ZipCode'])
usersdata.Age.hist(bins=50)
plt.title('Age distribution')
plt.xlabel('x ')
plt.ylabel('y ')
plt.show()




