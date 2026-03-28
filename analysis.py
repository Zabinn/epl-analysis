import pandas as pd

df = pd.read_csv("data/epl_clean.csv", parse_dates=["date"])
print(f"Loaded {len(df)} matches")

#Teams that scored most goals
home_goals=df.groupby("home team")['homegoals'].sum()
away_goals=df.groupby("away team")["awaygoals"].sum()
totalgoals=(home_goals+away_goals).sort_values(ascending=False)
print("Teams that scored the most goals:")  
print(totalgoals.head(5))


#How strong is the home advantage?
# Q2 - How strong was home advantage?
results = df["result"].value_counts()
total = len(df)

print("\nHome vs Away advantage:")
print(f"Home wins: {results['H']} ({round(results['H']/total*100, 1)}%)")
print(f"Draws:     {results['D']} ({round(results['D']/total*100, 1)}%)")
print(f"Away wins: {results['A']} ({round(results['A']/total*100, 1)}%)")

#DISCIPLINE
homeyellow=df.groupby("home team")['homeyellow'].sum()
awayyellow=df.groupby("away team")['awayyellow'].sum()
totalyellowcards=(homeyellow+awayyellow).sort_values(ascending= True) 
print("\nTeam with most discipline:")
print(totalyellowcards.head(5))

# Save results for Power BI 
totalgoals.to_csv("data/goals_by_team.csv", header=["totalgoals"])
totalyellowcards.to_csv("data/yellows_by_team.csv", header=["totalyellowcards"])
df["result"].value_counts().to_csv("data/results_summary.csv", header=["count"])

print("\nResults saved!")