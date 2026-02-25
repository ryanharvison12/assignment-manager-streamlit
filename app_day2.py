import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

st.divider()

# load assignments 
assignment = [
    {
        "id": "HW1",
        "title": "Introduction to Database",
        "description": "basics of database design",
        "points": 100,
        "type": "homework"
    },
    {
        "id": "HW2",
        "title": "Normalization",
        "description": "Normalize the table designs",
        "points": 100,
        "type": "lab"
    }
]

# Add New Assignment
st.markdown("# Add New Assignment")

# input
title = st.text_input("Title", placeholder="ex. Homework 1", help="This is the name of the assignment")

description = st.text_area("Description", placeholder="ex. database design...")
due_date = st.date_input("Due Date")
assignment_type = st.radio("Type", ["Homework", "Lab"])
# Not in assignment  assignment_type2 = st.selectbox("Type", ["Homework", "Lab"])
 # Not in assignment  if assignment_type2 == "Other":
 # Not in assignment   assignment_type2 = st.text_input("Assignent Type")


# Not in assignment assignment_type3 = st.checkbox("Assignment Type")

# Not in assignment lab = st.checkbox("Lab")

with st.expander("Assignment Preview", expanded=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")

btn_save = st.button("Save", width="stretch")
if btn_save:
    st.warning("Working on it!")