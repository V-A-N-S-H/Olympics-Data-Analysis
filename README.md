# Olympics Data Analysis

An interactive **Olympics Data Analysis** web application built using **Python**, **Streamlit**, and various data visualization libraries. This project provides detailed insights into the history of the Olympic Games through interactive charts, medal tallies, athlete statistics, and country-wise analysis.

## Live Demo

**Deployment:**  
https://olympics-data-analysis-llhtkbqqpmgslyh3ldcu5j.streamlit.app/

---

## Features

### Medal Tally
- View overall medal tally
- Filter medal tally by year
- Filter medal tally by country
- Analyze country performance across Olympic editions

### Overall Analysis
- Total Olympic editions
- Number of host cities
- Participating nations
- Sports and events statistics
- Athlete participation over the years
- Events conducted in each sport
- Most successful athletes

### Country-wise Analysis
- Medal trend over the years
- Sport-wise performance heatmap
- Top athletes of a selected country

### Athlete-wise Analysis
- Age distribution of athletes
- Age distribution of medal winners
- Weight vs Height visualization
- Male vs Female participation over the years

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Matplotlib
- Seaborn
- SciPy

---

## Project Structure

```text
Olympics-Data-Analysis/
│
├── app.py                    # Streamlit application
├── helper.py                 # Analysis functions
├── preprocessor.py           # Data preprocessing
├── Olympics_Analysis.ipynb   # Data analysis notebook
│
├── athlete_events.csv        # Olympics dataset
├── noc_regions.csv           # Country mapping dataset
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Dataset

The project uses the **Olympic History Dataset**, which contains information about:

- Athlete Name
- Gender
- Age
- Height
- Weight
- Team
- Country
- Olympic Year
- Host City
- Sport
- Event
- Medal Won

The dataset is preprocessed by filtering Summer Olympics data, merging country information, removing duplicate records, and preparing the data for analysis.

---

## How It Works

1. Load the Olympics dataset.
2. Preprocess the data and merge country information.
3. Generate interactive visualizations and statistics.
4. Allow users to filter data based on year, country, and sport.
5. Display insights using tables, charts, heatmaps, and graphs.

---

## Visualizations

The application includes:

- Interactive Line Charts
- Heatmaps
- Scatter Plots
- Distribution Plots
- Plotly Visualizations
- Statistical Tables

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Olympics-Data-Analysis.git
```

### Navigate to the project folder

```bash
cd Olympics-Data-Analysis
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Main libraries used:

- streamlit
- pandas
- numpy
- plotly
- matplotlib
- seaborn
- scipy

---

## Future Improvements

- Add Olympic records and milestones.
- Compare two countries side by side.
- Predict future medal tallies using Machine Learning.
- Add athlete search functionality.
- Export charts and reports.
- Deploy using Docker and CI/CD.

---

## Author

**Vansh Kashyap**

B.Tech Computer Science and Engineering

Passionate about Data Science, Machine Learning, Data Analytics, and Artificial Intelligence.

---

## License

This project is intended for educational and learning purposes.
