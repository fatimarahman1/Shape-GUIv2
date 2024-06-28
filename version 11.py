import customtkinter as ctk
from tkinter import messagebox
import random
from PIL import Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
# Initialise the main application window
root = ctk.CTk()
root.geometry('1500x950')
root.title("Shape Application")

# Initialise global variables for frames and question amount
frameHome = None
frameLesson = None
frameQuiz = None
frameOptions = None

questionAmount = 10
chosenAnswer = ctk.IntVar(value=0)  # Initialize with a default value
currentWidgets = []
currentScale = 1.0

# Class to represent each shape with its properties
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

# Load images for the shapes using CTkImage
circleImg = ctk.CTkImage(light_image=Image.open("1.png"),
                         dark_image=Image.open("2.png"),
                         size=(500,500))
triangleImg = ctk.CTkImage(light_image=Image.open("3.png"),
                         dark_image=Image.open("4.png"),
                         size=(500,500))
squareImg = ctk.CTkImage(light_image=Image.open("5.png"),
                         dark_image=Image.open("6.png"),
                         size=(500,500))
pentagonImg = ctk.CTkImage(light_image=Image.open("7.png"),
                         dark_image=Image.open("8.png"),
                         size=(500,500))
hexagonImg = ctk.CTkImage(light_image=Image.open("9.png"),
                         dark_image=Image.open("10.png"),
                         size=(500,500))
octagonImg = ctk.CTkImage(light_image=Image.open("11.png"),
                         dark_image=Image.open("12.png"),
                         size=(500,500))

# Create a list of shape objects
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

def scaleFonts(frame, scale):
    for widget in frame.winfo_children():
        if isinstance(widget, ctk.CTkLabel):
            widget.configure(font=("Arial", int(12 * scale)))
        elif isinstance(widget, ctk.CTkButton):
            widget.configure(font=("Arial", int(12 * scale)))
        elif isinstance(widget, ctk.CTkEntry):
            widget.configure(font=("Arial", int(12 * scale)))

def frameHomePage():
    global frameHome
    global frameLesson
    frameHome = ctk.CTkFrame(root, width=1200, height=1200, fg_color="transparent")

    # Home page widgets
    heading = ctk.CTkLabel(frameHome, text="Welcome to the Shape Application!")
    buttonLesson = ctk.CTkButton(frameHome, text="Start Lesson", command=lambda: [frameLessonPage(), frameHome.destroy()])
    buttonQuiz = ctk.CTkButton(frameHome, text="Start Quiz", command=lambda: [frameQuizPage(), frameHome.destroy()])
    buttonOptions = ctk.CTkButton(frameHome, text="Options", command=OptionsMenu)
    buttonExit = ctk.CTkButton(frameHome, text="Exit", command=root.quit)

    # Layout the widgets
    heading.grid(row=0, column=1)
    buttonLesson.grid(row=1, column=1, padx=50, pady=20)
    buttonQuiz.grid(row=2, column=1, padx=50, pady=20)
    buttonOptions.grid(row=0, column=0, padx=0, pady=0)
    buttonExit.grid(row=4, column=1, pady=10)

    frameHome.pack(padx=20, pady=20)

def frameLessonPage():
    global frameLesson
    frameLesson = ctk.CTkFrame(root, fg_color="transparent")

    heading = ctk.CTkLabel(frameLesson, text="Shape Lesson")
    buttonReturn = ctk.CTkButton(frameLesson, text="Return", command=lambda: [frameHomePage(), frameLesson.destroy()])

    global myLabel
    myLabel = ctk.CTkLabel(frameLesson, image=shapeList[0].image)

    shapeNameLabel = ctk.CTkLabel(frameLesson, text=(f"This is a  {shapeList[0].name}"))




    # Layout the widgets
    heading.grid(row=0, column=1, pady=10)
    buttonReturn.grid(row=2, column=1, pady=10)
    myLabel.grid(row=1, column=1, pady=10)
    shapeNameLabel.grid(row=1, column=2, pady=5, sticky="w")

    buttonForward = ctk.CTkButton(frameLesson, text=">>", command=lambda: forward(2))
    buttonForward.grid(row=3, column=2, pady=10)

    def forward(imageNumber):
        global myLabel

        # Remove current image and display the next
        myLabel.destroy()

        myLabel = ctk.CTkLabel(frameLesson, image=shapeList[imageNumber - 1].image)
        myLabel.grid(row=1, column=1, pady=10)

        # Update forward button command
        buttonForward = ctk.CTkButton(frameLesson,
                                      text=">>",
                                      command=lambda: forward(imageNumber + 1 if imageNumber < len(shapeList) else 1))
        buttonForward.grid(row=3, column=2, pady=10)

    frameLesson.pack(padx=20, pady=20)

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
        randomInt = random.randint(0, len(question_types) - 1)
        randomQuestionTypeIndex.append(randomInt)
    print(randomQuestionTypeIndex)

    frameQuiz = ctk.CTkFrame(root, fg_color="transparent")
    heading = ctk.CTkLabel(frameQuiz, text="Shape Quiz")
    buttonReturn = ctk.CTkButton(frameQuiz, text="Return", command=lambda: [frameHomePage(), frameQuiz.destroy()])

    heading.grid(row=0, column=1, pady=10)
    buttonReturn.grid(row=8, column=1, pady=10)
    DisplayQuestion(randomQuestionTypeIndex, chosenAnswer)

