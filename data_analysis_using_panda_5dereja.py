###more on data
import pandas as pd
import matplotlib.pyplot as plt

names_s=['user_id','age','gender','occupation','zip_code']
dUsers1=pd.read_csv("c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.user", sep='|',names=names_s)
print(dUsers1.head())
headers1=['user_id','movie_id','rating','unix_timestamp']
dRating=pd.read_csv("c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.data", sep="\t", names=headers1)
print(dRating.head())
m_names=['movie_id','title','release_date','video_release_date','imdb_url']
dMovie=pd.read_csv('c:/users/fissha/desktop/tech/python/python_part5_data/ml-100k/u.item', sep='|', names=m_names, usecols=range(5), encoding='ISO-8859-1')
print(dMovie.head())
movie_ratings=pd.merge(dRating,dMovie)
usersOnMovies=pd.merge(movie_ratings,dUsers1)


