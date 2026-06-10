import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Define your matrix pins (adjust to match your wiring)
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define what each key does
keyboard.keymap = [
    [KC.A, KC.B, KC.C],
]

if __name__ == "__main__":
    keyboard.go()
