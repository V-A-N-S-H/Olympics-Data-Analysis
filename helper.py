def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values("Gold", ascending=False).reset_index()

    medal_tally["Total"] = medal_tally["Gold"] + medal_tally["Silver"] + medal_tally["Bronze"]

    return medal_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, "Overall")

    country = df['region'].dropna()
    country = country.unique().tolist()
    country.sort()
    country.insert(0, "Overall")

    return years, country

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == "Overall" and country == "Overall":
        temp_df = medal_df
    if year == "Overall" and country != "Overall":
        flag = 1
        temp_df = medal_df[medal_df["region"] == country]
    if year != "Overall" and country == "Overall":
        temp_df = medal_df[medal_df["Year"] == int(year)]
    if year != "Overall" and country != "Overall":
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values("Year").reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values("Gold", ascending=False).reset_index()
    x["total"] = x["Gold"] + x["Silver"] + x["Bronze"]

    return x
        

def participating_nation_over_time(df):

    nations_over_time = df.drop_duplicates(["Year", "region"])["Year"].value_counts().reset_index().sort_values("Year")

    return nations_over_time

def no_of_events_over_time(df):

    events_over_time = df.drop_duplicates(["Year", "Event"])["Year"].value_counts().reset_index().sort_values("Year")

    return events_over_time

def participating_athlete_over_time(df):

    athletes_over_time = df.drop_duplicates(["Year", "Name"])["Year"].value_counts().reset_index().sort_values("Year")

    return athletes_over_time


def most_successful_athlete(df, sport):
    temp_df = df.dropna(subset=["Medal"])

    if sport != "Overall":
        temp_df = temp_df[temp_df["Sport"] == sport]

    x = temp_df["Name"].value_counts().reset_index()
    x.columns = ["Name", "Medals"]

    return (
        x.head(10)
        .merge(df, on="Name", how="left")
        [["Name", "Medals", "Sport", "region"]]
        .drop_duplicates("Name")
    )