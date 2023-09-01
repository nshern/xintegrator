import streamlit as st
import streamlit.components.v1 as components

riri = Integration("rihanna")
riri.get_tweet_table(5, type="mentions")
riri.get_posts_as_embedded(type="mentions")

# st.set_page_config(
#     page_title=None,
#     page_icon=None,
#     layout="wide",
#     initial_sidebar_state="auto",
#     menu_items=None,
# )

# riri = Integration("mfmorten")
# riri.get_tweet_table(5, "user")
# results = riri._get_posts_as_embeded(
#     type="user", params={"hide_media": "true", "hide_thread": "true"}
# )

# for i in results:
#     components.html(i, height=500)
