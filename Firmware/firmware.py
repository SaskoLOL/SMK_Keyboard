from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
import board

keyboard = KMKKeyboard()

# Define column and row pins for 17x7 matrix
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16
)

keyboard.row_pins = (
    board.GP17, board.GP18, board.GP19, board.GP20,
    board.GP21, board.GP22, board.GP26  # 7 rows
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 119-key keymap layout (rows * cols order)
keyboard.keymap = [
    [
        # Row 0 (Top macro row)
        KC.M6, KC.M7, KC.M8, KC.M9, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,

        # Row 1 (Macro column, starting from second physical row)
        KC.M1, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,

        # Row 2 (Main F-row and top numbers)
        KC.M2, KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCR, KC.SLCK, KC.PAUS,

        # Row 3
        KC.M3, KC.GRAVE, KC._1, KC._2, KC._3, KC._4, KC._5, KC._6, KC._7, KC._8, KC._9, KC._0, KC.MINS, KC.EQL, KC.BSPC, KC.INS, KC.HOME,

        # Row 4
        KC.M4, KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL, KC.END,

        # Row 5
        KC.M5, KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO, KC.NO, KC.NO,

        # Row 6
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.NO, KC.NO, KC.NO, KC.NO
    ]
]
keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()