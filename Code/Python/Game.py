import cv2
import time
import tkinter
m = tkinter.Tk()
def quit():
    m.destroy()
def gameUI():
    w = tkinter.Label(m, text='MurderBobADVANCED')
    ww = tkinter.Button(m, text='Play', width=25, command=lambda: cutscene1())
    w.pack()
    ww.pack()
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
def game():
    # ill MAYBE try to translate this into UI but idk....
    print("MurderbobADVANCED")
    print("A new era for MurderBob.")
    print("Play")
    print("Settings")
    print("Credits")
    opt = input("")
    if (opt == "Play" or opt == "play"):
        cutscene1()
        cutscene2()
    if (opt == "Settings" or opt == "settings"):
        print("Nothing's here.. greg")
        print("-----------------------------------------")
        game()
    if (opt == "Credits" or opt == "credits"):
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
        game()
gameUI()