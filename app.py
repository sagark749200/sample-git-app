import streamlit as st
from click import option

st.title('CampusX')

col1, col2 = st.columns(2)

with col1:
    st.image('screenshot1.jpg')

with col2:
    st.write("""As a Data Science YouTuber with over 380K+ subscribers, I am passionate about teaching others how to master Machine Learning, Deep Learning, Natural Language Processing, Computer Vision and Data Analysis. With over 100 repositories on GitHub, I am committed to sharing my knowledge and experience in these areas. My repositories include a wide range of projects, from simple examples to complex applications, all designed to help learners of all levels. With over 6.5k followers on GitHub, I am constantly engaged with the community, sharing insights and responding to questions. If you are interested in Data Science and looking to improve your skills, be sure to check out my repositories and YouTube channel.""")

st.header('course offered')
st.subheader('Data Science and machine learning')
st.subheader('Data Analysis')
st.subheader('Python')
st.subheader('SQL')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- home
- about
- career
- contact
- login
""")

st.sidebar.selectbox('Select one',['teacher','student'])
btn = st.sidebar.button('select')

if btn:
    st.title('hello' + option)
