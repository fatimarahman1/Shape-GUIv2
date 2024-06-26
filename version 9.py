from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk,Image
import ttkbootstrap as ttk
from collections import Counter

#Initialise the main application window
root = Tk()
root.geometry('1280x720')
root.title("Shape Application")

#Initialise global variables for frames and question amount
frameHome = None
frameLesson = None
frameQuiz = None

questionAmount = 10
chosenAnswer = IntVar()
currentWidgets = []

#Class to represent each shape with its properties
class Shape:
    def __init__(self, name, angleSum, corners, image):
        self.name = name
        self.angleSum = angleSum
        self.corners = corners
        self.image = image

class Question:
    def __init__(self, text: str, questionType: int):
        self.text = text
        self.questionType = questionType

# Function to load images
def load_image(image_path):
    img = Image.open(image_path)
    return ImageTk.PhotoImage(img)

#Image List, load images for the shapes
circleImg = ImageTk.PhotoImage(Image.open("1.png"))
triangleImg = ImageTk.PhotoImage(Image.open("3.png"))
squareImg = ImageTk.PhotoImage(Image.open("5.png"))
pentagonImg = ImageTk.PhotoImage(Image.open("7.png"))
hexagonImg = ImageTk.PhotoImage(Image.open("9.png"))
octagonImg = ImageTk.PhotoImage(Image.open("11.png"))

#Create a list of shape objects
shapeList = []
shapeList.append(Shape("Circle", 360, 0, circleImg))
shapeList.append(Shape("Triangle", 180, 3, triangleImg))
shapeList.append(Shape("Square", 360, 4, squareImg))
shapeList.append(Shape("Pentagon", 540, 5, pentagonImg))
shapeList.append(Shape("Hexagon", 720, 6, hexagonImg))
shapeList.append(Shape("Octagon", 1080, 8, octagonImg))

questionList = []
questionList.append(Question("What is the name of this shape?", 0))
questionList.append(Question("How many corners does this shape have?", 1))
questionList.append(Question("What is the angle sum of this shape?", 2))
def frameHomePage():
    global frameHome
    global frameLesson
    frameHome = Frame(root)

    #Home page widgets
    heading = Label(frameHome, text="Welcome to the Shape Application!")
    buttonLesson = Button(frameHome, text="Start Lesson", command = lambda:[frameLessonPage(),frameHome.destroy()])
    buttonQuiz = Button(frameHome, text="Start Quiz", command = lambda:[frameQuizPage(),frameHome.destroy()])
    buttonOptions = Button(frameHome, text="Options")
    #Add button for light/dark theme and button for text enlarging/minimising
    #for dark theme command = setAppearanceMode("Dark")
    buttonExit = Button(frameHome, text="Exit", command=root.quit)

    #Layout the widgets
    heading.grid(row = 0, column = 1)
    buttonLesson.grid(row = 1, column = 1)
    buttonQuiz.grid(row = 2, column = 1)
    buttonOptions.grid(row = 3, column = 1)
    buttonExit.grid(row = 4, column = 1)

    frameHome.pack()

def frameLessonPage():
    global frameLesson
    frameLesson = Frame(root)

    heading = Label(frameLesson, text="Shape Lesson")
    buttonReturn = Button(frameLesson, text="Return", command = lambda:[frameHomePage(),frameLesson.destroy()])
   
    global myLabel
    myLabel = Label(frameLesson, image = shapeList[0].image)
    
    #Layout the widgets
    heading.grid(row = 0, column = 1)
    buttonReturn.grid(row = 2, column = 1)
    myLabel.grid(row = 1, column = 1)
  
    buttonForward = Button(frameLesson, text = ">>", command = lambda: forward(2))
    buttonForward.grid(row = 3, column = 2)

    def forward(imageNumber):
        global myLabel

        #Remove current image and display the next
        myLabel.destroy()

        myLabel = Label(frameLesson, image=shapeList[imageNumber - 1].image)
        myLabel.grid(row=1, column=1)

        #update forward button command
        buttonForward = Button(frameLesson, text=">>",
                               command=lambda: forward(imageNumber + 1 if imageNumber < len(shapeList) else 1))
        buttonForward.grid(row=3, column=2)
   
    frameLesson.pack()

def frameQuizPage():
    global frameQuiz
    global questionIndex
    global randomShape
    global score
    global chosenAnswer
    global currentWidgets

    score = 0
    questionIndex = 0
    randomShape = list(range(len(shapeList)))
    random.shuffle(randomShape)

    randomQuestionTypeIndex = []
    question_types = [question.questionType for question in questionList]
    for i in range(questionAmount):
        randomInt = random.randint(0, len(question_types)-1)
        randomQuestionTypeIndex.append(randomInt)
    print(randomQuestionTypeIndex)

    frameQuiz = Frame(root)
    heading = Label(frameQuiz, text="Shape Quiz")
    buttonReturn = Button(frameQuiz, text = "Return", command = lambda:[frameHomePage(),frameQuiz.destroy()])

    heading.grid(row = 0, column = 1)
    buttonReturn.grid(row = 8, column = 1)
    DisplayQuestion(randomQuestionTypeIndex, chosenAnswer)

