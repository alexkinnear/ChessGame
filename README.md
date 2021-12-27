# Chess
- Classic 1 player chess game with a greedy AI that accounts for piece and position values
- User plays as white against the cpu (black)
- the game ends when one of the kings is captured

## game.py
- UI that uses pygame to display and chessboard and handle movement logic

## piece.py
- abstract class that has Pawn, Knight, Bishop, Queen, King, Empty subclasses to represent the pieces

## greedy.py
- helper file with functions to handle AI logic for black pieces

## util.py
- helper file with functions to assist with finding valid positions