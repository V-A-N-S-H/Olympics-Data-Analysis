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

    st.table(medal_tally)

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

    st.title("Most Successful Athletes")
    sport = df["Sport"].unique().tolist()
    sport.sort()
    sport.insert(0, "Overall")

    selected_sport = st.selectbox("Select a Sport", sport)
    x = helper.most_successful_athlete(df, selected_sport)
    st.table(x)

if user_menu == "Country-wise Analysis":

    st.sidebar.title("Country-wise Medal Tally")

    country_list = df["region"].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox("Select a Country", country_list)

    country_df = helper.year_wise_medal_tally(df, selected_country)

    country_df = helper.year_wise_medal_tally(df, selected_country)

    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally Over the Years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

    st.title("Top 15 athletes of " + selected_country)
    top_athletes = helper.most_successful_athlete_of_country(df, selected_country)
    st.table(top_athletes)