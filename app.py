# Import relevant libraries
import pandas as pd
import streamlit as st
import numpy as np
import hashlib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# Additional functions
def create_usertable():
    pass

def add_userdata(username, password):
    pass

def login_user(username, password):
    return True

# CSS for glassmorphism effects
glassmorphism_css = """
<style>
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #F8F8F2;
    font-family: 'Arial', sans-serif;
}
.container {
    backdrop-filter: blur(10px);
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin: 20px;
}
.header, .section-box {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
    text-align: center;
}
.header h1, .section-box h2 {
    color: #FF6F3C;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
}
.header p, .section-box p {
    color: #C5FF95;
}
.section-box ul {
    list-style-type: none;
    padding: 0;
}
.section-box li {
    background: rgba(255, 255, 255, 0.1);
    padding: 10px;
    margin: 5px 0;
    border-radius: 5px;
}
</style>
"""

# Avatar Image using a URL
avatar1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWGkOUXueZp3UxSugbaG0yLeXeM-NtQEE_oFWmpqdzrQ&s"
avatar2 = "https://w7.pngwing.com/pngs/843/694/png-transparent-avatar-female-cartoon-avatar-purple-face-black-hair-thumbnail.png"

result_temp = """
    <div class="container">
        <h4>Algorithm: {}</h4>
        <img src="{}" alt="Avatar" style="vertical-align: middle; float: left; width: 50px; height: 50px; border-radius: 50%; margin-right: 15px;">
        <p style="text-align: justify;">{} % probability that the patient has heart disease</p>
    </div>
    """

prescriptive_message_temp = """
    <div class="container">
        <h3>Recommended Lifestyle Modifications</h3>
        <ul>
            <li>Adopt a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins</li>
            <li>Engage in regular physical activity, such as brisk walking, swimming, or cycling, for at least 30 minutes most days of the week</li>
            <li>Maintain a healthy body weight through a balanced diet and regular exercise</li>
            <li>Quit smoking and avoid secondhand smoke exposure</li>
            <li>Manage stress levels through relaxation techniques, such as meditation, yoga, or deep breathing exercises</li>
        </ul>
        <h3>Medical Management</h3>
        <ul>
            <li>Consult a cardiologist or healthcare professional for a comprehensive evaluation and personalized treatment plan</li>
            <li>Adhere to prescribed medications, such as cholesterol-lowering drugs, blood pressure medications, or anti-clotting agents, as recommended by your doctor</li>
            <li>Attend regular check-ups and follow-up appointments to monitor your heart health and adjust treatment as needed</li>
        </ul>
    </div>
    """

descriptive_message_temp = """
    <div class="container">
        <h3>What is Heart Disease?</h3>
        <p>Heart disease is a broad term that encompasses a variety of conditions affecting the heart and blood vessels. It includes disorders such as coronary artery disease, heart failure, arrhythmias, and heart valve problems. These conditions can have severe consequences if left untreated, including heart attacks, strokes, and other life-threatening complications.</p>
        <p>Coronary artery disease, the most common form of heart disease, is caused by a buildup of plaque in the arteries that supply blood to the heart muscle. This buildup can partially or completely block the flow of oxygen-rich blood, leading to angina (chest pain) or a heart attack.</p>
        <p>Heart failure occurs when the heart muscle is weakened and unable to pump blood effectively throughout the body. This can be caused by various factors, such as coronary artery disease, high blood pressure, or heart valve problems.</p>
        <p>Arrhythmias are abnormal heart rhythms that can cause the heart to beat too slowly (bradycardia), too quickly (tachycardia), or irregularly. These rhythms can be triggered by heart disease, electrolyte imbalances, or certain medications.</p>
        <p>Heart valve disorders involve the malfunctioning of one or more of the heart's four valves, which regulate blood flow through the heart. These disorders can be congenital (present at birth) or acquired later in life due to factors like age, infection, or heart disease.</p>
    </div>
    """

def change_avatar(sex):
    if sex == "male":
        avatar_img = avatar1
    else:
        avatar_img = avatar2
    return avatar_img

# Password 
def generate_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def verify_hashes(password, hashed_text):
    if generate_hashes(password) == hashed_text:
        return hashed_text
    return False

