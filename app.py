import streamlit as st


st.set_page_config(page_title="Introduction", page_icon="👋")


with open("docs/Dolly Belcher CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.download_button(label="Download CV", data=PDFbyte, file_name="Dolly Belcher CV.pdf", mime='application/pdf')

st.title("Hello, I'm Dolly Belcher👋🏼")



st.write("[LinkedIn](https://www.linkedin.com/in/dollybelcher)")

st.text("")

st.markdown("""
            I am an experienced data analyst who specialises in data visualisation. I play a key role at Immediate Media, the publisher behind BBC Good Food and Radio Times, focusing on advertising revenue and sales performance.
            My expertise and passion lies in transforming data into clear, actionable insights.

            Please find my key skills and CV below. On the pages, I have included a range of dashboards I have created with short descriptions.

            If you have any questions, please contact me using the form below.
            """)

st.header("Skills")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.image("docs/python.png", width=50)

with col2:
    st.image("docs/GA.png", width=50)

with col3:
    st.image("docs/salesforce.png", width=50)

with col4:
    st.image("docs/SQL.png", width=50)

with col5:
    st.image("docs/tableau.png", width=50)

with col6:
    st.image("docs/GAM.png", width=50)






st.text("")
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
