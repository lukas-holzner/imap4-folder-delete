#!/usr/bin/env python

import streamlit as st
import imaplib

def connect_to_server(host, user, password):
    mail = imaplib.IMAP4_SSL(host)
    mail.login(user, password)
    return mail

def fetch_folders(mail):
    response, folder_list = mail.list()
    if response == 'OK':
        return [folder.split()[-1].decode() for folder in folder_list]
    else:
        return []

def delete_folders(mail, folders):
    for folder in folders:
        mail.delete(folder)

# Streamlit app
st.title('IMAP Mailbox Manager')

# User inputs for IMAP server connection
if 'host' not in st.session_state:
    st.session_state.host = ''
if 'user' not in st.session_state:
    st.session_state.user = ''
if 'password' not in st.session_state:
    st.session_state.password = ''

st.session_state.host = st.text_input('Host', value=st.session_state.host)
st.session_state.user = st.text_input('Username', value=st.session_state.user)
st.session_state.password = st.text_input('Password', value=st.session_state.password, type='password')

# Initialize session state
if 'mail' not in st.session_state:
    st.session_state.mail = None

if st.button('Connect'):
    st.session_state.mail = connect_to_server(st.session_state.host, st.session_state.user, st.session_state.password)

if st.session_state.mail:
    folders = fetch_folders(st.session_state.mail)
    selected_folders = st.multiselect('Select folders to delete', folders)

    if st.button('Delete Selected Folders'):
        delete_folders(st.session_state.mail, selected_folders)
        st.success('Selected folders deleted.')
    
    if st.button('Disconnect'):
        st.session_state.mail.logout()
        st.session_state.mail = None
        st.rerun()