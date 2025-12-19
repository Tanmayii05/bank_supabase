import streamlit as st
import pandas as pd
from supabase import create_client

#Supabase Configuration
SUPABASE_URL = "https://zryqpjnjjzrebrrshfck.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpyeXFwam5qanpyZWJycnNoZmNrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDUwNzksImV4cCI6MjA4MTYyMTA3OX0.P7o9TfnShmpKb-vPo0rfg0UCjthqyZvHvDxOA1RmLC0"

supabase=create_client(SUPABASE_URL, SUPABASE_KEY)

#Streamlit UI
st.title(" HDFC BANK (Supabase)")
#
menu=["REGISTER", "VIEW"]
choice=st.sidebar.selectbox ("Menu", menu)

#REGISTER
if choice=="REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("AGE", min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE", min_value=500)
    if st.button("Save"):
        supabase.table("users1").insert({
            "name": name,
            "age": age,
            "account": account,
            "balance":bal}).execute()
        st.success ("user added successfully")

#View Students
if choice == "VIEW":
    st.subheader("view users")
    data=supabase.table("users1").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)






    
