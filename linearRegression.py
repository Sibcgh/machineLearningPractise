import pandas as pd
import quandl


df = quandl.get("WIKI/GOOGL")

df  = df [['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = 
print(df.head())