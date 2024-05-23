# Import relevant libraries
import pandas as pd
import streamlit as st
import numpy as np
import pickle
import os
import joblib
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
    """
    This function checks if the provided username and password are valid.
    Replace this with your actual implementation.
    """
    # For demonstration purposes, we'll assume any username and password combination is valid
    return True

html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Heart Disease Risk Prediction</h1>
		</div>
		"""

# Avatar Image using a url
avatar1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWGkOUXueZp3UxSugbaG0yLeXeM-NtQEE_oFWmpqdzrQ&s"
avatar2 = "https://w7.pngwing.com/pngs/843/694/png-transparent-avatar-female-cartoon-avatar-purple-face-black-hair-thumbnail.png"

result_temp = """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 20px;">
        <h4 style="color: white; text-align: center;">Algorithm: {}</h4>
        <img src="https://w7.pngwing.com/pngs/843/694/png-transparent-avatar-female-cartoon-avatar-purple-face-black-hair-thumbnail.png" alt="Avatar" style="vertical-align: middle; float: left; width: 50px; height: 50px; border-radius: 50%; margin-right: 15px;">
        <p style="text-align: justify; color: white; margin-top: 10px;">{} % probability that the patient has heart disease</p>
    </div>
    """

result_temp2 = """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 20px;">
        <h4 style="color: white; text-align: center;">Algorithm: {}</h4>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWGkOUXueZp3UxSugbaG0yLeXeM-NtQEE_oFWmpqdzrQ&s" alt="Avatar" style="vertical-align: middle; float: left; width: 50px; height: 50px; border-radius: 50%; margin-right: 15px;">
        <p style="text-align: justify; color: white; margin-top: 10px;">{} % probability that the patient has heart disease</p>
    </div>
    """


prescriptive_message_temp = """
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">Recommended Lifestyle Modifications</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Adopt a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins</li>
		<li style="text-align:justify;color:black;padding:10px">Engage in regular physical activity, such as brisk walking, swimming, or cycling, for at least 30 minutes most days of the week</li>
		<li style="text-align:justify;color:black;padding:10px">Maintain a healthy body weight through a balanced diet and regular exercise</li>
		<li style="text-align:justify;color:black;padding:10px">Quit smoking and avoid secondhand smoke exposure</li>
		<li style="text-align:justify;color:black;padding:10px">Manage stress levels through relaxation techniques, such as meditation, yoga, or deep breathing exercises</li>
		<ul>
		<h3 style="text-align:justify;color:black;padding:10px">Medical Management</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Consult a cardiologist or healthcare professional for a comprehensive evaluation and personalized treatment plan</li>
		<li style="text-align:justify;color:black;padding:10px">Adhere to prescribed medications, such as cholesterol-lowering drugs, blood pressure medications, or anti-clotting agents, as recommended by your doctor</li>
		<li style="text-align:justify;color:black;padding:10px">Attend regular check-ups and follow-up appointments to monitor your heart health and adjust treatment as needed</li>
		<ul>
	</div>
	"""

descriptive_message_temp = """
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">What is Heart Disease?</h3>
		<p>Heart disease is a broad term that encompasses a variety of conditions affecting the heart and blood vessels. It includes disorders such as coronary artery disease, heart failure, arrhythmias, and heart valve problems. These conditions can have severe consequences if left untreated, including heart attacks, strokes, and other life-threatening complications.</p>
		<p>Coronary artery disease, the most common form of heart disease, is caused by a buildup of plaque in the arteries that supply blood to the heart muscle. This buildup can partially or completely block the flow of oxygen-rich blood, leading to angina (chest pain) or a heart attack.</p>
		<p>Heart failure occurs when the heart muscle is weakened and unable to pump blood effectively throughout the body. This can be caused by various factors, such as coronary artery disease, high blood pressure, or heart valve problems.</p>
		<p>Arrhythmias are abnormal heart rhythms that can cause the heart to beat too slowly (bradycardia), too quickly (tachycardia), or irregularly. These rhythms can be triggered by heart disease, electrolyte imbalances, or certain medications.</p>
		<p>Heart valve disorders involve the malfunctioning of one or more of the heart's four valves, which regulate blood flow through the heart. These disorders can be congenital (present at birth) or acquired later in life due to factors like age, infection, or heart disease.</p>
	</div>
	"""

def change_avatar(sex):
	if sex == "male":
		avatar_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWGkOUXueZp3UxSugbaG0yLeXeM-NtQEE_oFWmpqdzrQ&s'
	else:
		avatar_img = 'https://w7.pngwing.com/pngs/843/694/png-transparent-avatar-female-cartoon-avatar-purple-face-black-hair-thumbnail.png'
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

    if choice == "Home":
        # Home page content
        pass
    elif choice == "Login":
        # Login page content
        pass
    elif choice == "Sign up":
        # Sign up page content
        pass

    if choice == "Home":
        st.sidebar.markdown("**Heart Diesease Prediction ❤️**")
        st.sidebar.image('https://research.jgu.edu.in/wp-content/uploads/2023/12/heart.jpg', use_column_width=True)
        st.sidebar.image('https://siddharth7997.github.io/HeartDiseaseStudy/heart.gif', use_column_width=True)


        # CSS for styling
        st.markdown("""
    <style>
        /* Customize fonts and colors */
        body {
            font-family: Algerian, times new;
            color: #F8F8F2; /* Text color */
            background: url('https://research.jgu.edu.in/wp-content/uploads/2023/12/heart.jpg') no-repeat center center fixed; /* Background image */
            background-size: cover; /* Cover the entire background *
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        .header {
            background: linear-gradient(135deg, #FF5A5F, #FFC371); /* Gradient background color */
            color: #EDE342; /* Box text color */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .section-box {
            background: linear-gradient(135deg, #E493B3, #97359C); /* Gradient background color */
            color: #F8F8F2; /* Box text color */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 36px;
            font-weight: bold;
            margin: 0;
            color: #E1AFD1; /* Red header color */
        }
        p {
            color: #C5FF95; /* Red text color */
        }
    </style>
""", unsafe_allow_html=True)

        # Header section
        st.markdown("""
    <style>
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        .header {
            background-color: #bdb2ff; /* Background color */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Box shadow effect */
        }
        h1 {
            text-align: center;
            font-size: 48px;
            color: #d00000; /* Text color */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4); /* Text shadow effect */
        }
    </style>
    <div class="container">
        <div class="header">
            <h1>Heart Disease Assessment</h1>
        </div>
    </div>
""", unsafe_allow_html=True)


        # Introduction section
        st.markdown("""
    <div class="container">
        <h2 style="color: #FFEBB2;">Empower Your Heart Health</h2>
        <p style="color: #FFEBB2;">Discover Your Heart's Story</p>
        <p style="color: #FFEBB2;">Heart disease is a leading cause of mortality worldwide, affecting millions each year. The risks are real, from heart attacks to strokes, but knowledge is power. Our web app delves deep into your heart's health, analyzing factors like age, gender, cholesterol levels, and lifestyle choices to assess your risk. Armed with this knowledge, you can take proactive steps towards a healthier heart and a happier life.</p>
        <p style="color: #FFEBB2;">Take the first step on your heart health journey. Welcome to a world where your heart's health is in your hands.</p>
    </div>
""", unsafe_allow_html=True)


        st.markdown("""
    <div class="container section-box">
        <h2>Discover Your Heart's Story</h2>
        <p>Welcome to our Heart Disease Assessment app, where we believe every heartbeat tells a story. Our app harnesses the power of machine learning to analyze your health data and provide a personalized assessment of your heart disease risk.</p>
        <p>It considers factors like your age, gender, cholesterol levels, blood pressure, and exercise habits to generate a comprehensive risk score, giving you valuable insights into your heart health.</p>
        <h3>Using the App</h3>
        <p>To begin your heart health journey:</p>
        <ol>
            <li>Sign up for an account by clicking the arrow at the top left corner and selecting "Sign Up".</li>
            <li>After signing up, log in using your username and password.</li>
            <li>Once logged in, select "Early Heart Disease Diagnosis" from the dropdown menu.</li>
            <li>Fill out the form with your details completely and accurately.</li>
            <li>Click "Submit Details" and then "Predict" to receive your personalized assessment.</li>
        </ol>
        <p>Remember, your heart's health is in your hands. Start your journey to a healthier heart today!</p>
        <h4>Note</h4>
        <p>Please ensure you fill out the form completely to avoid errors in prediction. Your health is important to us, and we want to provide you with the most accurate assessment possible.</p>
    </div>
""", unsafe_allow_html=True)


    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password",type="password")
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pwd = generate_hashes(password)
            result = login_user(username,verify_hashes(password,hashed_pwd))
            if result:
                st.success("Welcome back {}".format(username))
                activity = st.selectbox("Choose The Action You Wish To Perform", submenu)
                if activity == "Information on Heart Disease":
                    # Define theme colors and font
                    primaryColor = "#FF6F3C"
                    backgroundColor = "#333333"
                    secondaryBackgroundColor = "#444444"
                    textColor = "#ffffff"
                    font = "Algerian"
                    # Custom CSS for improved aesthetics
                    custom_css = f"""
    <style>
        /* Main background color */
        .stApp {{
            background-color: {backgroundColor};
            color: {textColor};
            font-family: {font};
        }}

        /* Section background color */
        .css-1mpk29p {{
            background-color: {secondaryBackgroundColor};
            color: {textColor};
            font-family: {font};
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add box-shadow */
        }}

        /* Header color */
        .css-1k6enqb {{
            color: {primaryColor};
            font-size: 32px; /* Increase font size */
            font-weight: bold;
            margin-bottom: 15px; /* Increase margin */
        }}

        /* Subheader color */
        .css-1vrc75a {{
            color: {textColor};
            font-size: 22px; /* Increase font size */
            font-weight: bold;
            margin-bottom: 15px; /* Increase margin */
        }}

        /* Image border radius */
        .stImage {{
            border-radius: 10px;
            margin-bottom: 20px; /* Increase margin */
        }}

        /* Horizontal rule color */
        .horizontal-rule {{
            border-top: 2px solid {primaryColor};
            margin: 40px 0; /* Increase margin */
        }}

.heart {{
    position: relative;
    width: 80px;
    height: 70px;
    background: var(--primary-color); /* Use the variable here */
    border-radius: 50%;
    animation: pulse 2s infinite;
}}
    </style>
"""

                    # Header
                    st.title("Understanding Heart Disease: Causes, Symptoms, and Prevention")
                    st.markdown(custom_css, unsafe_allow_html=True)
                    # Introduction
                    st.header("Introduction:")
                    st.write(
                    "Heart disease continues to be a global health challenge, claiming millions of lives annually. "
                    "It encompasses a wide array of conditions that impact the heart's structure and function, hindering its ability to efficiently pump blood. "
                    "A deeper understanding of the root causes, common symptoms, and effective prevention strategies is imperative in tackling this pervasive health threat."
                        )
                    st.markdown("---")

                    # Causes
                    st.header("Causes:")

                    st.markdown(
    "Heart disease can develop due to various factors, including:\n"
    "1. **Lifestyle Choices:** Unhealthy habits such as smoking, poor diet, and lack of exercise can increase the risk.\n"
    "2. **Medical Conditions:** Conditions like high blood pressure, diabetes, and obesity can contribute.\n"
    "3. **Genetics:** Family history of heart disease can increase susceptibility.\n"
    "4. **Age and Gender:** Risk increases with age and differs between men and women.\n"
    "5. **Other Factors:** Stress, excessive alcohol consumption, and poor dental health can also play a role.\n"
)
                    st.markdown("---")


                    # Symptoms
                    st.header("Symptoms:")
                    st.markdown(
    "Symptoms of heart disease can vary depending on the specific condition but may include:\n"
    "1. **Chest Pain or Discomfort:** A common symptom, often described as pressure, squeezing, or fullness in the chest.\n"
    "2. **Shortness of Breath:** Difficulty breathing or feeling short of breath, especially with exertion.\n"
    "3. **Fatigue:** Feeling unusually tired or lacking in energy, even after rest.\n"
    "4. **Swelling:** Swelling in the legs, ankles, or abdomen due to fluid retention.\n"
    "5. **Irregular Heartbeat:** Heart palpitations, fluttering, or a racing sensation in the chest.\n"
)
                    st.markdown("---")

                    # Prevention
                    st.header("Prevention:")
                    st.markdown(
    "Preventing heart disease involves adopting a heart-healthy lifestyle and managing risk factors effectively. "
    "Here are some prevention strategies:\n"
    "1. **Healthy Diet:** Eat plenty of fruits, vegetables, whole grains, and lean proteins. Avoid processed foods and excessive sugar and salt.\n"
    "2. **Regular Exercise:** Aim for at least 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous exercise each week.\n"
    "3. **Maintain a Healthy Weight:** Keep your weight in check to reduce the risk of heart disease and other health problems.\n"
    "4. **Manage Stress:** Practice stress-reducing activities such as yoga, meditation, or deep breathing exercises.\n"
    "5. **Quit Smoking:** Smoking is a major risk factor for heart disease. Quitting can significantly reduce your risk.\n"
    "6. **Limit Alcohol:** Excessive alcohol consumption can increase the risk of heart disease. Limit intake to moderate levels.\n"
    "7. **Regular Health Check-ups:** Regular visits to your healthcare provider can help monitor your heart health and identify any issues early.\n"
)
                    st.markdown("---")


                    # Conclusion
                    st.header("Conclusion:")
                    st.write(
                        "Heart disease is a complex condition that requires a comprehensive approach to prevention and management. "
                        "By adopting a heart-healthy lifestyle and effectively managing risk factors, individuals can reduce their risk of heart disease and improve their overall heart health."
                    )

                    # Footer
                    # Footer
                    st.markdown(
    """
    <style>
        /* Style for the footer */
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #222222;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        <p>@Kishore Kumar_2024</p>
    </div>
    """,
    unsafe_allow_html=True
)
                    st.markdown("---")
                    st.write(
    "The information provided on this page is for educational purposes only and should not be considered medical advice. "
    "For personalized medical recommendations, please consult a healthcare professional."
)

                    
                # Early Heart Disease Diagnosis
                elif activity=="Early Heart Disease Diagnosis":
                    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://t3.ftcdn.net/jpg/02/30/65/32/240_F_230653294_5anAftMO11TB2Sy9IDR3MwLTacW22z4y.jpg");
        background-size: cover;
        background-position: center;
        color: white;
    }
    .css-1mpk29p {
        background-color: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(5px);
        border-radius: 10px;
        padding: 20px;
        animation: fade-in 1s ease;
    }
    @keyframes fade-in {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)
                    st.markdown("##### Please fill out your information to Know if you are at risk of an Heart Disease")
                    # User Input Form
                    form = st.form('data_form')
                    age = form.number_input("Enter Your Age", min_value=18, max_value=77)
                    sex = form.radio("Choose your Gender",["Male","Female"], index=None)
                    chtyp = ["Typical Angina"," Atypical Angina","Non-Anginal Pain"," Asymptomatic"]
                    ChestPainType = form.selectbox("Choose the Type of chest pain you experience", chtyp, index=None)
                    RestingBP = form.number_input("Enter Your Resting Blood Pressure (mmHg)", min_value=92, max_value=200)
                    Cholesterol = form.number_input("Enter Your Serum Cholesterol level (mm/dl)", min_value=85, max_value=603)
                    FastingBS = form.radio("Is your Fasting Blood sugar level > 120mg/dl",["Yes","No"], index=None)
                    RestingECG = form.selectbox("Select Resting Electrocardiogram Results", ["Normal","ST-T wave abnormality", "Left ventricular hypertrophy"], index=None)
                    MaxHR = form.number_input("Enter Your Maximum heart rate achieved", min_value=60, max_value=202)
                    ExerciseAngina = form.radio("Do you experience heart discomfort after an exercise", ["Yes","No"], index=None)
                    Oldpeak = form.number_input("Select ST Depression", min_value=0.0, max_value=6.0, step=0.1)
                    ST_Slope = form.selectbox("What is slope of the peak exercise ST segment",['Up sloping',"Flat","Down Slope"], index=None)                 
                    form.form_submit_button('Submit details')

                    # Use the data to create a dataframe
                    user_data = pd.DataFrame({
                        
                            "Age" : [age],
                            "Sex" :	[sex],
                            "ChestPainType"	: [ChestPainType],
                            "RestingBP"	: [RestingBP],
                            "Cholesterol" : [Cholesterol],
                            "FastingBS"	: [FastingBS],
                            "RestingECG" : [RestingECG],	
                            "MaxHR"	: [MaxHR],
                            "ExerciseAngina" : [ExerciseAngina],	
                            "Oldpeak"	: [Oldpeak],
                            "ST_Slope"	: [ST_Slope]
                        }
                    )

                    
                    st.markdown("### Confirm Your Details")
                    st.dataframe(user_data)
                    user_data["Sex"] = user_data["Sex"].map({"Male":"M", "Female":"F"})
                    user_data["ChestPainType"] = user_data["ChestPainType"].map({"Typical Angina":"TA"," Atypical Angina":"ATA","Non-Anginal Pain":"NAP"," Asymptomatic":"ASY"})
                    user_data["RestingECG"] = user_data["RestingECG"].map({"Normal":"Normal","ST-T wave abnormality":"ST", "Left ventricular hypertrophy":"LVH"})
                    user_data["ExerciseAngina"] = user_data["ExerciseAngina"].map({"No":"N","Yes":"Y"})
                    user_data["ST_Slope"] = user_data["ST_Slope"].map({'Up sloping':'Up',"Flat":'Flat',"Down Slope":"Down"})
                    
                    # Import Model
                    model = joblib.load("model.pkl")
                    # Import Preprocessor
                    preprocessor = joblib.load("preprocessor.pkl")
                    if st.button("Get Prediction"):
                         # Preprocess user data
                        userdata_scaled = preprocessor.transform(user_data)
                        # Get Prediction
                        prediction = model.predict(userdata_scaled)
                        predict_prob = model.predict_proba(userdata_scaled)[0][1] * 100
                        if prediction == 1:
                            st.warning(f"You have a {predict_prob:.2f}% chance of having heart disease.")
                            st.markdown(prescriptive_message_temp,unsafe_allow_html=True)
                                
                
                        else:
                            st.success("You are not at Risk of a Heart Disease")
                        

            else:
                st.warning("Incorrect Username/Password")


    elif choice=="Sign up":
        new_user = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password", type="password")
        confirm_password = st.sidebar.text_input("Confirm Password", type="password")
        
        if new_password == confirm_password:
            st.sidebar.success("Password Confirm")
        else:
            st.sidebar.warning("Password is not the same")
        if st.sidebar.button("Submit"):
            create_usertable()
            hashed_new_password = generate_hashes(new_password)
            add_userdata(new_user, hashed_new_password)
            st.success(f"Congratulations! {new_user}, You have successfully created a new account")
            st.info("Log In to Get Started")



    
if __name__ == '__main__':
	main()
