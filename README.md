# <img src='belts.jpeg' height='50'></a> Teach Me Grappling Analytics
This project scrapes all videos and their information (title, upload date, view count) from the Youtube channel ["Teach Me Grappling"](https://www.youtube.com/channel/UC8X1oaFtxTGGAueI-sWE4Mg), although this project can easily be replicated for any Youtube channel simply by changing the 'url' variable within the 'scraper.py' file in this repo. The sequence runs as follows: 1. 'scraper.py' scrapes info from the channel's video page 2. the info is stored in 'teach_me.csv' 3. 'csv_df.py' reads the csv file into a pandas dataframe where data manipulation and analysis is performed 4. finally the end data is visualized in 'barplot.png'

Note that in order for selenium to operate on your machine you must also have a browser driver installed and in your working directory.

## How It's Made:

**Tech used:** Python, Selenium, Pandas, Matplotlib

Used Python's Selenium library to first scroll to the bottom of the channel's page in order to load every video. Then extract links, titles, published date, and view count for every video. 

After this, I used Python's csv library to write each video and its accompanying information as a row in a csv file.

Next I used Pandas to convert the values in the 'views' columns from strings to numerical data types. Firstly though, the 'K' and 'M' values (representing 1000 and 1000000 respectively) had to be removed from the strings in order for them to be converted to numerical data types. These were removed conditionally using a stand alone function within pandas "apply" method. After cleaning the dataset I used Matplotlib to create a simple visualization of the median and mean view counts for all videos on this channel.

## Future Expansions

In the near future, I'll separate videos into different categories based on technique to see which techniques get more relative amounts of views. I'll start with just this channel, but eventually incorporate several other grappling youtube channels.
