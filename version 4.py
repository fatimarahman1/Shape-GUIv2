from tkinter import *
import random
from PIL import ImageTk,Image

root = Tk()
root.geometry('1280x720')
root.title("Shape Application")

frameHome = None
frameLesson = None
frameQuiz = None

def frameHomePage():
    global frameHome
    global frameLesson
    frameHome = Frame(root)
    heading = Label(frameHome, text="Welcome to the Shape Application!")
    buttonLesson = Button(frameHome, text="Start Lesson", command = lambda:[frameLessonPage(),frameHome.pack_forget()])
    buttonQuiz = Button(frameHome, text="Start Quiz", command = lambda:[frameQuizPage(),frameHome.pack_forget()])
    buttonOptions = Button(frameHome, text="Options")
    buttonExit = Button(frameHome, text="Exit", command=root.quit)

    heading.grid(row = 0, column = 1)
    buttonLesson.grid(row = 1, column = 1)
    buttonQuiz.grid(row = 2, column = 1)
    buttonOptions.grid(row = 3, column = 1)
    buttonExit.grid(row = 4, column = 1)

    #frameLesson.pack_forget()
    frameHome.pack()
    

def frameLessonPage():
    global frameLesson
    frameLesson = Frame(root)

    #Image List
    circleImg = ImageTk.PhotoImage(Image.open("1.png"))
    triangleImg = ImageTk.PhotoImage(Image.open("3.png"))
    squareImg = ImageTk.PhotoImage(Image.open("5.png"))
    pentagonImg = ImageTk.PhotoImage(Image.open("7.png"))
    hexagonImg = ImageTk.PhotoImage(Image.open("9.png"))
    octagonImg = ImageTk.PhotoImage(Image.open("11.png"))

    imageList = [circleImg, triangleImg, squareImg, pentagonImg, hexagonImg, octagonImg]
    imageNames = ["Circle", "Triangle", "Square", "Pentagon", "Hexagon", "Octagon"]
    imageSides = [0,3,4,5,6,8]
    imageCorners = [0,3,4,5,6,8]
    
    heading = Label(frameLesson, text="Shape Lesson")
    buttonReturn = Button(frameLesson, text = "Return", command = lambda:[frameHomePage(),frameLesson.pack_forget()])
   
    global myLabel
    myLabel = Label(frameLesson, image = circleImg)
    myLabel.image = circleImg
    
    heading.grid(row = 0, column = 1)
    buttonReturn.grid(row = 2, column = 1)
    myLabel.grid(row = 1, column = 1)
  
    #buttonBack = Button(frameLesson, text = "<<", command =  lambda: back)
    buttonExit = Button(frameLesson, text = "Exit", command=root.quit)
    buttonForward = Button(frameLesson, text = ">>", command = lambda: forward(2))

    #buttonBack.grid(row = 3, column = 0)
    buttonExit.grid(row = 3, column = 1)
    buttonForward.grid(row = 3, column = 2)

    def forward(imageNumber):
        global myLabel

        myLabel.grid_forget()

        myLabel = Label(frameLesson, image=imageList[imageNumber - 1])
        myLabel.grid(row=1, column=1)

        buttonForward = Button(frameLesson, text=">>", command=lambda: forward(imageNumber + 1 if imageNumber < len(imageList) else 1))

        buttonForward.grid(row=3, column=2)
   
    frameLesson.pack()

def frameQuizPage():
    global frameQuiz
    frameQuiz = Frame(root)
    heading = Label (frameQuiz, text="Shape Quiz")
    buttonReturn = Button(frameQuiz, text = "Return", command = lambda:[frameHomePage(),frameQuiz.pack_forget()])

    heading.grid(row = 0, column = 1)
    buttonReturn.grid(row = 1, column = 1)

    frameQuiz.pack()
    
frameHomePage()
root.mainloop()
