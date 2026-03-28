# 'Top goal scoring teams'#
SELECT 
    team,
    SUM(goals) AS total_goals
FROM (
    SELECT "home team" AS team, homegoals AS goals FROM epl_clean
    UNION ALL
    SELECT "away team" AS team, awaygoals AS goals FROM epl_clean
) AS all_goals
GROUP BY team
ORDER BY total_goals DESC;

# 'Home vs Away Win %'#
SELECT 
    result,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM epl_clean), 2) AS percentage
FROM epl_clean
GROUP BY result
ORDER BY count DESC;

# 'Disciplined Teams'#
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

# 'Highest Average Goals Per Game'#
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


# 'Most Clean Sheets'#
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

# 'Attacking Efficiency (Goals per Shot on Target)'#
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