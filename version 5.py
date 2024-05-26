from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk,Image
import ttkbootstrap as ttk

#Initialise the main application window
root = Tk()
root.geometry('1280x720')
root.title("Shape Application")

#Initialise global variables for frames and question amount
frameHome = None
frameLesson = None
frameQuiz = None

questionAmount = 5

#Class to represent each shape with its properties
class Shape:
        def __init__(self, name, sides, corners, image):
            self.name = name
            self.sides = sides
            self.corners = corners
            self.image = image

#Image List, load images for the shapes
circleImg = ImageTk.PhotoImage(Image.open("1.png"))
triangleImg = ImageTk.PhotoImage(Image.open("3.png"))
squareImg = ImageTk.PhotoImage(Image.open("5.png"))
pentagonImg = ImageTk.PhotoImage(Image.open("7.png"))
hexagonImg = ImageTk.PhotoImage(Image.open("9.png"))
octagonImg = ImageTk.PhotoImage(Image.open("11.png"))

#Create a list of shape objects
shapeList = []
shapeList.append(Shape("Circle", 0, 0, circleImg))
shapeList.append(Shape("Triangle", 3, 3, triangleImg))
shapeList.append(Shape("Square", 4, 4, squareImg))
shapeList.append(Shape("Pentagon", 5, 5, pentagonImg))
shapeList.append(Shape("Hexagon", 6, 6, hexagonImg))
shapeList.append(Shape("Octagon", 8, 8, octagonImg))
def frameHomePage():
    global frameHome
    global frameLesson
    frameHome = Frame(root)

    #Home page widgets
    heading = Label(frameHome, text="Welcome to the Shape Application!")
    buttonLesson = Button(frameHome, text="Start Lesson", command = lambda:[frameLessonPage(),frameHome.pack_forget()])
    buttonQuiz = Button(frameHome, text="Start Quiz", command = lambda:[frameQuizPage(),frameHome.pack_forget()])
    buttonOptions = Button(frameHome, text="Options")
    buttonExit = Button(frameHome, text="Exit", command=root.quit)

    #Layout the widgets
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

    heading = Label(frameLesson, text="Shape Lesson")
    buttonReturn = Button(frameLesson, text = "Return", command = lambda:[frameHomePage(),frameLesson.pack_forget()])
   
    global myLabel
    myLabel = Label(frameLesson, image = circleImg)
    myLabel.image = circleImg
    
    #Layout the widgets
    heading.grid(row = 0, column = 1)
    buttonReturn.grid(row = 2, column = 1)
    myLabel.grid(row = 1, column = 1)
  
    buttonExit = Button(frameLesson, text = "Exit", command=root.quit)
    buttonForward = Button(frameLesson, text = ">>", command = lambda: forward(2))

    buttonExit.grid(row = 3, column = 1)
    buttonForward.grid(row = 3, column = 2)

    def forward(imageNumber):
        global myLabel

        #Remove current image and display the next
        myLabel.grid_forget()

        myLabel = Label(frameLesson, image=shapeList[imageNumber - 1].image)
        myLabel.grid(row=1, column=1)

        #update forward button command
        buttonForward = Button(frameLesson, text=">>", command=lambda: forward(imageNumber + 1 if imageNumber < len(shapeList) else 1))

        buttonForward.grid(row=3, column=2)
   
    frameLesson.pack()

def frameQuizPage():
    global frameQuiz
    global questionIndex
    global randomShape
    global score

    score = 0
    questionIndex = 0
    randomShape = list(range(len(shapeList)))
    random.shuffle(randomShape)

    frameQuiz = Frame(root)
    heading = Label(frameQuiz, text="Shape Quiz")
    buttonReturn = Button(frameQuiz, text = "Return", command = lambda:[frameHomePage(),frameQuiz.pack_forget()])

    heading.grid(row = 0, column = 1)
    buttonReturn.grid(row = 5, column = 1)
    DisplayQuestion()

def DisplayQuestion():
    global frameQuiz, questionAmount, questionIndex, randomShape

    questionList = ["What shape is this?"]
    print("index " + str(questionIndex))
    print ("score " + str(score))

    #Display the question and shape image
    labelQuestion = Label(frameQuiz, text=questionList[0])
    labelQuestion.grid(row = 1, column = 1)

    labelShapeImage = Label(frameQuiz, image=shapeList[randomShape[questionIndex]].image)
    labelShapeImage.grid(row = 2, column = 1)

    #Input field for the answer
    entryAnswer = Entry(frameQuiz)
    entryAnswer.grid(row = 3, column = 1)

    #Submit button to check the answer
    buttonSubmit = Button(frameQuiz, text="Submit", command=lambda:[SubmitAnswer(entryAnswer.get(), shapeList[randomShape[questionIndex]])])
    buttonSubmit.grid(row = 4, column = 1)

    frameQuiz.pack()

def SubmitAnswer(answer, shape):
    global score, questionIndex, frameQuiz
    if answer.lower() == shape.name.lower():
        score += 1
    questionIndex += 1

    if questionIndex < questionAmount:
        DisplayQuestion()
    else:
        messagebox.showinfo("Results", f"You scored: {score} out of {questionAmount}")
        frameQuiz.pack_forget()
        frameHomePage()

#Initialise the application with the home page
frameHomePage()
root.mainloop()
