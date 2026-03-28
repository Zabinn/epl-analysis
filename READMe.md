# EPL 2023/24 Data Analysis Project

A data analysis portfolio project exploring the English Premier League 2023/24 season using Python, SQL and Power BI.

## Tools Used
- Python (Pandas, Matplotlib, Seaborn)
- SQL (SQLite)
- Power BI

## Project Structure
epl-analysis/
    ├── data/
    │   ├── epl_raw.csv
    │   ├── epl_clean.csv
    │   ├── goals_by_team.csv
    │   ├── yellows_by_team.csv
    │   └── results_summary.csv
    ├── etl.py
    ├── analysis.py
    ├── visualization.py
    ├── sql_queries.py
    └── READMe.md
     

## Data Source
Data sourced from [football-data.co.uk](https://www.football-data.co.uk) — EPL 2023/24 season.

## Key Findings

### Goals
- Man City were the top scoring team with 96 goals across the season
- Man City also had the highest average goals per game at 2.53

### Attacking Efficiency
- West Ham, Newcastle, Aston Villa and Arsenal were the most clinical finishers with a 40% conversion rate
- Man City had more shots on target (278) but a lower conversion rate (35%) — winning through volume

### Defense
- Arsenal kept the most clean sheets (18) — the best defense in the league
- Man City were second with 13 clean sheets

### Home Advantage
- Home teams won 46% of matches vs 32% for away teams — home advantage is significant in the EPL

### Discipline
- Man City were the most disciplined team with only 51 yellow cards

## How to Run

1. Run ETL pipeline:
```
    python etl.py
```

2. Run analysis:
```
    python analysis.py
```

3. Run visualizations:
```
    python visualization.py
```

4. Run SQL queries:
```
    python sql_queries.py
```

## Charts
Generated charts are saved in the `reports/` folder:
- `chart1_goals.png` — Total goals by team
- `chart2_results.png` — Home vs Away win %
- `chart3_discipline.png` — Yellow cards by team
- `dashboard_preview.png` — Power BI dashboard screenshot

## Dashboard Preview
![Dashboard](reports/dashboard_preview.png)

## queries.sql
Queries for sql added 

## Author
Mohammed Zabin Shukkoor