def OptionsMenu():
    themes = ["Light", "Dark"]
    textSize = ["50%", "100%", "150%"]

    def changeTheme(choice):
        ctk.set_appearance_mode(choice)

    def changeSize(choice):
        global currentScale
        if choice == "50%":
            currentScale = 0.5
        elif choice == "100%":
            currentScale = 1.0
        elif choice == "150%":
            currentScale = 1.5

        # Resize fonts in the current frames
        if frameHome:
            scaleFonts(frameHome, currentScale)
        if frameLesson:
            scaleFonts(frameLesson, currentScale)
        if frameQuiz:
            scaleFonts(frameQuiz, currentScale)

    myOption = ctk.CTkOptionMenu(root, values=themes,
                                 command=changeTheme)
    myOption.pack(pady=10)

    myOption1 = ctk.CTkOptionMenu(root, values=textSize,
                                  command=changeSize)
    myOption1.pack(pady=10)

def DisplayQuestion(randomQuestionTypeIndex, chosenAnswer):
    global frameQuiz, questionAmount, questionIndex, randomShape, currentWidgets

    modifiedQuestionIndex = questionIndex
    if questionIndex >= len(shapeList):
        modifiedQuestionIndex = questionIndex % len(shapeList)

    for widget in currentWidgets:
        widget.destroy()
    currentWidgets.clear()

    if randomQuestionTypeIndex[questionIndex] == 0:
        # Display the question and shape image
        labelQuestion = ctk.CTkLabel(frameQuiz, text=questionList[randomQuestionTypeIndex[questionIndex]].text)
        labelQuestion.grid(row=1, column=1, pady=10)
        currentWidgets.append(labelQuestion)

        labelShapeImage = ctk.CTkLabel(frameQuiz, image=shapeList[randomShape[modifiedQuestionIndex]].image)
        labelShapeImage.grid(row=2, column=1, pady=10)
        currentWidgets.append(labelShapeImage)

        # Input field for the answer
        entryAnswer = ctk.CTkEntry(frameQuiz)
        entryAnswer.grid(row=3, column=1, pady=10)
        currentWidgets.append(entryAnswer)

        # Submit button to check the answer
        buttonSubmit = ctk.CTkButton(frameQuiz,
                                     text="Submit",
                                     command=lambda: [SubmitAnswer(entryAnswer.get(),
                                                                   shapeList[randomShape[modifiedQuestionIndex]],
                                                                   randomQuestionTypeIndex)])
        buttonSubmit.grid(row=4, column=1, pady=10)
        currentWidgets.append(buttonSubmit)

    if randomQuestionTypeIndex[questionIndex] == 1:
        # Display the question and shape image
        labelQuestion = ctk.CTkLabel(frameQuiz, text=questionList[randomQuestionTypeIndex[questionIndex]].text)
        labelQuestion.grid(row=1, column=1, pady=10)
        currentWidgets.append(labelQuestion)

        labelShapeImage = ctk.CTkLabel(frameQuiz, image=shapeList[randomShape[modifiedQuestionIndex]].image)
        labelShapeImage.grid(row=2, column=1, pady=10)
        currentWidgets.append(labelShapeImage)

        wrongShapesList = [shape for shape in shapeList if shape != shapeList[randomShape[modifiedQuestionIndex]]]
        choices = random.sample(wrongShapesList, 3)
        choices.append(shapeList[randomShape[modifiedQuestionIndex]])
        random.shuffle(choices)
        chosenAnswer.set(0)

        for r in range(4):
            rb = ctk.CTkRadioButton(frameQuiz, text=choices[r].corners, variable=chosenAnswer, value=choices[r].corners)
            rb.grid(row=r + 3, column=1, sticky="W", pady=10)
            currentWidgets.append(rb)

        # Submit button to check the answer
        buttonSubmit = ctk.CTkButton(frameQuiz,
                                     text="Submit",
                                     command=lambda: [SubmitAnswer(chosenAnswer.get(),
                                                                   shapeList[randomShape[modifiedQuestionIndex]],
                                                                   randomQuestionTypeIndex)])
        buttonSubmit.grid(row=7, column=1, pady=10)
        currentWidgets.append(buttonSubmit)

    if randomQuestionTypeIndex[questionIndex] == 2:
        # Display the question and shape image
        labelQuestion = ctk.CTkLabel(frameQuiz, text=questionList[randomQuestionTypeIndex[questionIndex]].text)
        labelQuestion.grid(row=1, column=1, pady=10)
        currentWidgets.append(labelQuestion)

        labelShapeImage = ctk.CTkLabel(frameQuiz, image=shapeList[randomShape[modifiedQuestionIndex]].image)
        labelShapeImage.grid(row=2, column=1, pady=10)
        currentWidgets.append(labelShapeImage)

        wrongShapesList = [shape for shape in shapeList if shape != shapeList[randomShape[modifiedQuestionIndex]]]
        choices = random.sample(wrongShapesList, 3)
        choices.append(shapeList[randomShape[modifiedQuestionIndex]])
        random.shuffle(choices)
        chosenAnswer.set(0)

        for r in range(4):
            rb = ctk.CTkRadioButton(frameQuiz, text=choices[r].angleSum,
                                    variable=chosenAnswer,
                                    value=choices[r].angleSum)
            rb.grid(row=r + 3, column=1, sticky="W", pady=10)
            currentWidgets.append(rb)

        # Submit button to check the answer
        buttonSubmit = ctk.CTkButton(frameQuiz,
                                     text="Submit",
                                     command=lambda: [SubmitAnswer(chosenAnswer.get(),
                                                                   shapeList[randomShape[modifiedQuestionIndex]],
                                                                   randomQuestionTypeIndex)])
        buttonSubmit.grid(row=7, column=1, pady=10)
        currentWidgets.append(buttonSubmit)

    frameQuiz.pack(padx=20, pady=20)

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

# Initialise the application with the home page
frameHomePage()
root.mainloop()
