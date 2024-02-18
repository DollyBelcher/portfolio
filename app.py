import streamlit as st


st.set_page_config(page_title="Introduction", layout="wide")


with open("docs/Dolly Belcher CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.download_button(label="Download CV", data=PDFbyte, file_name="Dolly Belcher CV.pdf", mime='application/pdf')

st.title("Hello, I'm Dolly Belcher👋🏼")



st.write("[LinkedIn](https://www.linkedin.com/in/dollybelcher)")

st.text("")

st.markdown("""
            I am an experienced data analyst who specialises in data visualisation. I play a key role at Immediate Media, the publisher behind BBC Good Food and Radio Times, focusing on advertising revenue and sales performance.
            My expertise and passion lies in transforming data into clear, actionable insights.

            Please find my key skills below. On seperate pages, I have included a range of dashboards I have created with short descriptions. Any sensitive data has been redacted, to maintain confidentiality.

            If you have any questions, please contact me using the form!
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