def DisplayQuestion(randomQuestionTypeIndex, chosenAnswer):
    global frameQuiz, questionAmount, questionIndex, randomShape, currentWidgets

    modifiedQuestionIndex = questionIndex
    if questionIndex >= len(shapeList):
        modifiedQuestionIndex = questionIndex % len(shapeList)

    for widget in currentWidgets:
        widget.destroy()
    currentWidgets.clear()

    if randomQuestionTypeIndex[questionIndex] == 0:
        #Display the question and shape image
        labelQuestion = Label(frameQuiz, text=questionList[randomQuestionTypeIndex[questionIndex]].text)
        labelQuestion.grid(row = 1, column = 1)
        currentWidgets.append(labelQuestion)

        labelShapeImage = Label(frameQuiz, image=shapeList[randomShape[modifiedQuestionIndex]].image)
        labelShapeImage.grid(row = 2, column = 1)
        currentWidgets.append(labelShapeImage)

        #Input field for the answer
        entryAnswer = Entry(frameQuiz)
        entryAnswer.grid(row = 3, column = 1)
        currentWidgets.append(entryAnswer)

        #Submit button to check the answer
        buttonSubmit = Button(frameQuiz, text="Submit",
                              command=lambda:[SubmitAnswer(entryAnswer.get(),
                                                           shapeList[randomShape[modifiedQuestionIndex]],
                                                           randomQuestionTypeIndex)])
        buttonSubmit.grid(row = 4, column = 1)
        currentWidgets.append(buttonSubmit)

    if randomQuestionTypeIndex[questionIndex] == 1:

        # Display the question and shape image
        labelQuestion = Label(frameQuiz, text=questionList[randomQuestionTypeIndex[questionIndex]].text)
        labelQuestion.grid(row=1, column=1)
        currentWidgets.append(labelQuestion)

        labelShapeImage = Label(frameQuiz, image=shapeList[randomShape[modifiedQuestionIndex]].image)
        labelShapeImage.grid(row=2, column=1)
        currentWidgets.append(labelShapeImage)

        wrongShapesList = [shape for shape in shapeList if shape != shapeList[randomShape[modifiedQuestionIndex]]]
        choices = random.sample(wrongShapesList, 3)
        choices.append(shapeList[randomShape[modifiedQuestionIndex]])
        random.shuffle(choices)
        chosenAnswer.set(None)

        for r in range(4):
            rb = Radiobutton(frameQuiz,
                        text=choices[r].corners,
                        variable=chosenAnswer,
                        value=choices[r].corners)
            rb.grid(row=r+3, column=1, sticky="W")
            currentWidgets.append(rb)

        # Submit button to check the answer
        buttonSubmit = Button(frameQuiz,
                              text="Submit",
                              command=lambda: [SubmitAnswer(chosenAnswer.get(),
                                                            shapeList[randomShape[modifiedQuestionIndex]],
                                                            randomQuestionTypeIndex)])
        buttonSubmit.grid(row=7, column=1)
        currentWidgets.append(buttonSubmit)

    if randomQuestionTypeIndex[questionIndex] == 2:
        # Display the question and shape image
        labelQuestion = Label(frameQuiz, text=questionList[randomQuestionTypeIndex[questionIndex]].text)
        labelQuestion.grid(row=1, column=1)
        currentWidgets.append(labelQuestion)

        labelShapeImage = Label(frameQuiz, image=shapeList[randomShape[modifiedQuestionIndex]].image)
        labelShapeImage.grid(row=2, column=1)
        currentWidgets.append(labelShapeImage)

        wrongShapesList = [shape for shape in shapeList if shape != shapeList[randomShape[modifiedQuestionIndex]]]
        choices = random.sample(wrongShapesList, 3)
        choices.append(shapeList[randomShape[modifiedQuestionIndex]])
        random.shuffle(choices)
        chosenAnswer.set(None)

        for r in range(4):
            rb = Radiobutton(frameQuiz,
                        text=choices[r].angleSum,
                        variable=chosenAnswer,
                        value=choices[r].angleSum)
            rb.grid(row=r+3, column=1, sticky="W")
            currentWidgets.append(rb)

        # Submit button to check the answer
        buttonSubmit = Button(frameQuiz,
                              text="Submit",
                              command=lambda: [SubmitAnswer(chosenAnswer.get(),
                                                            shapeList[randomShape[modifiedQuestionIndex]],
                                                            randomQuestionTypeIndex)])
        buttonSubmit.grid(row=7, column=1)
        currentWidgets.append(buttonSubmit)

    frameQuiz.pack()

def SubmitAnswer(answer, shape, randomQuestionTypeIndex):
    global score, questionIndex, frameQuiz, chosenAnswer
    if randomQuestionTypeIndex[questionIndex] == 0:
        if answer.lower() == shape.name.lower():
            score += 1
        questionIndex += 1
    elif randomQuestionTypeIndex[questionIndex] == 1:
        if answer == shape.corners:
            score += 1
        questionIndex += 1
    elif randomQuestionTypeIndex[questionIndex] == 2:
        if answer == shape.angleSum:
            score += 1
        questionIndex += 1
    print(score)
    if questionIndex < questionAmount:
        DisplayQuestion(randomQuestionTypeIndex, chosenAnswer)
    else:
        messagebox.showinfo("Results", f"You scored: {score} out of {questionAmount}")
        frameQuiz.destroy()
        frameHomePage()

#Initialise the application with the home page
frameHomePage()
root.mainloop()
