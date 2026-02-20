import streamlit as st

st.title("Course Management")
st.header("Course Management Dashboard")
st.caption("MISY350")
st.divider()

# Step 2 Define Assignment List (Data Continuity)
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

#3. Step 3: Add New Assignment Section (Inputs & Layouts)
st.subheader("Add New Assignment")
with st.container(border=True):
    col1,col2 = st.columns([2,1])

    with col1:
        with st.container(border=True):
            st.markdown("### Assignment Details")
            title = st.text_input("Assignment title", placeholder="homework")
            description = st.text_input("Assignment Description")
            points = st.number_input("Points")
    with col2:
        st.markdown("**Time and Type**")
        due_date = st.date_input("Due Date")
        type = st.radio("type", ["Homework", "Lab"])
