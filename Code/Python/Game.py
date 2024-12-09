import cv2
def cutscene1():
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
    if (opt == "Credits" or opt == "credits"):
        print("ill cook soon - wish")
game()