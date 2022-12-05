import pandas as pd
import re
import matplotlib.pyplot as plt

df = pd.read_csv('teach_me_grappling.csv')

def condition(x):
    if 'K' in x:
        return int(float(x.replace('K views', ''))*1000)
    elif 'M' in x:
        return int(float(x.replace('M views', ''))*1000000)
    else:
        return int(float(x.replace(' views', '')))

df.views = df['views'].apply(condition)


print(df.views.mean(), df.views.median())
print(df)

plt.bar(['Mean Views', 'Median Views'], [int(df.views.mean()), int(df.views.median())])
plt.title("Channel Videos' Mean and Median Views")
plt.savefig('barplot.png')