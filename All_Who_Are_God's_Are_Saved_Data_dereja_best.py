##more on data
import pandas as pd
frame1=pd.DataFrame({'one':range(4),'for':['All','Can','Be','Saved']})
frame2=pd.DataFrame({'one':range(4),'for':["Saved","Are","All","God's"]})
##on right means keep the one right intact,do not change anything about it
##allSaved=pd.merge(frame1,frame2,on='for', how='right')
##on left means keep the one on the left 
#allSaved=pd.merge(frame1,frame2,on='for', how='right')
#allSaved=pd.merge(frame1,frame2,on='for')
###key word outer will merge all contents
#allSaved=pd.merge(frame1,frame2,on='for', how='outer')
allSaved=pd.merge(frame1,frame2,on='for', how='inner')
#allSaved=pd.concat([frame1,frame2])
#allSaved=pd.concat([frame1,frame2], axis=1)
print("Blessed be the Father, the Son, and, the Holy Spirit, the One True God ")
print(allSaved)
