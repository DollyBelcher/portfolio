import streamlit as st


st.header("✉️Contact me!")

form = """<form action="https://formsubmit.co/dollybelcher@hotmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder="Message"></textarea>
     <button type="submit">Send</button>
</form>"""

st.markdown(form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
