import streamlit as st
import streamlit.components.v1 as components


# Custom CSS for title and dashboard styling
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

.centered-content {
    display: flex;
    justify-content: center;
    align-items: center;
}

.tableauPlaceholder {
    margin: 0 auto; /* Center the dashboard */
    width: auto; /* Full width */
    height: 100%; /* Auto-adjust the height */
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-title">Social Media</div>', unsafe_allow_html=True)

st.markdown("""
    In my personal time, I have analysed a public dataset which shows the amount of time people spend on social media.
    The main chart shows the negative correlation between income and time spent on social media, with younger people spending more time on social media but have, on average, lower incomes.
""")

tableau_dashboard = """
<div class='centered-content'>
    <div class='tableauPlaceholder' id='viz1708267693637'>
        <div class='tableauPlaceholder' id='viz1708267693637' style='position: relative'><noscript><a href='#'><img alt='Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;So&#47;SocialMedia_17081708178110&#47;Dashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SocialMedia_17081708178110&#47;Dashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;So&#47;SocialMedia_17081708178110&#47;Dashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1708267693637');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='500px';vizElement.style.maxWidth='1000px';vizElement.style.width='100%';vizElement.style.minHeight='627px';vizElement.style.maxHeight='1127px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='500px';vizElement.style.maxWidth='1000px';vizElement.style.width='100%';vizElement.style.minHeight='627px';vizElement.style.maxHeight='1127px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1927px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

    </div>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1708267693637');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width='100%';
    vizElement.style.height='auto';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Embed the dashboard using Streamlit components
components.html(tableau_dashboard, width=1100, height=1100, scrolling=True)

