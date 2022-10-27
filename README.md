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