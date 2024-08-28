import random
import numpy as np
import matplotlib.pyplot as plt
import pathlib

def main():
    nIter = 1e3 # number of iterations

    oldSelectionCorrect = []
    newSelectionCorrect = []

    for i in range(int(nIter)):
        doors = ["Door1", "Door2", "Door3"]

        # we randomly select one door as the correct door
        correctDoor = None # TODO

        # then we make our guess and also randomly pick one door
        selectedDoor = None # TODO

        # implement the opening of the one of the wrong doors
        # TODO

        # new selection would now be to pick the other unopened door
        newSelection = None # TODO
        
        # we save which decision would be better
        # we save it in this weird way to get a nice plot with the number of iterations dependance
        oldSelectionCorrect += [1] if correctDoor == selectedDoor else [0]
        newSelectionCorrect += [1] if correctDoor == newSelection else [0]

    print(f"Number of iterations: {nIter}")
    print(f"Original selection correct: {sum(oldSelectionCorrect)} ({sum(oldSelectionCorrect)/nIter:.3f} %)")
    print(f"New selection correct: {sum(newSelectionCorrect)} ({sum(newSelectionCorrect)/nIter:.3f} %)")

    fName = plotTimeDevelopment(oldSelectionCorrect, newSelectionCorrect)
    print(f"Saved plot as {fName.resolve()}")

def plotTimeDevelopment(oldSelectionCorrect, newSelectionCorrect):
    # NO NEED TO ADJUST THIS FUNCTION
    # calculate the cumulative sum
    oldSelectionCorrect_cummulative = np.cumsum(oldSelectionCorrect)
    newSelectionCorrect_cummulative = np.cumsum(newSelectionCorrect)

    total = oldSelectionCorrect_cummulative + newSelectionCorrect_cummulative

    fig, ax = plt.subplots()

    x = np.arange(len(oldSelectionCorrect_cummulative))+1
    ax.scatter(x, oldSelectionCorrect_cummulative / total, s=2, label = "Old selection correct")
    ax.scatter(x, newSelectionCorrect_cummulative / total, s=2, label = "New selection correct")

    ax.plot(x, oldSelectionCorrect_cummulative / total, alpha=.3)
    ax.plot(x, newSelectionCorrect_cummulative / total, alpha=.3)

    ax.plot([x[0], x[-1]], [1/3, 1/3], linestyle="--", c="black")
    ax.plot([x[0], x[-1]], [2/3, 2/3], linestyle="--", c="black")

    plt.ylabel("Succes rate [%]")
    plt.xlabel("Number of iterations [-]")

    plt.legend()

    ax.set_xscale("log")

    fName = pathlib.Path("dvere.png")
    fig.savefig(fName, dpi=250)
    return fName

if __name__ == "__main__":
    main()