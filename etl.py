import pandas as pd
from pathlib import Path
# File paths
RAW_FILE   = Path("data/epl_raw.csv")
CLEAN_FILE = Path("data/epl_clean.csv")

# EXTRACT - Load the raw data
df = pd.read_csv(RAW_FILE, encoding="latin-1")
print("Raw data loaded!")
#print(f"Rows: {len(df)}")
#print(f"Columns: {list(df.columns)}")

# TRANSFORM - Clean the data
columns_needed={"Date":"date",'HomeTeam':'home team','AwayTeam':'away team','FTHG':'homegoals','FTAG':'awaygoals','FTR':'result','HS':'homeshots','AS':'awayshots','HST':'home_shots_on_target','AST':'away_shots_on_target','HF':'homefouls','AF':'awayfouls', 'HY':'homeyellow','AY':'awayyellow' }  
df = df.rename(columns=columns_needed)
df = df[list(columns_needed.values())]
# print(f"\nColumns after transform: {list(df.columns)}")
# Clean - fix date type and drop any empty rows
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
df = df.dropna()
print(f"Clean rows: {len(df)}")
#printing the first few rows of the cleaned data
print(df["date"].dtype)
print(df["date"].head())

#adding columns
df['total_goals'] = df['homegoals']+df['awaygoals']
df['home_points']=df['result'].map({'H':3,'D':1,'A':0})
df['away_points']=df['result'].map({'H':0,'D':1,'A':3})
print (df.head())

# LOAD - Save clean data
df.to_csv(CLEAN_FILE, index=False)
print("Clean file saved to data/epl_clean.csv!")