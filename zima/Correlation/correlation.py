import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def main():
    # load correlation data
    df = pd.read_csv('korelace.txt', sep = '\t', names = ['temperature', 'profit'])

    #plot data
    simple_plot([df['temperature']], [df['profit']], [None], 'Outside temperature [$^\\circ$C]', 'Profit [CZK]', 'ice_cream_profit.png')
    
    rho_p = pearson_for_cycles(df['temperature'].tolist(), df['profit'].tolist())
    print("pearson coefficient = ", rho_p)

    rho_s = spearman_corr(df['temperature'], df['profit'])
    print("spearman coefficient = ", rho_s)


def simple_plot(xdata, ydata, labels, xlabel, ylabel, filename = None): #function for plotting several datasets into the same image, x and ydata are expected to be lists of arrays. If only a single dataset is to be plotted, it must also be inside a list -> dataset = [dataset]

    plt.rcParams['font.size'] = 14 # changes font size
    fig, ax = plt.subplots(figsize = [8,6]) # creates a figure and a subplot object

    for x, y, l in zip(xdata, ydata, labels): # loop over several arrays at once (cuts when the first array finishes)
        ax.scatter(x, y, label = l) # line plot of x and y with a label to displayed inside a legend

    ax.legend() # includes a legend in the image
    ax.set_xlabel(xlabel) # gives a name to the x axis, below analogy for y axis
    ax.set_ylabel(ylabel) # matplotlib supports latex like math type-setting

    plt.show() # displays the current figure 
    if filename:
        fig.savefig(filename) # saves the figure 'fig' as a png file


def pearson_for_cycles(X,Y):
    mean_x, mean_y = 0, 0
    size = min(len(X), len(Y))
    for x, y in zip(X, Y):
        mean_x += x
        mean_y += y
    mean_x = mean_x / size
    mean_y = mean_y / size

    var_x, var_y, cov = 0, 0, 0
    for x, y in zip(X, Y):
        var_x += (x - mean_x) ** 2
        var_y += (y - mean_y) ** 2
        cov += (x - mean_x) * (y - mean_y)
    sigma_x = (var_x / (size - 1)) ** 0.5
    sigma_y = (var_y / (size - 1)) ** 0.5
    cov = cov / (size - 1)
    rho = cov / ( sigma_x * sigma_y )

    return rho


def pearson_numpy(x, y):
    return np.sum((x - np.mean(x))*(y - np.mean(y)))/np.sqrt(np.sum((x - np.mean(x)) ** 2) * np.sum((y - np.mean(y)) ** 2))


def spearman_corr(X,Y): # expects two pandas dataframes
    rank_x = X.rank(method = 'min').astype(int) # ranks the values of X
    rank_y = Y.rank(method = 'min').astype(int)
    diff_sq = (rank_x - rank_y) ** 2
    size = diff_sq.size
    sum_dif = diff_sq.sum()
    rho_s = 1 - 6 * sum_dif/ (size * (size ** 2 - 1))
    return rho_s


def rank_data(data):
    # Assign ranks to the data
    return np.argsort(np.argsort(data))


if __name__ == "__main__":
    main()