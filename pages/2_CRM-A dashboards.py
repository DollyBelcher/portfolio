import streamlit as st

st.markdown("""
<style>
.custom-title {
    background: linear-gradient(to right, #83a4d4, #b6fbff); /* Ombre effect from blue to light blue */
    color: #fff; /* White text color */
    padding: 20px;
    border-radius: 10px; /* Rounded corners */
    margin: 10px 0; /* Margin for spacing */
    text-align: center;
    font-size: 36px; /* Larger font size */
    font-weight: bold; /* Bold font */
}
</style>
""", unsafe_allow_html=True)

# Use markdown to display the title with the custom style
st.markdown('<div class="custom-title">CRM-A Dashboards</div>', unsafe_allow_html=True)


st.markdown("""During my time at Immediate Media, I have created dashboards on SalesForce CRM-A.
            Please find some examples below.
            """)


st.header("OMP Audience Planning Tool")
st.markdown("""- Developed a dashboard to give sales teams a comprehensive view of the top 50 advertisers spend in the open auction.
- Provides details on advertisers' spending patterns and audience reach.
- Integrates five distinct datasets from sources such as Google Ad Manager, Permutive, and Connect.
- Aims to equip salespeople with first-party data for upselling direct advertising.
- Addresses the growing importance of direct advertising due to the depreciation of third-party cookies.""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Revenue Analysis:")
    st.image(image="docs/Picture1.png")

with col2:
    st.markdown("Demographic Analysis:")
    st.image(image="docs/OMP 2.png")


st.header("Brand KPI")

st.markdown("""
- Created a dashboard to track essential Key Performance Indicators (KPIs).
- Focuses on metrics such as Cost Per Mille (CPMs) and user cookie acceptance rates.
- Provides invaluable insights for stakeholders.
- Serves as a crucial tool for ensuring website development changes do not negatively impact advertising revenue.
            """)

col1, col2 = st.columns(2)

with col1:
    st.image(image="docs/Brand KPI 1.png")

with col2:
    st.image(image="docs/Brand KPI 2.png")
