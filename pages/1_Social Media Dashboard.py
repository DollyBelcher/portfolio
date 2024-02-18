import streamlit as st
import streamlit.components.v1 as components
# Custom CSS for title, centering, and styling the dashboard
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

.centered-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.tableauPlaceholder {
    border: 2px solid #D7EAFF; /* Blue border */
    border-radius: 10px; /* Rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow */
}
</style>
""", unsafe_allow_html=True)

# Title with custom style
st.markdown('<div class="custom-title">Social Media</div>', unsafe_allow_html=True)


tableau_dashboard = """
<style>
.centered-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.tableauPlaceholder {
    background-color: #D7EAFF; /* Light blue background */
    border-radius: 10px; /* Rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow */
    padding: 20px;
    margin: 10px 0;
}
</style>

<div class='centered-container'>
    <div class='tableauPlaceholder' id='viz1708267693637' style='position: relative'>
        <noscript>
            <a href='#'>
                <img alt='Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;So&#47;SocialMedia_17081708178110&#47;Dashboard&#47;1_rss.png' style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz'  style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='SocialMedia_17081708178110/Dashboard' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;So&#47;SocialMedia_17081708178110&#47;Dashboard&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-GB' />
            <param name='filter' value='publish=yes' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1708267693637');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if (divElement.offsetWidth > 800) {
            vizElement.style.width='100%';
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else {
            vizElement.style.width='100%';
            vizElement.style.height='1927px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
</div>
"""

components.html(tableau_dashboard, height=1000, width=1200, scrolling=True)
