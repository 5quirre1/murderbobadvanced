import cv2
import time
import tkinter
def credits():
    m.destroy
    print("Credits")
    time.sleep(2)
    print("Thanks to Python and YouTube Music for making the grind possible 🔥")
    time.sleep(2)
    print("Thanks Google Slides for being a place to create cutscenes! :D")
    time.sleep(2)
    print("And now... for the people!")
    time.sleep(2)
    print("Give a standing ovation to:")
    time.sleep(2)
    print("Squirrel, for creating the original game, MurderBob, creating this idea, and for pretty much everything else too!")
    time.sleep(2)
    print("Names, for creating the cutscenes and lore!")
    time.sleep(2)
    print("Wish, for creating the Python version, cutscenes, and lore!")
    time.sleep(2)
    print("Hypercuber and Spruce for creating some of the graphics we use!")
    time.sleep(2)
    print("You, for always helping our journey and supporting us.")
    time.sleep(2)
    print("Thanks :) - Wish")
    print("-----------------------------")
    time.sleep(5)
    gameUI()
def quitMain():
    m.destroy()
def quitSettings():
    h.destroy()
def settingsUI():
    global h 
    h = tkinter.Tk()
    w = tkinter.Label(h, text="Settings")
    ww = tkinter.Label(h, text="sorry nothing is here yet")
    www = tkinter.Button(h, text='Exit', width=25, command=lambda: quitSettings())
    w.pack()
    ww.pack()
    www.pack()
def gameUI():
    global m 
    m = tkinter.Tk()
    w = tkinter.Label(m, text='MurderBobADVANCED')
    ww = tkinter.Button(m, text='Play', width=25, command=lambda: cutscene1())
    www = tkinter.Button(m, text='Credits', width=25, command=lambda: credits())
    wwww = tkinter.Button(m, text="Settings", width=25, command=lambda: settingsUI())
    wwwww = tkinter.Button(m, text="Quit", width=25, command=lambda: quitMain())
    w.pack()
    ww.pack()
    www.pack()
    wwww.pack()
    wwwww.pack()
    m.mainloop()
def cutscene1():
    quit()
    cap = cv2.VideoCapture('cutscenes/cutscene1.mp4')
    if (cap.isOpened()== False):
        print("Error opening video file")

    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('MurderbobADVANCED | Cutscene 1', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cutscene2()
def cutscene2():
    cap = cv2.VideoCapture('cutscenes/cutscene2.mp4')
    if (cap.isOpened()== False):
        print("Error opening video file")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('MurderbobADVANCED | Cutscene 2', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
gameUI()