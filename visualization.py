import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv("data/epl_clean.csv", parse_dates=["date"])
sns.set_theme(style="whitegrid")


# Chart 1 - Goals by team
home_goals = df.groupby("home team")["homegoals"].sum()
away_goals = df.groupby("away team")["awaygoals"].sum()
totalgoals = (home_goals + away_goals).sort_values(ascending=True)

plt.figure(figsize=(10, 8))
totalgoals.plot(kind="barh", color="blue")
plt.title("Total Goals Scored by Team — EPL 2023/24", fontsize=14, fontweight="bold")
plt.xlabel("Goals")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig("reports/chart1_goals.png")
plt.close()
print("Chart 1 saved!")

results = pd.read_csv("data/results_summary.csv", index_col=0)
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(results["count"], labels=results.index ,autopct="%1.1f%%")
ax.set_title("Home Win / Draw / Away Win %")
plt.savefig("reports/chart2_results.png" )
plt.close()
print("Chart 2 saved!")

yellows = pd.read_csv("data/yellows_by_team.csv", index_col=0)

plt.figure(figsize=(12, 6))
sns.barplot(x=yellows.index, y=yellows["totalyellowcards"],color='yellow')
plt.title("Yellow Cards by Team")
plt.xlabel("Team")
plt.ylabel("Total Yellow Cards")
plt.xticks(rotation=45, ha="right")
plt.savefig("reports/chart3_discipline.png", bbox_inches="tight")
plt.close()
print("Chart 3 saved!")