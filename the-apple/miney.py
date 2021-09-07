import keyboard, os
while True:
    if keyboard.is_pressed("ctrl+t"):
        try:
            os.system("taskkill /IM 'javaw.exe' /F")
        except:
            pass
    else:
        pass