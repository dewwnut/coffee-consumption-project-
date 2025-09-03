import plotly.express as px

def plot_consumption(df):
    # Bar chart: Top 10 coffee-consuming countries by total consumption
    fig = px.bar(df.nlargest(10, 'total_consumption'),
                 x='country', y='total_consumption',
                 title='Top 10 Coffee Consuming Countries (Total)',
                 labels={'total_consumption': 'Total Consumption (kg)'},
                 template='plotly_dark')
    fig.show()

    # Scatter plot: Per capita vs. total consumption
    fig = px.scatter(df, x='per_capita_consumption', y='total_consumption',
                     title='Per Capita vs. Total Coffee Consumption',
                     labels={'per_capita_consumption': 'Per Capita Consumption (kg)',
                             'total_consumption': 'Total Consumption (kg)'},
                     template='plotly_dark')
    fig.show()
