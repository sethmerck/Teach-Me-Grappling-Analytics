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
counts = pd.concat([grouped.count(), oth.count()], axis=0)
print([i for i in counts.title.values])
median_views = pd.concat([grouped.median(),oth.median()],axis=0)
med_views_list = [i for i in median_views.views.values]
median_views.plot(kind='bar')

data = [i for i in counts.title.values]

for i, v in enumerate(data):
    plt.text(i-0.225, med_views_list[i] * 0.5, f'n = {str(v)}', fontsize=12)

plt.xticks(rotation=0, ticks=[0,1,2], labels=['w/o "escape"','WITH "escape"', 'All'])
plt.xlabel('Video Group')
plt.ylabel('Median Views')
legend = plt.legend()
legend.remove()
plt.title('Teach Me Grappling View Data')
plt.savefig('bar_plot_median.png')
