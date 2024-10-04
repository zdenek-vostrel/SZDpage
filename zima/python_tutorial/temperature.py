#let's now try working with some larger dataset, for example weather data. To visualize it, we will need a new library - matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt


def main():
    filename = 'weather_data.csv'
    df = pd.read_csv(filename)
    time = pd.to_datetime(df['utc_timestamp'])

    ref_times = ["1980-01-01","1990-01-01","2000-01-01","2010-01-01", "2020-01-01"]

    xdata = [time[(time >= n) & (time < m)] for n, m in zip(ref_times[:-1], ref_times[1:])] # pandas allows conditional opperation on its elements, in this case our time axis is split into 4 regions according to a decade time intervals
    ydata = [df['CZ_temperature'][(time >= n) & (time < m) ] for n, m in zip(ref_times[:-1], ref_times[1:])] # the temperature column is split with the same conditional mask
    labels = ['yrs \'80 - \'90','yrs \'90 - \'00','yrs \'00 - \'10','yrs \'10 - \'20'] # label strings for the plot legend

    simple_plot(xdata, ydata, labels) #calling the plot function inside the main function


def simple_plot(xdata, ydata, labels): #function for plotting several datasets into the same image, x and ydata are expected to be lists of arrays. If only a single dataset is to be plotted, it must also be inside a list -> dataset = [dataset]

    plt.rcParams['font.size'] = 14 # changes font size
    fig, ax = plt.subplots(figsize = [8,6]) # creates a figure and a subplot object

    for x, y, l in zip(xdata, ydata, labels): # loop over several arrays at once (cuts when the first array finishes)
        ax.plot(x, y, label = l) # line plot of x and y with a label to displayed inside a legend

    ax.legend() # includes a legend in the image
    ax.set_xlabel('Date') # gives a name to the x axis, below analogy for y axis
    ax.set_ylabel('Temperature [$^\\circ$C]') # matplotlib supports latex like math type-setting

    plt.show() # displays the current figure 
    fig.savefig('modifiedTemperature.png') # saves the figure 'fig' as a png file


if __name__ == "__main__":
    main()