import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    apples = np.random.normal(0, 1.5, [2, 50000]) # generates 2 random arrays with gaussian distribution of mean value 0, sigma 1.5 and size 500000
    simple_plot([apples[0]], [apples[1]], ['Fallen apples'], None, None, "fallen_apples.png")
    
    # in the main function
    dist = (apples[0]**2 + apples[1]**2)**0.5 # calculates the radial distance of all points from the origin
    hist, edges = np.histogram(dist, bins = 500) # makes a histogram of those radial distances with 500 bins between minimal and maximal value
    safe_zone = find_safe_distance(hist, edges, len(apples[0]), 0.002) # calculates where the probability of getting hit is less than 0.2 %
    plot_histogram(hist, edges, None, 'Radial distance', f'Fallen apples / {np.round(edges[1] - edges[0], 3)} m', safe_zone, "fallen_apples_hist.png") # plots the histogram. the f'...{}' format allows one to execute code inside a string, the result of the code will then be converted to string.
    y0, probabilities = catch_apple(apples, 0.5, 1)
    plot_histogram(probabilities, np.append(y0, y0[-1] + 0.02), None, 'Point of origin [m]', 'Injury probability', y0[np.where(np.array(probabilities) <= 0.002)[0][0]] ,'fallen_apples_finite_area.png')
    

def find_safe_distance(hist, edges, size, prob):
    integral = 0
    for x, y in zip(hist, edges): # add relative frequency of histograms until the limit value is reached
        if integral >= 1 - prob:
            return y
        else:
            integral += x/size


def plot_histogram(hist, edges, lbl, xlabel, ylabel, line_pos, filename = None):
    plt.rcParams['font.size'] = 14 # change font size
    fig, ax = plt.subplots(figsize = [8,6]) # initialize image
    ax.stairs(hist, edges, label = lbl, fill = False, color = 'black') # plot histogram from histogram data and bin edge values
    ax.vlines(x = line_pos, ymin = 0, ymax=np.max(hist), color = 'red', label = f'Critical value at {np.round(line_pos, 2)}') # draw a vertical line where falling apples are unlikely
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    plt.show()
    if filename:
        fig.savefig(filename) # save image as png file


def catch_apple(apples, radius, sample_size):
    y0 = np.arange(0, 8, 0.02) # center of our circle
    size = len(apples[0]) # how many apples are we simulating?
    probabilities = [] # values to fill and plot
    for y in y0:
        relative_position = apples[0] ** 2 + (apples[1] - y) ** 2 # radial distance 
        portion = len(np.where(relative_position <= radius ** 2)[0]) / size # what portion of our points are within the circle
        probabilities.append(portion * sample_size)
    return y0, probabilities


def simple_plot(xdata, ydata, labels, xlabel, ylabel, filename = None, mk = ','): #function for plotting several datasets into the same image, x and ydata are expected to be lists of arrays. If only a single dataset is to be plotted, it must also be inside a list -> dataset = [dataset]

    plt.rcParams['font.size'] = 14 # changes font size
    fig, ax = plt.subplots(figsize = [8,6]) # creates a figure and a subplot object

    for x, y, l in zip(xdata, ydata, labels): # loop over several arrays at once (cuts when the first array finishes)
        ax.plot(x, y, label = l, marker = mk, linestyle = 'None') # plot with pixel size points (not a histogram) when marker is ','

    ax.legend() # includes a legend in the image
    ax.set_xlabel(xlabel) # gives a name to the x axis, below analogy for y axis
    ax.set_ylabel(ylabel) # matplotlib supports latex like math type-setting
    #ax.set_aspect('equal')

    plt.show() # displays the current figure 
    if filename:
        fig.savefig(filename) # saves the figure 'fig' as a png file


if __name__ == "__main__":
    main()