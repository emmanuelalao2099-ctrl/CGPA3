
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title = "Student CGPA Calculator",
    page_icon = "🎓"   # windows + . to access the emoji collection page on your pc
    layout = "centered"
)

# Grading system
grade_points = {
    "A": 5,  # 70 - 100
    "B": 4,  # 60 - 69
    "C": 3,  # 50 - 59
    "D": 2,  # 45 - 49
    "E": 1,  # 40 - 44
    "F": 0,  # <40
}

# Application title
st.title("🎓 Student CGPA Calculator")

st.write("Calculate your CGPA using your course credit units and grades.")

st.info("This calculator uses a 5.00 grading scale.")

# Course input
st.subheader("Enter Course Details")

number_of_courses = st.number_input(
    "Number of courses",
    min_value = 1,
    max_value = 300,
    value = 5,
    step = 1
)

courses = []

for i in range(int(number_of_courses)):
    st.markdown(f"### Course {i + 1}")
    col1, col2, col3 = st.columns(3)

    with col1:
        course_code = st.text_input(
            "Course Code",
            key=f"code_{i}"
        )

    with col2:
        course_unit = st.number_input(
            "Credit Unit",
            min_value = 1,
            max_value = 10,
            value = 3,
            key = f"unit_{i}"
        )

     with col3:
        grade = st.selectbox(
            "Grade",
            option = ["A", "B", "C", "D", "E", "F"],
            key = f"grade_{i}"
        )

     courses.append({
         "Course Code": course_code,
         "Credit unit": credit_unit,
         "Grade": grade
     })

# Calculate button
if st.button("Calculate CGPA", type="primary"):

total_credit_units = 0
total_quality_points = 0

result = []

for course in courses:


    grade_point = grade_points[course[grade]]
    quality_point = (course["credit_unit"] * grade_point)


    total_credit_units += course["credit_unit"]
    total_quality_points += quality_point

    results.append({
        "Course Code": course["Course Code"],
        "Credit Unit": course["Credit Unit"],
        "Grade": course["Grade"],
        "Grade point": grade_point,
        "Quality Point": quality_point
    })


   cgpa = total_quality_points / total_credit_units

   # Display results
st.success("CGPA calculated successfully!")

st.subheader("Academic Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Units",
    total_credit_units
)

col2.metric(
    "Quality Points",
    total_quality_points
)

col3.metric(
    "CGPA",
    f"{cgpa:.2f} / 5.00"
)

# Display course table
st.subheader("Course Breakdown")

results_df = pd.DataFrame(results)

st.dataframe(
    results_df,
    use_container_width = True,
    hide_index = True
)

# Download results
csv = results_df.to_csv(index=False).encode("utf-a")

st.download_button(
    label="Download Result",
    data=csv,
    file_name="student_cgpa_result.csv",
    mime="text/csv"
)
