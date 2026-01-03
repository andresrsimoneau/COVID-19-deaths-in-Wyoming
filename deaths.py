import pandas as pd
import sqlite3

wyoming = pd.read_csv('us-states.csv')
sqlwyoming = sqlite3.connect('wyoming.db')

wyoming.to_sql('wyoming', sqlwyoming, if_exists = 'replace', index=False)
sqllivewyoming = sqlwyoming.cursor()

sqllivewyoming.execute("""
SELECT SUM(
FROM wyoming 
WHEN state = 'Wyoming' AND date < 2021-01-01
""")

the2020cases = sqllivewyoming.fetchall()
