import pickle 
import streamlit as st
import requests
import os



def fetch_poster(movie_id):
    url= f'http://api.themoviedb.org/3/movie/{movie_id}?api_key=91b9c4e47e9287767cfd7906fef7669e&language=en-US'
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = 'http://image.tmdb.org/t/p/w500' + poster_path
    return full_path




def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key =lambda x: x[1])
    movie_names = []
    movie_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_poster.append(fetch_poster(movie_id))
        movie_names.append(movies.iloc[i[0]].title)
    return movie_names,movie_poster
st.header("Movie Recommendation System using Machine Learning")


cur_dir = os.path.dirname(__file__)
file_path = os.path.join(cur_dir,"saved_model","movie_list.pkl")

file_path1 = os.path.join(cur_dir,"saved_model","similarity.pkl.gz")

def load(file):
    with open(file,'rb') as f:
        return pickle.load(f)
    

movies = load(file_path)
similarity = load(file_path1)

movie_list = movies['title'].values



selected = st.selectbox(
    'Type or select a movie to get the recommendatinon ',
    movie_list
)


if st.button('recommendation'):
    recommendation_movies_name,recommended_movies_poster = recommend(selected)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendation_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommendation_movies_name[1])
        st.image(recommended_movies_poster[1])


    with col3:
        st.text(recommendation_movies_name[2])
        st.image(recommended_movies_poster[2])



    with col4:
        st.text(recommendation_movies_name[3])
        st.image(recommended_movies_poster[3])


    with col5:
        st.text(recommendation_movies_name[4])
        st.image(recommended_movies_poster[4])

