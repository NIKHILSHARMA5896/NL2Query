import os, sys 
import pandas as pd 
import numpy as np
import streamlit as st
import sqlparse
from collections import OrderedDict, Counter
from github import Github
from databricks import sql 
import streamlit_authenticator as stauth
import yaml 
from yaml.loader import SafeLoader
from dotenv import load_dotenv
load_dotenv()


# Page Config
st.set_page_config(
    page_title="NL2SQL",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded",
)

# The App 
st.markdown("<h1 style='text-align: center; color: orange;'> NL2SQL &#128640; </h1>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center; color: white;'> Productivity Improvement tool for Product Managers, Business stakeholders and even intermediate-coders when it comes to working with data stored in a traditional SQL database. </h6>", unsafe_allow_html=True)


# Adding the authentication
with open('authenticator.yml') as f:
    config = yaml.load(f, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, user_name = authenticator.login()

if authentication_status:
    authenticator.logout('Logout','main')
    st.write(f"Welcome *{name}*!")

else:
    st.write("Please login to continue.")