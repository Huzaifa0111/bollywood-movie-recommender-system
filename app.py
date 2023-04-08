import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(imdb_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ENTER_YOUR_API-KEY&language=en-US'.format(imdb_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = bollywood_1950_to_2019[bollywood_1950_to_2019['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        imdb_id = bollywood_1950_to_2019.iloc[i[0]].imdb_id
        #fetch poster from API
        recommended_movies_poster.append(fetch_poster(imdb_id))
        recommended_movies.append(bollywood_1950_to_2019.iloc[i[0]].original_title)
    return recommended_movies, recommended_movies_poster
 

bollywood_1950_to_2019 = pickle.load(open('./bollywood-movie-recommender-system/bollywood_1950_to_2019.pkl','rb'))
similarity = pickle.load(open('./bollywood-movie-recommender-system/similarity.pkl', 'rb'))
image_folder = './bollywood-movie-recommender-system/img/'


selected_movie_name = option = st.selectbox('How would you like to be contacted?',bollywood_1950_to_2019['original_title'].values)


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.write(names[0])

    with col2:
        st.image(posters[1])
        st.write(names[1])

    with col3:
        st.image(posters[2])
        st.write(names[2])

    with col4:
        st.image(posters[3])
        st.write(names[3])

    with col5:
        st.image(posters[4])
        st.write(names[4])
