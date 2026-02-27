import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

next_assignment_id_number = 3

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

point = st.number_input("Points")

# Not in assignment  assignment_type2 = st.selectbox("Type", ["Homework", "Lab"])
 # Not in assignment  if assignment_type2 == "Other":
 # Not in assignment   assignment_type2 = st.text_input("Assignent Type")


# Not in assignment assignment_type3 = st.checkbox("Assignment Type")

# Not in assignment lab = st.checkbox("Lab")

with st.expander("Assignment Preview", expanded=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")


btn_save = st.button("Save", use_container_width=True, disabled=False) #we put it as false just to show that if you put true you can disable it

import time
import json
from pathlib import Path

json_path = Path("assignment.json")


if btn_save:
    with st.spinner("Saving the Assignment..."):
        time.sleep(5)
        if title == "":
            st.warning("Enter Assignment Title")
        else:
            #Add/Create New Assignment
            new_assignment_id = "HW_" + str(next_assignment_id_number)
            next_assignment_id_number += 1

            assignment.append(
                {
                    "id" : new_assignment_id,
                    "title" : title,
                    "description" : description,
                    "points" : point,
                    "type" : assignment_type

                }
            )

            #Recording the data into an actual file 
            #if json_path,exists():
            with json_path.open("w", encoding="utf-8") as f:
                json.dump(assignment, f)


            st.success("Assignment is recorded!")
            st.dataframe(assignment)

            # so now when I saved the streamlit assignment it will be recorded in the json file and then I can load it from the json file and show it in the dataframe it like generated that assignment.json file