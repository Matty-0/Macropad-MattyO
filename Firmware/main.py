#imports for creating and running the keyboard command
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC


#creates the actual keyboard
keyboard = KMKKeyboard()

#Defining what the matrix pins will do for each key
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3,)

#Keys are defined here telling them what to do
keyboard.keymap = [
    [KC.W, KC.A, KC.D],
]

#statement to run the command "keyboard" if the name is correct
if __name__ == "__main__":
    keyboard.go()
