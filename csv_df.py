import pandas as pd
import matplotlib.pyplot as plt

# create dataframe
df = pd.read_csv('teach_me_grappling.csv')

# turn viewcount datatype from string to integer
def condition(x):
    if 'K' in x:
        return int(float(x.replace('K views', ''))*1000)
    elif 'M' in x:
        return int(float(x.replace('M views', ''))*1000000)
    else:
        return int(float(x.replace(' views', '')))

df.views = df['views'].apply(condition)

# obtain categories
grouped = df.groupby(df['title'].str.contains('escape', case=False))
oth = df.groupby(df['title'].str.contains(''))


# create bar plot using median value of each category
median_views = pd.concat([grouped.median(),oth.median()],axis=0)
median_views.plot(kind='bar')
plt.xticks(rotation=0, ticks=[0,1,2], labels=['w/o "escape"','WITH "escape"', 'All'])
plt.xlabel('Video Group')
plt.ylabel('Median Views')
legend = plt.legend()
legend.remove()
plt.title('Teach Me Grappling View Data')
plt.savefig('barplot_medians.png')
