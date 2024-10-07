import streamlit as st
import streamlit_authenticator as stauth
from menu import menu
import yaml
from yaml.loader import SafeLoader
from streamlit_authenticator.utilities.exceptions import (LoginError)

from utils.func import hide_header_icons 

st.set_page_config(page_title="Report")

hide_header_icons()

with open('conifg.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Load secrets
usernames = st.secrets["credentials"]["usernames"]
passwords = st.secrets["credentials"]["passwords"]
names = st.secrets["credentials"]["names"]
logged_in = st.secrets["credentials"]["logged_in"]

# Create a dictionary of credentials
credentials = {
    "usernames": {
        usernames[i]: {
            "name": names[i],
            "password": passwords[i],
            "logged_in": logged_in[i]
        } for i in range(len(usernames))
    }
}

# Initialize authenticator
authenticator = stauth.Authenticate(
    credentials, 
    config['cookie']['name'],   
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

print(config['cookie']['name'])

try:
    authenticator.login()
except LoginError as e:
    st.error(e)

if st.session_state["authentication_status"]:
    st.session_state.authenticator = authenticator
    menu(True) 
    st.switch_page("pages/Home.py")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")

with open('conifg.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)
