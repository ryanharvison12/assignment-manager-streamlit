# He did a bunch of copy and pastign from app_day2.py that I didn't get 

import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

next_assignment_id_number = 3



tab1, tab2, tab3 = st.tabs(["View Assignment", "Add New Assignments", "Update An Assignment"])


with tab1:
    #st.info("This tab is under development!")
    option = st.radio("View/Search", ["View", "Search"), horizontal=True)

    if option == "View":
        st.dataframe(assignments)


    else:
        search_title = st.selectbox("Assignment Titles", [])
    st.dataframe(assignments)
with tab2:
