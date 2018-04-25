###This lesson is on data frames God bless Avinash Jain, May he reveal for him
###The Way, The Truth, and The Life:The Lord Jesus Christ
import pandas as pd
###create a dataframe of dictionaries
frame1=pd.DataFrame({'star':range(4),'name':['Debe','YeDebe Ljoch','Oryon','Sebatu']})
frame2=pd.DataFrame({'':range(5,9),'name':['Sky_Blue','Green','Yellow','Red']})
print(frame2)
print(pd.merge(frame1,frame2))
