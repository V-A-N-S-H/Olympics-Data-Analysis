import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

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

if user_menu == "Athlete-wise Analysis":

    st.title("Distribution of Age")
    athlete_df = df.drop_duplicates(subset=["Name", "region"])

    x1 = athlete_df["Age"].dropna()
    x2 = athlete_df[athlete_df["Medal"] == "Gold"]["Age"].dropna()
    x3 = athlete_df[athlete_df["Medal"] == "Silver"]["Age"].dropna()
    x4 = athlete_df[athlete_df["Medal"] == "Bronze"]["Age"].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ["Age Distribution", "Gold Medalist", "Silver Medalist", "Bronze Medalist"], show_hist=False, show_rug=False)
    st.plotly_chart(fig)

    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    famous_sports = ['Baseball', "Judo", "Football", "Athletics",
                  "Swimming", "Badminton", "Gymnastics",
                  "Handball", "Weightlifting", "Wrestling",
                  "Water Polo", "Hockey", "Rowing",
                  "Shooting", "Boxing", "Taekwondo", "Cycling", "Diving",
                  "Tennis", "Golf", "Softball", "Archery",
                  "Volleyball", "Table Tennis", "Rugby Sevens",
                  "Beach Volleyball", "Rugby", "Polo", "Ice Hockey"]
    
    x = []
    name = []
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df["Sport"] == sport]
        x.append(temp_df[temp_df["Medal"] == "Gold"]["Age"].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    st.plotly_chart(fig)

    st.title("Weight vs Height of Athletes")
    sport = df["Sport"].unique().tolist()
    sport.sort()
    sport.insert(0, "Overall")

    selected_sport = st.selectbox("Select a Sport", sport)

    temp_df = helper.weight_vs_height(df, selected_sport)

    fig, ax = plt.subplots()
    ax = sns.scatterplot(x="Weight", y="Height", hue="Medal", style="Sex", data=temp_df, size=70)
    st.pyplot(fig)

    st.title("Men vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    st.plotly_chart(fig)