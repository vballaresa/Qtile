from libqtile.config import key
from libqtile.command import lazy

keys =[

    # Movimiento del foco
    key(["mod4"], "j", lazy.layout.left()),
    key(["mod4"], "k", lazy.layout.down()),
    key(["mod4"], "l", lazy.layout.right()),
    key(["mod4"], "i", lazy.layout.up()),

    # Movimiento de ventanas
    key(["mod4", "shift"], "j", lazy.layout.shuffle_left()),
    key(["mod4", "shift"], "k", lazy.layout.shuffle_down()),
    key(["mod4", "shift"], "l", lazy.layout.shuffle_right()),
    key(["mod4", "shift"], "i", lazy.layout.shuffle_up()),

    # Controles de ventana
    key(["mod4"], "m", lazy.window.kill()),
    key(["mod4"], "n", lazy.window.toggle_fullscreen()),
    ]