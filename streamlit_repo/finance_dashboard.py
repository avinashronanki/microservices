#https://www.youtube.com/watch?v=0ESc1bh3eIg
import streamlit as st 
import pandas as pd 
import numpy as np
import requests

# st.title("this is a title")
# st.header("this is a header")
# st.write("this is a requral text")
# st.write("test")

# st.sidebar.write("this is supercool web app")

# df = pd.DataFrame(
#     np.random.randn(50, 20),
#     columns=('col %d' % i for i in range(20)))
# st.dataframe(df.style.highlight_max(axis=0))

# st.image("https://images.unsplash.com/photo-1490730141103-6cac27aaab94?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80")

options = st.sidebar.selectbox("which dashboard",("twitter","wallstreet bets","stocktwits","chart","pattern"))
st.header(options)

if options == 'stocktwits':
    symbol = st.sidebar.text_input("Input text",value='AAPL')

    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    data = r.json()
    # st.write(data)

    for message in data["messages"]:
        st.write('Messages: '+message['body'])
        st.write('Created at :'+message['created_at'])

