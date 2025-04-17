import pandas as pd
import os
import streamlit as st
user_name_list=[]
proj_list=[]
rate_list=[]
CSV_FILE="data_treat.csv"
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["User_Name", "Project Name","Rating"])
    df.to_csv(CSV_FILE, index=False)
name=st.text_input("Write down name here: ")
# if st.button("Enter Name"):
 


project=st.text_input("Write down project name here: ")



rating=st.number_input("Rate Hamza Work out of 10")
# if st.button("Enter Project Name"):
 

 
if st.button("Submit"):
 if name and project and rating:
  user_name_list.append(name)
  proj_list.append(project)
  rate_list.append(rating)

 
  new_data = pd.DataFrame([{
            "User_Name": user_name_list,
            "Project_Name": proj_list,
            'Rating':rate_list
            
        }])
  new_data.to_csv(CSV_FILE, mode='a', header=False, index=False)


with st.expander("Developer Work"):
    password_dev = st.text_input("Write down password here to check database:", type="password")
    if password_dev == 'hamza123qwe':
        data_df = pd.read_csv(CSV_FILE)
        st.dataframe(data_df)
    else:
        if password_dev:  # Only show warning if something is typed
            st.warning("Incorrect password!")

