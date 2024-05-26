from tkinter import *
import random

root = Tk()
root.geometry('1280x720')
root.title("Shape Application")

frameHome = None
frameLesson = None

def frameHomePage():
    global frameHome
    frameHome = Frame(root)
    heading = Label(frameHome, text="Learn about Shapes")
    buttonLesson = Button(frameHome, text="Start Lesson", command = frameLessonPage)
    buttonQuiz = Button(frameHome, text="Start Quiz")
    buttonOptions = Button(frameHome, text="Options")
    buttonExit = Button(frameHome, text="Exit", command=root.quit)

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

    heading.grid(row = 0, column = 1)

    frameHome.pack_forget()
    frameLesson.pack()
    
frameHomePage()
root.mainloop()
