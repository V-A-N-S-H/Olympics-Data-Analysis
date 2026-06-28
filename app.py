import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Olympics Analysis",
    layout="wide"
)

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    "Select an Option",
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select the Year", years)
    selected_country = st.sidebar.selectbox("Select the Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == "Overall" and selected_country == "Overall":
        st.title("Overall Tally")
    if selected_year == "Overall" and selected_country != "Overall":
        st.title(f'{selected_country} overall performance')
    if selected_year != "Overall" and selected_country == "Overall":
        st.title(f'Medal Tally in {selected_year}')
    if selected_year != "Overall" and selected_country != "Overall":
        st.title(f'Medal Tally in {selected_year} for {selected_country}')

    st.dataframe(medal_tally)

if user_menu == "Overall Analysis":
    Edition = df['Year'].unique().shape[0] - 1
    Cities = df['City'].unique().shape[0]
    Sports = df['Sport'].unique().shape[0]
    Events = df['Event'].unique().shape[0]
    Athletes = df['Name'].unique().shape[0]
    Nations = df['region'].unique().shape[0]

    st.title("Top Statistics")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(Edition)
    with col2:
        st.header("Hosts")
        st.title(Cities)
    with col3:
        st.header("Sports")
        st.title(Sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(Events)
    with col2:
        st.header("Athletes")
        st.title(Athletes)
    with col3:
        st.header("Nations")
        st.title(Nations)

    nations_over_time = helper.participating_nation_over_time(df)
    fig = px.line(nations_over_time, x="Year", y="count")
    fig.update_layout(
    yaxis_title="Number of Nations",
    xaxis_title="Year"
    )
    st.title("Participating Nations Over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.no_of_events_over_time(df)
    fig = px.line(events_over_time, x="Year", y="count")
    fig.update_layout(
        yaxis_title="Number of Events",
        xaxis_title="Year"
    )
    st.title("Number of Events Over the Years")
    st.plotly_chart(fig)

    Athlete_over_time = helper.participating_athlete_over_time(df)
    fig = px.line(Athlete_over_time, x="Year", y="count")
    fig.update_layout(
        yaxis_title="Number of Athletes",
        xaxis_title="Year"
    )
    st.title("Participating Athletes Over the Years")
    st.plotly_chart(fig)

    st.title("Events in Each Sport Over the Years")
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(["Year", "Sport", "Event"])
    ax = sns.heatmap(x.pivot_table(
        index="Sport",
        columns="Year",
        values="Event",
        aggfunc="count"
    ).fillna(0).astype("int"), annot=True)
    st.pyplot(fig)