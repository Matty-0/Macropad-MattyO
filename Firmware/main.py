
#imports for creating and running the keyboard command
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digitalio import DiodeLessScanner 
from kmk.keys import KC


#creates the actual keyboard
keyboard = KMKKeyboard()

#Defining what the matrix pins will do for each key
keyboard.matrix = DiodeLessScanner(
    pins=[board.D8, board.D9, board.D10]
)

#Keys are defined here telling them what to do
keyboard.keymap = [
    [KC.W, KC.A, KC.D],
]

#statement to run the command "keyboard" if the name is correct
if __name__ == "__main__":
    keyboard.go()
