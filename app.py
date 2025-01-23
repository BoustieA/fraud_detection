import streamlit as st
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger.info('Started app.py')

pg = st.navigation([
    st.Page("Pages/page1.py", title="Prédiction", icon=":material/attach_money:"),
    #st.Page("Pages/page2.py", title="Analyse data", icon=":material/monitoring:"),
])
pg.run()