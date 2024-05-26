from tkinter import *
import random

root = Tk()

def removeFrame(frame)
    frame.grid_forget()

frameHome = LabelFrame(root)
frameHome.pack(padx=10, pady=10)

heading = Label(frameHome, text="Learn about Shapes")
buttonLesson = Button(frameHome, text="Start Lesson")
buttonQuiz = Button(frameHome, text="Start Quiz")
buttonOptions = Button(frameHome, text="Options")
buttonExit = Button(frameHome, text="Exit")

heading.grid(row = 0, column = 1)
buttonLesson.grid(row = 1, column = 1)
buttonQuiz.grid(row = 2, column = 1)
buttonOptions.grid(row = 3, column = 1)
buttonExit.grid(row = 4, column = 1, command=root.quit)

root.mainloop()
