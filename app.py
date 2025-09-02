import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
  response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=1dd6bb1a907988d52fa52821d596ea25".format(movie_id))
  data = response.json()
  print(data)
  return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key= lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster =[]

    for i in distances:
       movie_id = movies.iloc[i[0]].movie_id
       recommended_movies.append(movies.iloc[i[0]].title)
       recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('sim.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')
option = st.selectbox(
'which movie do you like',
movies['title'].values)

if st.button('recommend'):
    names,posters = recommend(option)
    col1, col2 , col3 ,col4 ,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])