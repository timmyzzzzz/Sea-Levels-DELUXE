import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x= "Year", y = "CSIRO Adjusted Sea Level", data = df)
    # Create first line of best fit

    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880,2050))
    ax.plot(years, intercept + slope*years, 'r', label='first line of best fit')
    # Create second line of best fit
    df2 = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    years2 = pd.Series(range(2000,2050))
    ax.plot(years2, intercept2 + slope2*years2, 'b', label='second line of best fit')
    ax.legend()
    # Add labels and title
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot3.png')
    return fig.gca()
draw_plot()


def draw_plot1():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880, 2050))
    ax.plot(years, intercept + slope * years, 'r', label='First Line of Best Fit')
    
    # Create second line of best fit
    df2 = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    years2 = pd.Series(range(2000, 2050))
    ax.plot(years2, intercept2 + slope2 * years2, 'b', label='Second Line of Best Fit')
    
    # Add legend
    ax.legend()
    
    # Add labels and title
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot5.png')
    return fig.gca()

draw_plot1()