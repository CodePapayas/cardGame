Blackjack Game in Python

This project is a simple implementation of the Blackjack card game (also known as 21) in Python. It features basic game mechanics like shuffling and dealing cards, player actions (hit/stand), and evaluating the game state to determine wins or losses.
Current Features

    Deck Creation and Shuffling: Utilizes a PlayCard class to represent individual cards and a function to create a shuffled deck.
    Initial Dealing: Automatically deals two cards to both the player and the dealer at the start of the game.
    Player Actions: Allows the player to hit (request additional cards).

How to Run

TBD
Next Steps
Immediate To-Dos

    Implement check_game_state(): Calculate and update the total value of the hands for both the player and the dealer. This includes handling Aces correctly as either 1 or 11.
    Determine Win/Loss Conditions: Add logic to check_game_state() or another appropriate method to determine if the player or dealer has won or lost after each action.

Future Enhancements

    Dealer Logic: Implement the dealer's logic to hit until reaching a soft 17.
    Splitting Pairs: Allow players to split pairs into separate hands for additional betting.
    Double Down: Implement the option for players to double down on their bet under certain conditions.
    User Interface: Develop a more sophisticated user interface, potentially moving from console to a graphical UI.
    Multiplayer Support: Extend the game to support multiple players against the dealer.
