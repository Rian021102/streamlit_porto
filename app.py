import streamlit as st

# title
st.title("Welcome to my portfolio website!")

st.markdown("This website curates projects that best showcase my skills in end-to-end machine learning and data science projects, including creating pipelines (data collection, data cleaning, data analysis), model building, and deployment as a final product.")

# add a divider line
st.markdown("---")

st.header("Projects: ")

# Divide the main columns into two sub-columns for each project
col1, col2, col3 = st.columns(3)

# Project 1
with col1:
    st.image("images/agHMSaj-e1611383647846.jpg", use_column_width=True)
    st.subheader("Project: Anime Recommendation System Using SVD")
    st.markdown("Anime recommender system utilizing Singular Value Decomposition (SVD) technique. The recommendation system is built using the Surprise library, where it is trained based on user ratings. The model then predicts the rating for each unseen item, and the recommendations are sorted from the highest to lowest (top 10) predicted ratings for each user. The model is then deployed using HuggingFace Spaces.")
    st.markdown("[GitHub](https://github.com/Rian021102/anime-recommender-using-svd)")
    st.markdown("[Demo](https://huggingface.co/spaces/Rianknow/anime-rec)")

# Project 2
with col2:
    st.image('images/download.jpeg', use_column_width=True)
    st.subheader("Project: NLP Identification of Sarcastic Headlines")
    st.markdown("Natural Language Processing (NLP) project to identify sarcastic headlines. This projects utilizes NLP technique in identifying sarcasm in headlines. Built using Tensorflow framework and it's deployed using Streamlit cloud, where the data is being streamed from Hugging Face datasets")
    st.markdown("[GitHub](https://github.com/Rian021102/nlp_in_sarcasm_detection)")
    st.markdown("[Demo](https://detectingsarcasm.streamlit.app/)")

with col3:
    st.image('images/pollution.jpeg')
    st.subheader("Project: Air Pollution Prediction")
    st.markdown("This project is an initiative, after the recent air pollution crisis in Jakarta, to predict the air pollution level in Jakarta. The data is taken from Jakarta goverment website that provides reading from stations in Jakarta. This initiative is to showcase Machine Learning Implementation that can predict the status of the pollution real time (unfortunately I have no access to realtime sensor), and prediction can be shared to the public.")
    st.markdown("[GitHub](https://github.com/Rian021102/jakarta-ispu)")
    st.markdown("[Demo](hhttps://huggingface.co/spaces/Rianknow/air-quality)")
# Add sidebar that automatically opens when the app is run
st.sidebar.header("About Me")

# Add a photo
st.sidebar.image("images/IMG_1798.jpg", width=250)

# Add markdown text
st.sidebar.markdown("I am Rian Rachmanto, a data scientist and machine learning engineer with a background in the energy sector. This portfolio website is a showcase of my projects and highlights my expertise in developing comprehensive end-to-end machine learning solutions, including deployment.")

# Add divider line below the text
st.sidebar.markdown("---")

# Add subheader
st.sidebar.subheader("Skills")

# Add skills
st.sidebar.text("SQL")
st.sidebar.progress(0.9)
st.sidebar.text("Python")
st.sidebar.progress(0.9)
st.sidebar.text("Tensorflow & Keras")
st.sidebar.progress(0.8)
st.sidebar.text("Pytorch")
st.sidebar.progress(0.7)
st.sidebar.text("Cloud Deployment")
st.sidebar.progress(0.7)
st.sidebar.text("Docker")
st.sidebar.progress(0.8)
st.sidebar.text("End-to-End Machine Learning")
st.sidebar.progress(0.9)

# Add divider line below the text
st.sidebar.markdown("---")

# Add subheader
st.sidebar.subheader("Let's Connect!")

# Divide sidebar into two columns
col1, col2 = st.sidebar.columns(2)

# Add LinkedIn image and link
col1.image("images/linkedin-icon-1024x1024-net2o24e.png", width=50)
col1.markdown("[LinkedIn](https://www.linkedin.com/in/rian-rachmanto/)")

# Add GitHub image and link
col2.image("images/GitHub-Mark.png", width=50)
col2.markdown("[GitHub](https://github.com/Rian021102)")
