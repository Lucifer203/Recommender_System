import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))


st.header("Movie Recommender System")

select_value = st.selectbox("Select movie from dropdown.",movies['title'].values)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=f03372edea164cef3d983c8dc7e0f858&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    index = movies[movies["title"]==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key= lambda vector : vector[1])
    recommend_movies =[]
    recommend_poster=[]
    for i in distance[1:6]:
        # print(movies.iloc[i[0]].title)
        movies_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id=movies_id))
    return recommend_movies,recommend_poster

if st.button("Show Recommend"):
    movie_rec,movies_rec_poster = recommend(select_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_rec[0])
        st.image(movies_rec_poster[0])
    with col2:
        st.text(movie_rec[1])
        st.image(movies_rec_poster[1])

    with col3:
        st.text(movie_rec[2])
        st.image(movies_rec_poster[2])

    with col4:
        st.text(movie_rec[3])
        st.image(movies_rec_poster[3])

    with col5:
        st.text(movie_rec[4])
        st.image(movies_rec_poster[4])


