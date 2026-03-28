import pandas as pd
import sqlite3

# Load clean data into a temporary SQLite database
conn = sqlite3.connect(":memory:")
df = pd.read_csv("data/epl_clean.csv")
df.to_sql("epl_clean", conn, index=False, if_exists="replace")

# Q1: Top goal scoring teams
q1 = """
SELECT 
    team,
    SUM(goals) AS total_goals
FROM (
    SELECT "home team" AS team, homegoals AS goals FROM epl_clean
    UNION ALL
    SELECT "away team" AS team, awaygoals AS goals FROM epl_clean
)
GROUP BY team
ORDER BY total_goals DESC;
"""

result1 = pd.read_sql(q1, conn)
print(" Top Goal Scoring Teams ")
print(result1.head(10))
print()

# Q2: Home vs Away Win %
q2 = """
SELECT 
    result,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM epl_clean), 2) AS percentage
FROM epl_clean
GROUP BY result
ORDER BY count DESC;
"""

result2 = pd.read_sql(q2, conn)
print(" Home vs Away Win %")
print(result2)
print()

# Q3: Most disciplined teams by yellow cards
q3 = """
SELECT 
    team,
    SUM(yellows) AS total_yellows
FROM (
    SELECT "home team" AS team, homeyellow AS yellows FROM epl_clean
    UNION ALL
    SELECT "away team" AS team, awayyellow AS yellows FROM epl_clean
)
GROUP BY team
ORDER BY total_yellows ASC;
"""

result3 = pd.read_sql(q3, conn)
print(" Most Disciplined Teams (Fewest Yellow Cards)")
print(result3.head(10))
print()

# Q4: Team with highest average goals per game
q4 = """
SELECT 
    team,
    ROUND(SUM(goals) * 1.0 / COUNT(*), 2) AS avg_goals_per_game
FROM (
    SELECT "home team" AS team, homegoals AS goals FROM epl_clean
    UNION ALL
    SELECT "away team" AS team, awaygoals AS goals FROM epl_clean
)
GROUP BY team
ORDER BY avg_goals_per_game DESC;
"""

result4 = pd.read_sql(q4, conn)
print(" Highest Average Goals Per Game")
print(result4.head(10))
print()

# Q5: Team with most clean sheets
q5 = """
SELECT 
    team,
    COUNT(*) AS clean_sheets
FROM (
    SELECT "home team" AS team FROM epl_clean WHERE awaygoals = 0
    UNION ALL
    SELECT "away team" AS team FROM epl_clean WHERE homegoals = 0
)
GROUP BY team
ORDER BY clean_sheets DESC;
"""

result5 = pd.read_sql(q5, conn)
print(" Most Clean Sheets")
print(result5.head(10))
print()

# Q6: Attacking efficiency - goals scored vs shots on target ratio
q6 = """
SELECT 
    team,
    SUM(goals) AS total_goals,
    SUM(shots_on_target) AS total_shots_on_target,
    ROUND(SUM(goals) * 1.0 / SUM(shots_on_target), 2) AS conversion_rate
FROM (
    SELECT "home team" AS team, homegoals AS goals, home_shots_on_target AS shots_on_target FROM epl_clean
    UNION ALL
    SELECT "away team" AS team, awaygoals AS goals, away_shots_on_target AS shots_on_target FROM epl_clean
)
GROUP BY team
ORDER BY conversion_rate DESC;
"""

result6 = pd.read_sql(q6, conn)
print(" Attacking Efficiency (Goals per Shot on Target)")
print(result6.head(10))
print()