def main():
    """Heart Disease Assessment"""
    menu = ["Home", "Login", "Sign up"]
    submenu = ["Information on Heart Disease", "Early Heart Disease Diagnosis"]
    choice = st.sidebar.selectbox("Menu", menu)

    st.markdown(glassmorphism_css, unsafe_allow_html=True)

    if choice == "Home":
        st.sidebar.markdown("**Heart Disease Prediction ❤️**")
        st.sidebar.image('https://research.jgu.edu.in/wp-content/uploads/2023/12/heart.jpg', use_column_width=True)
        st.sidebar.image('https://siddharth7997.github.io/HeartDiseaseStudy/heart.gif', use_column_width=True)

        # Header section
        st.markdown("""
            <div class="header">
                <h1>Heart Disease Assessment</h1>
                <p>Empower Your Heart Health</p>
                <p>Discover Your Heart's Story</p>
                <p>Heart disease is a leading cause of mortality worldwide, affecting millions each year. The risks are real, from heart attacks to strokes, but knowledge is power. Our web app delves deep into your heart's health, analyzing factors like age, gender, cholesterol levels, and lifestyle choices to assess your risk. Armed with this knowledge, you can take proactive steps towards a healthier heart and a happier life.</p>
                <p>Take the first step on your heart health journey. Welcome to a world where your heart's health is in your hands.</p>
            </div>
        """, unsafe_allow_html=True)

    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pwd = generate_hashes(password)
            result = login_user(username, verify_hashes(password, hashed_pwd))
            if result:
                st.success(f"Welcome back {username}")
                activity = st.selectbox("Choose The Action You Wish To Perform", submenu)
                if activity == "Information on Heart Disease":
                    st.title("Understanding Heart Disease: Causes, Symptoms, and Prevention")

                    # Introduction
                    st.markdown("""
                        <div class="section-box">
                            <h2>Introduction:</h2>
                            <p>Heart disease continues to be a global health challenge, claiming millions of lives annually. It encompasses a wide array of conditions that impact the heart's structure and function, hindering its ability to efficiently pump blood. A deeper understanding of the root causes, common symptoms, and effective prevention strategies is imperative in tackling this pervasive health threat.</p>
                        </div>
                    """, unsafe_allow_html=True)

                    # Causes
                    st.markdown("""
                        <div class="section-box">
                            <h2>Causes:</h2>
                            <p>Heart disease can develop due to various factors, including:</p>
                            <ul>
                                <li><strong>Lifestyle Choices:</strong> Unhealthy habits such as smoking, poor diet, and lack of exercise can increase the risk.</li>
                                <li><strong>Medical Conditions:</strong> Conditions like high blood pressure, diabetes, and obesity can contribute.</li>
                                <li><strong>Genetics:</strong> Family history of heart disease can increase susceptibility.</li>
                                <li><strong>Age and Gender:</strong> Advancing age and being male are significant risk factors.</li>
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)

                    # Symptoms
                    st.markdown("""
                        <div class="section-box">
                            <h2>Symptoms:</h2>
                            <p>Common symptoms of heart disease include:</p>
                            <ul>
                                <li>Chest pain or discomfort</li>
                                <li>Shortness of breath</li>
                                <li>Fatigue</li>
                                <li>Irregular heartbeats</li>
                                <li>Swelling in the legs, ankles, or feet</li>
                                <li>Dizziness or lightheadedness</li>
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)

                    # Prevention
                    st.markdown("""
                        <div class="section-box">
                            <h2>Prevention:</h2>
                            <p>Preventing heart disease involves adopting a healthy lifestyle and managing risk factors:</p>
                            <ul>
                                <li>Maintain a balanced diet</li>
                                <li>Exercise regularly</li>
                                <li>Avoid smoking and limit alcohol intake</li>
                                <li>Manage stress</li>
                                <li>Regular health check-ups</li>
                                <li>Take prescribed medications as directed</li>
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)

                elif activity == "Early Heart Disease Diagnosis":
                    st.title("Early Heart Disease Diagnosis")

                    age = st.number_input("Enter Your Age", 29, 100)
                    sex = st.radio("Select Your Gender", ["Male", "Female"])
                    cp = st.radio("Chest Pain Type", ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
                    trestbps = st.number_input("Resting Blood Pressure", 50, 200)
                    chol = st.number_input("Serum Cholesterol in mg/dl", 50, 200)
                    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
                    restecg = st.radio("Resting Electrocardiographic Results", ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"])
                    thalach = st.number_input("Maximum Heart Rate Achieved", 50, 200)
                    exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
                    oldpeak = st.number_input("Oldpeak")
                    slope = st.radio("Heart Rate Slope", ["Upsloping", "Flat", "Downsloping"])
                    ca = st.radio("Number of Major Vessels Colored by Fluoroscopy", ["0", "1", "2", "3"])
                    thal = st.radio("Thal", ["Normal", "Fixed Defect", "Reversable Defect"])

                    # Transform and encode features
                    if st.button("Analyze"):
                        user_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
                        user_data_encoded = pd.DataFrame(user_data, columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"])

                        user_data_encoded['sex'] = user_data_encoded['sex'].map({"Male": 1, "Female": 0})
                        user_data_encoded['cp'] = user_data_encoded['cp'].map({"Typical angina": 0, "Atypical angina": 1, "Non-anginal pain": 2, "Asymptomatic": 3})
                        user_data_encoded['fbs'] = user_data_encoded['fbs'].map({"Yes": 1, "No": 0})
                        user_data_encoded['restecg'] = user_data_encoded['restecg'].map({"Normal": 0, "Having ST-T wave abnormality": 1, "Showing probable or definite left ventricular hypertrophy": 2})
                        user_data_encoded['exang'] = user_data_encoded['exang'].map({"Yes": 1, "No": 0})
                        user_data_encoded['slope'] = user_data_encoded['slope'].map({"Upsloping": 0, "Flat": 1, "Downsloping": 2})
                        user_data_encoded['thal'] = user_data_encoded['thal'].map({"Normal": 0, "Fixed Defect": 1, "Reversable Defect": 2})

                        new_features = user_data_encoded[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']].values

                        # Load the model and make prediction
                        rf_model = RandomForestClassifier()
                        rf_model.fit(new_features, np.random.randint(0, 2, size=new_features.shape[0]))  # Dummy training for demonstration
                        prediction = rf_model.predict(new_features)

                        if prediction[0] == 1:
                            st.markdown(result_temp.format("Random Forest", change_avatar(sex.lower()), 95), unsafe_allow_html=True)
                            st.markdown(prescriptive_message_temp, unsafe_allow_html=True)
                        else:
                            st.markdown(result_temp.format("Random Forest", change_avatar(sex.lower()), 5), unsafe_allow_html=True)
                            st.markdown(descriptive_message_temp, unsafe_allow_html=True)
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "Sign up":
        new_user = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.checkbox("Sign up"):
            create_usertable()
            add_userdata(new_user, generate_hashes(new_password))
            st.success("You have successfully created a new account")
            st.info("Go to the login menu to login")

if __name__ == '__main__':
    main()
