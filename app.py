import streamlit as st
from helper import DB
import plotly.express as px

import plotly.graph_objects as go
db=DB()
st.sidebar.title('Flight analytics')
user=st.sidebar.selectbox('Menu',['select one','Check Flights','Analytics'])
if user =='Check Flights':
    st.title('Check Flights')
    col1,col2=st.columns(2)
    city = db.fetch_city()
    with col1:

        source=st.selectbox('Source',sorted(city))
    with col1:

        dest=st.selectbox('Destination',sorted(city))
    if st.button('search'):
        result=db.fetch_all_flight(source,dest)
        st.dataframe(result)

elif  user=='Analytics':

    airline,freq=db.fetch_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=freq,
            hoverinfo="label+percent",
            textinfo="value"
        ))
    st.header("Pie chart")
    st.plotly_chart(fig)
    city, freq = db.busy()
    fig = px.bar(
            x=city,
            y=freq

        )
    st.header("Bar chart")
    st.plotly_chart(fig,theme='streamlit',use_container_width=True)
    daily,freq = db.daily()
    fig = px.line(
            x=daily,
            y=freq

        )
    st.header("Bar chart")
    st.plotly_chart(fig,theme='streamlit',use_container_width=True)

else:
    st.title('Tell about your project')