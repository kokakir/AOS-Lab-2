
import msvcrt

x = msvcrt.kbhit()
if x:
    k = ord(msvcrt.getch())
    if k == 101:
        print("Нажата E")