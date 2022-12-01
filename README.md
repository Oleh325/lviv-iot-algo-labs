## Lab 1

Task: Implement a deletion method for an AVL tree.

## Lab 2

Task: Implement a flood fill algorithm.

Flood fill algorithm takes in three parameters: starting node, target color and replacement color.

The format of the data in the input file _input.txt_:
- first row: height and width of the field that contains the colored elements (separated by commas).
- second row: coordinates of the starting pixel from which the color change should start.
- third row: replacement color.
- fourth row and lower: array of colored elements.

The _output.txt_ files hould contain the color values of the field cells after performing the replacement.

## Lab 3

Beer

An outsourced company (one of the market leaders) is preparing for a corporate event. The HR department sent a questionnaire about the types of beer that can be distributed at the holiday. Most of the company's employees like a few types of beer, and will be very offended if at least one of the beers they like is not available at the party. Since you are the market leader, you cannot insult your employees.
On the other hand, buying all possible types of beer is expensive.

Task: find out how many different types of beer you need to bring to the corporate party.

Incoming data:
The first line contains the numbers N - the number of employees and B - the number of available beers. The second line contains N*B letters N or Y. If letter i*N + j - Y, then employee i likes beer j

Output data:
The smallest number of types of beer that should be on the holiday

Limitation:
Every employee likes at least one type of beer
0 < N < 50
0 < B < 50

## Lab 4

WChain

Two participants play a linguistic game. At the beginning of the game, a list of N words is given. The first player chooses an arbitrary word w1 and crosses out one arbitrary letter from it so to get another word w2 from this list. After that, the turn goes to another player, and he tries to do the same with the word w2. The game ends in one of two cases:
- One letter word remains.
- It is not possible to cross out any letter to get another word from the dictionary.

Task: Determine the length of the maximum chain that can be achieved in this game at given words.

Incoming data:
The first line contains N — the number of words in the dictionary. Each of the following N lines contains a word which consists of small Latin letters from a to z.

Output data:
The length of the maximum chain

Limitation:
1 ≤ N ≤ 10^5
1 ≤ L ≤ 50

## Lab 5

Create a realisation for Knuth Morris Pratt string matching algorithm and unit tests for it. Test the algorithm in it's worst case, best case and average scenario.