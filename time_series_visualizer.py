import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=['date'])

# Clean data
hi = df['value'].quantile(0.025)
lo = df['value'].quantile(0.975)
df = df.loc[(df['value'] >= hi) & (df['value'] <= lo)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(17, 8))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df, color='red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).mean()

    legends = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
               'September', 'October', 'November', 'December']

    # Draw bar plot
    fig = df_bar.unstack().plot(kind='bar', figsize = (16, 10)).figure
    plt.legend(legends)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figwidth(20)
    fig.set_figheight(10)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax1 = sns.boxplot(x=df_box.year, y=df_box.value, data=df_box, ax=ax1)
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Year')
    ax2 = sns.boxplot(x=df_box.month, y=df_box.value, data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
