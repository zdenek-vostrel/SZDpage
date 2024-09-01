#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <TH1D.h> // ROOT histogram class
#include <TROOT.h> // ROOT main class

// Main function to simulate D'Alembert's strategy
void DAlemberts_strategy() {
    // Load ROOT macros for styling
    gROOT->LoadMacro("/home/mira/local/atlasstyle-00-03-05/AtlasStyle.C");
    gROOT->LoadMacro("/home/mira/local/atlasstyle-00-03-05/AtlasUtils.C");

    // Declare a histogram to store results
    TH1D* h_total;

    int super_total = 0; // Variable to accumulate total results
    int pocet_her = 100; // Number of games to simulate

    // Initialize histogram for total results
    h_total = new TH1D("total", "total", 100, 0.5, 100.5);
    h_total->SetXTitle("Number of Bets");
    h_total->SetYTitle("Total Amount");
    h_total->Sumw2(); // Enable error calculation for the histogram

    // Loop through the number of games
    for (int n = 1; n <= pocet_her; n++) {
        int total = 200; // Starting capital
        int bet = 10;    // Initial bet amount
        int min_bet = 1; // Minimum bet amount

        // Simulate 100 rounds of betting
        for (int i = 1; i <= 100; i++) {
            // Check if the bet is valid
            if (bet < min_bet || total < bet) break;

            // Generate a random outcome (0 = loss, or 1 = win)
            int j = rand() % 2;

            // Update total and bet based on the outcome
            if (j == 0) { // Loss
                total -= bet; // Lose the bet
                bet++;        // Increase the bet for the next round
            } else { // Win
                total += bet; // Win the bet
                bet--;        // Decrease the bet for the snext round
            }
        }

        // Accumulate the total results
        super_total += total;
        h_total->Fill((n - 0.5), total); // Fill histogram with the total for this game
    }

    // Adjust super_total by subtracting the initial capital for all games
    super_total -= (pocet_her * 200);
    std::cout << super_total << std::endl; // Output the final result
    h_total->Draw("hist"); // Draw the histogram
}
