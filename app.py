import streamlit as st
import joblib
import numpy as np

#==================================================================================================================

st.set_page_config(
    page_title = "College Adimission Prediction! ",
    page_icon = "🎓"
)

#===================================================================================================================

st.image("college.webp")
st.title("🎓College Adimission Prediction")
st.write("Hey!🖐 Here you can get the probability of your admission in the college, by giving a small infomation.")
st.markdown("---")

#===================================================================================================================

st.sidebar.title("🎓College Admission Prediction..")
st.sidebar.image("admission.jpg")
st.sidebar.markdown("---")
st.sidebar.write("It a Machine Learning based app build using the Linear Regression Model, used to predict the probability of your admission by getting the following information :")
st.sidebar.markdown("- Age")
st.sidebar.markdown("- Gender")
st.sidebar.markdown("- Category")
st.sidebar.markdown("- State")
st.sidebar.markdown("- Preferred Stream")
st.sidebar.markdown("- Entrance Exam")
st.sidebar.markdown("- Entrance Score")
st.sidebar.markdown("- Board Percentage")
st.sidebar.markdown("- Extra_Curricular Score")
st.sidebar.markdown("---")

st.sidebar.write("**Made By : Harshita Gupta**")

#====================================================================================================================

model = joblib.load("admission_prediction_model (1).pkl")

input_names = ["age", "gender", "category", "state", "preferred_stream", "entrance_exam", "entrance_score", "board_percentage",
                "extracurricular_score"]


age_values = st.number_input("Age", min_value = 14, max_value = 100)

gender_dict = {
    "other" : 0,
    "male"  : 1,
    "female": 2   
}
gender = st.selectbox("Choose Gender", gender_dict.keys())
gender_values = gender_dict[gender]

category_dict = {
    "st"      : 0,
    "obc"     : 1,
    "sc"      : 2,
    "general" : 3,
    "ews"     : 5
}
category = st.selectbox("Choose Category", category_dict.keys())
category_values = category_dict[category]

state_dict = {
        "rajasthan"            : 0,
        "karnataka"            : 1,
        "gujarat"              : 2,
        "himachal pradesh"     : 3,
        "assam"                : 4,
        "punjab"               : 5,
        "chhattisgarh"         : 6,
        "uttar pradesh"        : 7,
        "meghalaya"            : 8,
        "tamil nadu"           : 9,
        "maharashtra"          : 10,
        "nagaland"             : 11,
        "arunachal pradesh"    : 12,
        "telangana"            : 13,
        "jharkhand"            : 14,
        "mizoram"              : 15,
        "odisha"               : 16,
        "bihar"                : 17,
        "sikkim"               : 18,
        "andhra pradesh"       : 19,
        "tripura"              : 20,
        "manipur"              : 21,
        "madhya pradesh"       : 22,
        "haryana"              : 23,
        "goa"                  : 24,
        "kerala"               : 25
}
state = st.selectbox("Choose State", state_dict.keys())
state_values = state_dict[state]

preferred_stream_dict = {
        
        "management "              : 0,
        "arts"                     : 1,
        "nursing"                  : 2,
        "architecture"             : 3,
        "agriculture"              : 4,
        "computer applications"    : 5,
        "commerce"                 : 6,
        "engineering"              : 7,
        "science"                  : 8,
        "law"                      : 9,
        "medical"                  : 10,
        "pharmacy"                 : 11
}
preferred_stream = st.selectbox("Choose Stream", preferred_stream_dict.keys())
preferred_stream_values = preferred_stream_dict[preferred_stream]

entrance_exam_dict = {
   
        "none"    : 0,
        "cet"     : 1,
        "neet"    : 2,
        "jee"     : 3
}
entrance_exam = st.selectbox("Choose Entrance Exam ", entrance_exam_dict.keys())
entrance_exam_values = entrance_exam_dict[entrance_exam]

entrance_score_values = st.number_input("Entrance Score", min_value = 0, max_value = 315)
board_percentage_values = st.number_input("Board Percentage", min_value = 50.44, max_value = 99.53)
extracurricular_score_values = st.number_input("Extra_Curricular Score", min_value = 0 , max_value = 10)

inputs = [age_values, gender_values, category_values, state_values, preferred_stream_values, entrance_exam_values, 
            entrance_score_values, board_percentage_values, extracurricular_score_values ]

inputs = np.array(inputs).reshape(1, -1)

if st.button("Predict"):
    output = model.predict(inputs)
    st.success((f"Admission Probabilty : {output[0] * 100}"))

    prob = output[0] * 100
    
    if prob < 50:
        st.warning("There is no chance of your admission 😞")
    elif 50 <= prob < 60:
        st.info("There are moderate chances that you get admission 🙂")
    elif 60 <= prob < 70:
        st.info("There are high chances that you get admission 😄")
    else:  # prob >= 70
        st.success("Very high chances of admission! 🎉")



