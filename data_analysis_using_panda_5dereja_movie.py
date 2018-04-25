###more on data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as npm

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
print("WATCH RIIGHT HERE AND LEARN")
print(movie_ratings.head())
uOnMovies=pd.merge(movie_ratings,dUsers1)
##the order method might not work
##x.groupby('title').size().order(ascedning=False)[:i] is the correct way to use it
most_rated=uOnMovies.groupby('title').size()[:30]
##the above is equal to uOnMovies.title.value_counts()[:30]
###the "title.value_counts()[:i] where i is an int
##is more accurate if 'order(ascending=False)' method is not used.
##the value_counts() does search for those titles with most repetition...
print(uOnMovies.title.value_counts()[:30])
print("THIS ARE THE MOST RATED MOVIES.........................**********************")
print(most_rated)
###which movies have the highest average score calculated by the aggregation method
movie_stats=uOnMovies.groupby('title').agg({'rating':[npm.size,npm.mean]})
##the size='how many times the movie *x* is rated by users' and the mean='explains
##the average of the rating whether it is 1 star, 2 stars, etc
#help(uOnMovies.groupby('title').agg)
print(movie_stats)
###did not work : ***print(uOnMovies.title.agg({'rating':[npm.size,npm.mean]}))
###sorting based on rating while calculating the ratings mean value of the movie_stats
print(movie_stats.sort_values([('rating','mean')],ascending=False).head())
###the above will print those movies with the highest *** type ratings for mean
###size column tells how many people rated it while the
##mean column tells "interms of ****starts given from users "
dUsers1.age.hist(bins=30)
plt.title('Distribution of users age')
plt.xlabel('age')
plt.ylabel('count of users')
plt.grid(axis='y', color='blue')
plt.show()
most_50=uOnMovies.groupby('movie_id').size()[:50]
print("*******************************************")
#uOnMovies.reset_index('movie_id', inplace=True)
print(uOnMovies)
pvMovie=uOnMovies.pivot_table(index=['movie_id','title'],columns=['gender'],values='rating',fill_value=0)
print("PRINT LAST RESTS HERE********************************************************")
print(pvMovie)
###if the subtraction results in +ve value males likes the movie better than the females
pvMovie['kensew']=pvMovie.M-pvMovie.F
print(pvMovie.head())
pvMovie.reset_index('movie_id', inplace=True)
###go through most_50 array data and append it to disagreements only the kensew column
###while kensew performs substraction as defined earlier(i.e. e['kensew']=pvMovie.M-pvMovie.F)
##and assigns the kensew column
disagreements=pvMovie[pvMovie.movie_id.isin(most_50.index)]['kensew']
print(disagreements)
plt.title('Rating between men and female')
plt.xlabel('Average ratings dfirrence')
plt.ylabel('Title')
help(disagreements.plot)
disagreements.plot(kind='barh',figsize=[2,2])
plt.show()



