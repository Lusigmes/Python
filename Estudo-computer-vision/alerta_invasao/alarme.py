import winsound

alarmeControl = False
def alarme():
    global alarmeControl
    for _ in range(10):
        winsound.Beep(2500,500)
    alarmeControl = False