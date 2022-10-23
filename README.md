# War_Card_Game_Console
This is console version of the card game known as War. It should only be treated as a demonstration of my skillset and my expeience, since it essentially plays itself.
It is made as a exercise to practice object oriented programming.

<h1>Summary</h1>
The game is enclosed within one python file.

The first part of it contains classes and functions which are describing objects taking part in the game. They are as follows:

<strong>Deck</strong> - object of a card deck which contains functions for creating a deck, shuffling it and distributing cards to players

<strong>Hand</strong> - object of a hand. Every player has a hand that contains 26 cards (deck of 52 cards is splitted in half). It can add or remove cards

<strong>Player</strong> - object of a player that can play cards or check if they still has cards to play

<h1>Rules of the game</h1>
War is relatively simple game. Each player has on their hand 26 cards that they draw one at the time. The player whose card has higher rank wins and the winner takes both cards. However, if players draw cards with identical rank, it starts the war. In this scenario players have to put another card from their deck face down on the already drawn cards. And then, one more, on top of these two, but this time face up. Rank of the last cards is compared and the higher rank wins. In this game we ommit case of multiple war. The game continues until one of the players remain without a cards.

<h1>How to run the game</h1>
<ol type="1">
    <li>Select the code editor of your choice (I use Visual Studio Code)</li>
    <li>Copy the repository to your new catalogue - use `git clone link_to_repository` command</li>
    <li>Select interpreter for your version of python</li>
    <li>Enter directory with the <strong>war.py</strong> file inside</li>
    <li>Run program with following command: <em>python war.py</em></li>
</ol>