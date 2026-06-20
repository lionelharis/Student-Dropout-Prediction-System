import streamlit as st
import pickle
import numpy as np

# ==========================
# Load Model
# ==========================
model = pickle.load(open("decision_tree.pkl", "rb"))

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Student Dropout Prediction System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Dropout Prediction System")
st.markdown(
    "Predict whether a student is at risk of dropping out."
)

st.divider()

# ==========================
# Student Information
# ==========================
st.subheader("Student Information")

age = st.number_input(
    "Age at Enrollment",
    min_value=15,
    max_value=80,
    value=18
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)
gender = 1 if gender == "Male" else 0

debtor = st.selectbox(
    "Is the Student a Debtor?",
    ["No", "Yes"]
)
debtor = 1 if debtor == "Yes" else 0

fees = st.selectbox(
    "Tuition Fees Up To Date?",
    ["Yes", "No"]
)
fees = 1 if fees == "Yes" else 0

scholarship = st.selectbox(
    "Scholarship Holder?",
    ["No", "Yes"]
)
scholarship = 1 if scholarship == "Yes" else 0

st.divider()

# ==========================
# Academic Information
# ==========================
st.subheader("Academic Performance")

first_approved = st.number_input(
    "1st Semester Approved Subjects",
    min_value=0,
    max_value=20,
    value=0
)

first_grade = st.number_input(
    "1st Semester Grade",
    min_value=0.0,
    max_value=20.0,
    value=10.0,
    step=0.1
)

second_approved = st.number_input(
    "2nd Semester Approved Subjects",
    min_value=0,
    max_value=20,
    value=0
)

second_grade = st.number_input(
    "2nd Semester Grade",
    min_value=0.0,
    max_value=20.0,
    value=10.0,
    step=0.1
)

st.caption("Grades are on a scale of 0 to 20.")

# ==========================
# Risk Warnings
# ==========================
risk_count = 0

if first_grade < 5:
    st.warning("⚠️ Very low 1st semester grade.")
    risk_count += 1

if second_grade < 5:
    st.warning("⚠️ Very low 2nd semester grade.")
    risk_count += 1

if first_approved < 2:
    st.warning("⚠️ Very few subjects passed in 1st semester.")
    risk_count += 1

if second_approved < 2:
    st.warning("⚠️ Very few subjects passed in 2nd semester.")
    risk_count += 1

if debtor == 1:
    st.warning("⚠️ Student has outstanding debt.")
    risk_count += 1

if fees == 0:
    st.warning("⚠️ Tuition fees are not up to date.")
    risk_count += 1

if risk_count >= 3:
    st.error("🚨 Multiple risk factors detected.")

st.divider()

# ==========================
# Prediction
# ==========================
if st.button("Predict Dropout Risk"):

    data = np.array([[
        age,
        debtor,
        fees,
        scholarship,
        gender,
        first_approved,
        first_grade,
        second_approved,
        second_grade
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:

        st.error("⚠️ High Dropout Risk")

        st.markdown("""
        ### Recommended Actions
        ✅ Academic Counseling  
        ✅ Financial Assistance  
        ✅ Mentoring Program  
        ✅ Continuous Monitoring  
        """)

    else:

        st.success("✅ Low Dropout Risk")
        st.balloons()