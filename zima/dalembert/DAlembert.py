import random
import matplotlib.pyplot as plt
import numpy as np
import pathlib

def main():
    # Parameters
    initial_balance = 200           # Initial balance
    base_bet = 20                   # Initiabl bet
    bet_change = 5                  # Change of the bet
    rounds = 20                     # Maximum number of rounds
    number_of_simulations = 1000    # Nummber of simulations

    # Results       
    final_balance_DAlembert = []    
    final_balance_sameBet = []   
    final_balance_randomBet = []    

    for sim in range(number_of_simulations):
        # Start of the simulation
        final_balance_DAlembert += [d_alembert_strategy(initial_balance, base_bet, rounds, bet_change)]
        final_balance_sameBet += [always_bet_the_same(initial_balance, base_bet, rounds)]
        final_balance_randomBet += [random_bet_change(initial_balance, base_bet, rounds, bet_change)]

    plot(final_balance_DAlembert, final_balance_sameBet, final_balance_randomBet, initial_balance)


def plot(final_balance_DAlembert, final_balance_sameBet, final_balance_randomBet, initial_balance):
    fig, ax = plt.subplots()

    x = np.arange(len(final_balance_DAlembert))+1

    ax.hist(x, bins=x, weights=final_balance_DAlembert, align="mid", histtype="step", facecolor="none", alpha=.5, label="D'Alembert")
    m = np.mean(final_balance_DAlembert)
    s = np.std(final_balance_DAlembert)/np.sqrt(len(final_balance_DAlembert))
    ax.plot([x[0], x[-1]], [m,m], linestyle="--", c="C0", label=f"D'Alembert mean ({m:.1f} $\pm$ {s:.1f})")

    ax.hist(x, bins=x, weights=final_balance_sameBet, align="mid", histtype="step", facecolor="none", alpha=.5, label="Constant bet")
    m = np.mean(final_balance_sameBet)
    s = np.std(final_balance_sameBet)/np.sqrt(len(final_balance_sameBet))
    ax.plot([x[0], x[-1]], [m,m], linestyle="--", c="C1", label=f"Constant bet mean ({m:.1f} $\pm$ {s:.1f})")

    ax.hist(x, bins=x, weights=final_balance_randomBet, align="mid", histtype="step", facecolor="none", alpha=.5, label="Random bet")
    m = np.mean(final_balance_randomBet)
    s = np.std(final_balance_randomBet)/np.sqrt(len(final_balance_randomBet))
    ax.plot([x[0], x[-1]], [m,m], linestyle="--", c="C2", label=f"Random bet mean ({m:.1f} $\pm$ {s:.1f})")

    ax.plot([x[0], x[-1]], [initial_balance, initial_balance], linestyle="--", c="black", label="Initial balance")

    plt.ylabel("Balance at the end of the game")
    plt.xlabel("Game number")

    plt.legend()

    fName = pathlib.Path("DAlembert.png")
    fig.savefig(fName, dpi=250)

def d_alembert_strategy(initial_balance, base_bet, rounds, bet_change):
    balance = initial_balance
    current_bet = base_bet

    for r in range(rounds):
        if balance < current_bet:
            break

        # Result of the simulation (0 = loss, 1 = win)
        result = random.choice([0, 1])  # 0 = loss, 1 = win

        if result == 1:  # Win
            balance += current_bet
            current_bet = max(1, current_bet - bet_change)  # Decrease of the bet
        else:  # Loss
            balance -= current_bet
            current_bet += bet_change  # Increase of the bet

    return balance

def always_bet_the_same(initial_balance, base_bet, rounds):
    balance = initial_balance
    current_bet = base_bet

    for r in range(rounds):
        if balance < current_bet:
            break

        # Result of the simulation (0 = loss, 1 = win)
        result = random.choice([0, 1])  # 0 = loss, 1 = win

        if result == 1:  # Win
            balance += current_bet
        else:  # Loss
            balance -= current_bet

    return balance

def random_bet_change(initial_balance, base_bet, rounds, bet_change):
    balance = initial_balance
    current_bet = base_bet

    for r in range(rounds):
        if balance < current_bet:
            break

        # Result of the simulation (0 = loss, 1 = win)
        result = random.choice([0, 1])  # 0 = loss, 1 = win

        if result == 1:  # Win
            balance += current_bet
        else:  # Loss
            balance -= current_bet

        current_bet = random.choice([current_bet + bet_change, max(1, current_bet-bet_change)])

    return balance

if __name__ == "__main__":
    main()

