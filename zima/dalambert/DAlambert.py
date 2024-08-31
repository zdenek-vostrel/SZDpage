import random
import matplotlib.pyplot as plt
import numpy as np
import pathlib

def main():
    # Parameters
    initial_balance = 100           # Initial balance
    base_bet = 10                   # Initiabl bet
    rounds = 20                     # Maximum number of rounds
    number_of_simulations = 500     # Nummber of simulations

    # Results       
    final_balance_DAlambert = []    
    final_balance_sameBet = []   
    final_balance_randomBet = []    

    for sim in range(number_of_simulations):
        # Start of the simulation
        final_balance_DAlambert += [d_alembert_strategy(initial_balance, base_bet, rounds)]
        final_balance_sameBet += [d_alembert_strategy(initial_balance, base_bet, rounds)]
        final_balance_randomBet += [d_alembert_strategy(initial_balance, base_bet, rounds)]

    plot(final_balance_DAlambert, final_balance_sameBet, final_balance_randomBet, initial_balance)

def plot(final_balance_DAlambert, final_balance_sameBet, final_balance_randomBet, initial_balance):
    fig, ax = plt.subplots()

    x = np.arange(len(final_balance_DAlambert))+1

    ax.hist(x, bins=x, weights=final_balance_DAlambert, align="mid", histtype="step", facecolor="none", alpha=.5, label="D'Alambert")
    m = np.mean(final_balance_DAlambert)
    ax.plot([x[0], x[-1]], [m,m], linestyle="--", c="C0", label=f"D'Alambert mean ({m:.1f})")

    ax.hist(x, bins=x, weights=final_balance_sameBet, align="mid", histtype="step", facecolor="none", alpha=.5, label="Constant bet")
    m = np.mean(final_balance_sameBet)
    ax.plot([x[0], x[-1]], [m,m], linestyle="--", c="C1", label=f"Constant bet mean ({m:.1f})")

    ax.hist(x, bins=x, weights=final_balance_randomBet, align="mid", histtype="step", facecolor="none", alpha=.5, label="Random bet")
    m = np.mean(final_balance_randomBet)
    ax.plot([x[0], x[-1]], [m,m], linestyle="--", c="C2", label=f"Random bet mean ({m:.1f})")

    ax.plot([x[0], x[-1]], [initial_balance, initial_balance], linestyle="--", c="black", label="Initial balance")

    plt.ylabel("Balance at the end of the game")
    plt.xlabel("Game number")

    plt.legend()

    fName = pathlib.Path("DAlambert.png")
    fig.savefig(fName, dpi=250)

def d_alembert_strategy(initial_balance, base_bet, rounds):
    balance = initial_balance
    current_bet = base_bet

    for r in range(rounds):
        if balance < current_bet:
            break

        # Result of the simulation (0 = loss, 1 = win)
        result = random.choice([0, 1])  # 0 = loss, 1 = win

        if result == 1:  # Win
            balance += current_bet
            current_bet = max(1, current_bet - 1)  # Decrease of the bet
        else:  # Loss
            balance -= current_bet
            current_bet += 1  # Decrease of the bet

    return balance

def alway_bet_the_same(initial_balance, base_bet, rounds):
    balance = initial_balance
    current_bet = base_bet

    for r in range(rounds):
        if balance < current_bet:
            print("Not enough money to bet.")
            break

        # Result of the simulation (0 = loss, 1 = win)
        result = random.choice([0, 1])  # 0 = loss, 1 = win

        if result == 1:  # Win
            balance += current_bet
        else:  # Loss
            balance -= current_bet

    return balance

def random_bet_change(initial_balance, base_bet, rounds):
    balance = initial_balance
    current_bet = base_bet

    for r in range(rounds):
        if balance < current_bet:
            print("Not enough money to bet.")
            break

        # Result of the simulation (0 = loss, 1 = win)
        result = random.choice([0, 1])  # 0 = loss, 1 = win

        if result == 1:  # Win
            balance += current_bet
        else:  # Loss
            balance -= current_bet

        current_bet = random.choice([current_bet + 1, max(1, current_bet-1)])

    return balance

if __name__ == "__main__":
    main()

