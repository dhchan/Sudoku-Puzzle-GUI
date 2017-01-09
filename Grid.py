from tkinter import *

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
var = IntVar()
buttons = []
radiobuttons = []
currentBoard = []
seconds = 0
minutes = 0
hours = 0
initializeText = "blue"
normalText = "black"
incorrectText = "red"
tileColor1 = "white"
tileColor2 = "SystemButtonFace"
clockRunning = False
timer = Label(text = "00:00:00", font = ("Helvetica", "12", "bold"))
timer.grid(row = 12, column =0, columnspan = 2)


gameTitle = Label(text = "", font = ("Helvetica", "12", "bold"))
gameTitle.grid (row = 13, columnspan = 3)

easy1 = [(0, 0, 2, "show"), (0, 1, 3, "hide"), (0, 2, 5, "show"), (0, 3, 1, "hide"), (0, 4, 4, "hide"), (0, 5, 7, "show"), (0, 6, 9, "hide"), (0, 7, 8, "hide"), (0, 8, 6, "show"), \
         (1, 0, 4, "show"), (1, 1, 1, "hide"), (1, 2, 8, "hide"), (1, 3, 9, "show"), (1, 4, 6, "show"), (1, 5, 5, "hide"), (1, 6, 7, "hide"), (1, 7, 2, "show"), (1, 8, 3, "hide"), \
         (2, 0, 6, "hide"), (2, 1, 9, "hide"), (2, 2, 7, "hide"), (2, 3, 2, "hide"), (2, 4, 8, "show"), (2, 5, 3, "hide"), (2, 6, 1, "hide"), (2, 7, 4, "show"), (2, 8, 5, "show"), \
         (3, 0, 9, "show"), (3, 1, 8, "show"), (3, 2, 6, "hide"), (3, 3, 5, "hide"), (3, 4, 7, "show"), (3, 5, 4, "show"), (3, 6, 2, "hide"), (3, 7, 3, "hide"), (3, 8, 1, "hide"), \
         (4, 0, 5, "show"), (4, 1, 7, "show"), (4, 2, 3, "hide"), (4, 3, 8, "show"), (4, 4, 1, "hide"), (4, 5, 2, "show"), (4, 6, 4, "hide"), (4, 7, 6, "show"), (4, 8, 9, "show"), \
         (5, 0, 1, "hide"), (5, 1, 4, "hide"), (5, 2, 2, "hide"), (5, 3, 6, "show"), (5, 4, 3, "show"), (5, 5, 9, "hide"), (5, 6, 8, "hide"), (5, 7, 5, "show"), (5, 8, 7, "show"), \
         (6, 0, 7, "show"), (6, 1, 5, "show"), (6, 2, 9, "hide"), (6, 3, 3, "hide"), (6, 4, 2, "show"), (6, 5, 8, "hide"), (6, 6, 6, "hide"), (6, 7, 1, "hide"), (6, 8, 4, "hide"), \
         (7, 0, 8, "hide"), (7, 1, 6, "show"), (7, 2, 4, "hide"), (7, 3, 7, "hide"), (7, 4, 5, "show"), (7, 5, 1, "show"), (7, 6, 3, "hide"), (7, 7, 9, "hide"), (7, 8, 2, "show"), \
         (8, 0, 3, "show"), (8, 1, 2, "hide"), (8, 2, 1, "hide"), (8, 3, 4, "show"), (8, 4, 9, "hide"), (8, 5, 6, "hide"), (8, 6, 5, "show"), (8, 7, 7, "hide"), (8, 8, 8, "show"), ]

easy2 = [(0, 0, 1, "show"), (0, 1, 5, "hide"), (0, 2, 2, "hide"), (0, 3, 4, "show"), (0, 4, 8, "show"), (0, 5, 9, "show"), (0, 6, 3, "hide"), (0, 7, 7, "hide"), (0, 8, 6, "show"), \
         (1, 0, 7, "show"), (1, 1, 3, "show"), (1, 2, 9, "hide"), (1, 3, 2, "hide"), (1, 4, 5, "hide"), (1, 5, 6, "hide"), (1, 6, 8, "hide"), (1, 7, 4, "show"), (1, 8, 1, "hide"), \
         (2, 0, 4, "hide"), (2, 1, 6, "hide"), (2, 2, 8, "hide"), (2, 3, 3, "hide"), (2, 4, 7, "hide"), (2, 5, 1, "show"), (2, 6, 2, "show"), (2, 7, 9, "show"), (2, 8, 5, "show"), \
         (3, 0, 3, "hide"), (3, 1, 8, "hide"), (3, 2, 7, "show"), (3, 3, 1, "show"), (3, 4, 2, "show"), (3, 5, 4, "hide"), (3, 6, 6, "show"), (3, 7, 5, "hide"), (3, 8, 9, "hide"), \
         (4, 0, 5, "show"), (4, 1, 9, "hide"), (4, 2, 1, "hide"), (4, 3, 7, "show"), (4, 4, 6, "hide"), (4, 5, 3, "show"), (4, 6, 4, "hide"), (4, 7, 2, "hide"), (4, 8, 8, "show"), \
         (5, 0, 2, "hide"), (5, 1, 4, "hide"), (5, 2, 6, "show"), (5, 3, 8, "hide"), (5, 4, 9, "show"), (5, 5, 5, "show"), (5, 6, 7, "show"), (5, 7, 1, "hide"), (5, 8, 3, "hide"), \
         (6, 0, 9, "show"), (6, 1, 1, "show"), (6, 2, 4, "show"), (6, 3, 6, "show"), (6, 4, 3, "hide"), (6, 5, 7, "hide"), (6, 6, 5, "hide"), (6, 7, 8, "hide"), (6, 8, 2, "hide"), \
         (7, 0, 6, "hide"), (7, 1, 2, "show"), (7, 2, 5, "hide"), (7, 3, 9, "hide"), (7, 4, 4, "hide"), (7, 5, 8, "hide"), (7, 6, 1, "hide"), (7, 7, 3, "show"), (7, 8, 7, "show"), \
         (8, 0, 8, "show"), (8, 1, 7, "hide"), (8, 2, 3, "hide"), (8, 3, 5, "show"), (8, 4, 1, "show"), (8, 5, 2, "show"), (8, 6, 9, "hide"), (8, 7, 6, "hide"), (8, 8, 4, "show"), ]

medium1 = [(0, 0, 1, "hide"), (0, 1, 2, "show"), (0, 2, 3, "hide"), (0, 3, 6, "show"), (0, 4, 7, "hide"), (0, 5, 8, "show"), (0, 6, 9, "hide"), (0, 7, 4, "hide"), (0, 8, 5, "hide"), \
           (1, 0, 5, "show"), (1, 1, 8, "show"), (1, 2, 4, "hide"), (1, 3, 2, "hide"), (1, 4, 3, "hide"), (1, 5, 9, "show"), (1, 6, 7, "show"), (1, 7, 6, "hide"), (1, 8, 1, "hide"), \
           (2, 0, 9, "hide"), (2, 1, 6, "hide"), (2, 2, 7, "hide"), (2, 3, 1, "hide"), (2, 4, 4, "show"), (2, 5, 5, "hide"), (2, 6, 2, "hide"), (2, 7, 2, "hide"), (2, 8, 8, "hide"), \
           (3, 0, 3, "show"), (3, 1, 7, "show"), (3, 2, 2, "hide"), (3, 3, 4, "hide"), (3, 4, 6, "hide"), (3, 5, 1, "hide"), (3, 6, 5, "show"), (3, 7, 8, "hide"), (3, 8, 9, "hide"), \
           (4, 0, 6, "show"), (4, 1, 9, "hide"), (4, 2, 1, "hide"), (4, 3, 5, "hide"), (4, 4, 8, "hide"), (4, 5, 3, "hide"), (4, 6, 2, "hide"), (4, 7, 7, "hide"), (4, 8, 4, "show"), \
           (5, 0, 4, "hide"), (5, 1, 5, "hide"), (5, 2, 8, "show"), (5, 3, 7, "hide"), (5, 4, 9, "hide"), (5, 5, 2, "hide"), (5, 6, 6, "hide"), (5, 7, 1, "show"), (5, 8, 3, "show"), \
           (6, 0, 8, "hide"), (6, 1, 3, "hide"), (6, 2, 6, "hide"), (6, 3, 9, "hide"), (6, 4, 2, "show"), (6, 5, 4, "hide"), (6, 6, 1, "hide"), (6, 7, 5, "hide"), (6, 8, 7, "hide"), \
           (7, 0, 2, "hide"), (7, 1, 1, "hide"), (7, 2, 9, "show"), (7, 3, 8, "show"), (7, 4, 5, "hide"), (7, 5, 7, "hide"), (7, 6, 4, "hide"), (7, 7, 2, "show"), (7, 8, 6, "show"), \
           (8, 0, 7, "hide"), (8, 1, 4, "hide"), (8, 2, 5, "hide"), (8, 3, 3, "show"), (8, 4, 1, "hide"), (8, 5, 6, "show"), (8, 6, 8, "hide"), (8, 7, 9, "show"), (8, 8, 2, "hide"), ]


menu = Menu(root)
root.wm_title("DChan's Sudoku")
root.config(menu = menu)

subMenu = Menu(menu)
subMenu2 = Menu(menu)
menu.add_cascade(label = "Puzzles", menu = subMenu)
menu.add_cascade(label = "Themes", menu = subMenu2)
subMenu.add_command(label = "Easy1", command = lambda game = easy1, name = "Easy1": gameStart(game, name))
subMenu.add_command(label = "Easy2", command = lambda game = easy2, name = "Easy2": gameStart(game, name))
subMenu.add_command(label = "Medium1", command = lambda game = medium1, name = "Medium1": gameStart(game, name))
subMenu2.add_command(label = "Classic", command = lambda theme = "classic": setTheme(theme))
subMenu2.add_command(label = "Black", command = lambda theme = "black": setTheme(theme))

#set up buttons
for x in range(9):
    buttons.append([])
    Grid.columnconfigure(frame, x, weight=1)
    for y in range(9):
        buttons[x].append(Button)
        buttons[x][y] = Button(frame, activebackground = "blue", command=lambda row = x, col = y: sel(row,col))
        buttons[x][y].config(height=2, width=5, font = ("Helvetica", "12", "bold"))
        buttons[x][y].grid(row=x, column=y, sticky=N+S+E+W)
        if ((x <3 or x > 5) and (y < 3 or y > 5)) or ((x >= 3 and x <= 5) and y >= 3 and y <= 5):
            buttons[x][y].config(background = "white" )
        Grid.rowconfigure(frame, y, weight=1)

def setTheme(theme):
    global normalText, initializeText, tileColor1, tileColor2, incorrectText, currentBoard
    if theme == "classic":
        normalText, initializeText, incorrectText, tileColor1, tileColor2 = "black", "blue", "red", "white", "SystemButtonFace"
    elif theme == "black":
        normalText, initializeText, incorrectText, tileColor1, tileColor2 = "white", "blue", "red", "black", "gray"
    for x in range(9):
        for y in range(9):
            buttons[x][y].config(foreground = normalText)
            if ((x < 3 or x > 5) and (y < 3 or y > 5)) or ((x >= 3 and x <= 5) and y >= 3 and y <= 5):
                buttons[x][y].config(background=tileColor1)
            else:
                buttons[x][y].config(background=tileColor2)
    for entry in currentBoard:
        if (entry[3] == "show"):
            buttons[entry[0]][entry[1]].config(foreground = initializeText)
        else:
            buttons[entry[0]][entry[1]].config(foreground = normalText)
def gameStart(puzzle, name):
    global currentBoard, seconds, hours, minutes, clockRunning, normalText, initializeText, tileColor1, tileColor2
    currentBoard = puzzle
    for entry in puzzle:
        if (entry[3] == "show"):
            buttons[entry[0]][entry[1]].config(text = str(entry[2]), foreground = initializeText)
        else:
            buttons[entry[0]][entry[1]].config(text = "", foreground = normalText)
    for x in range(9):
        for y in range(9):
            if ((x < 3 or x > 5) and (y < 3 or y > 5)) or ((x >= 3 and x <= 5) and y >= 3 and y <= 5):
                buttons[x][y].config(background=tileColor1)
            else:
                buttons[x][y].config(background=tileColor2)
    gameTitle.config(text = name)
    seconds = 0
    hours = 0
    minutes = 0
    if not clockRunning:
        update_clock()

def sel(x, y):
    #btn_text.set("A")
    #print("testing")
    global initializeText, normalText
    if buttons[x][y].cget("foreground") != initializeText:
        if var.get() != 0:
            buttons[x][y].config(text = var.get(), foreground = normalText)
        else:
            buttons[x][y].config(text = "")

for x in range(9):
    radiobuttons.append(Radiobutton(frame, text = str(x + 1), variable = var, value = x + 1, activebackground = "blue", \
                                    font = ("Helvetica", "12", "bold")))
    radiobuttons[x].grid(row = 9, column = x )

radiobuttons[0].select()

clearOne = Radiobutton(frame, text = "Erase", variable = var, value = 0, activebackground = "blue", \
                       font = ("Helvetica", "12", "bold"))
clearOne.grid(row = 10, column = 0, columnspan = 2)

def clearAll():
    for x in range(9):
        for y in range(9):
            if buttons[x][y].cget("foreground") == normalText:
                buttons[x][y].config(text = "")

def showSolution():
    global initializeText, normalText
    for entry in currentBoard:
        buttons[entry[0]][entry[1]].config(text = str(entry[2]))
        if (entry[3] == "show"):
            buttons[entry[0]][entry[1]].config(foreground = initializeText)
        else:
            buttons[entry[0]][entry[1]].config(foreground = normalText)

def checkSolution():
    global hours, minutes, seconds
    correct = True
    for entry in currentBoard:
        if str(entry[2]) != buttons[entry[0]][entry[1]].cget("text"):
            correct = False
            buttons[entry[0]][entry[1]].config(foreground = incorrectText)
    top = Toplevel()
    if correct:
        msg = Message(top, text="Correct. Time completed: %02d:%02d:%02d Choose another!" %(hours, minutes, seconds), foreground="Green", \
                      width = 100, font = ("Helvetica", "12", "bold") )
        msg.pack()
        color = ""
        for x in range(9):
            for y in range (9):
                if x + y == 0:
                    color = "light pink"
                elif x + y == 1:
                    color = "hot pink"
                elif x + y == 2:
                    color = "deep pink"
                elif x + y == 3: #has 1-4
                    color = "red"
                elif x + y == 4:
                    color = "orange red"
                elif x + y == 5:
                    color = "dark orange"
                elif x + y == 6:
                    color = "yellow"
                elif x + y == 7:
                    color = "lawn green"
                elif x + y == 8:
                    color = "green2"
                elif x + y == 9:
                    color = "deep sky blue"
                elif x + y == 10:
                    color = "turquoise"
                elif x + y == 11:
                    color = "aquamarine"
                elif x + y == 12:
                    color = "light blue"
                elif x + y == 13:
                    color = "medium purple"
                elif x + y == 14:
                    color = "purple3"
                elif x + y == 15:
                    color = "deep pink"
                elif x + y == 16:
                    color = "hot pink"
                buttons[x][y].config(background = color, foreground = "white")
    else:
        msg = Message(top, text="Incorrect", foreground=incorrectText, width = 100)
        msg.pack()
    dismissButton = Button(top, text = "Dismiss", command = top.destroy)
    dismissButton.pack()

def update_clock():
    global seconds, minutes, hours, clockRunning
    clockRunning = True
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
    timer.config(text = "%02d:%02d:%02d" %(hours, minutes,seconds))
    root.after(1000, update_clock)

def show_hint():
    for entry in currentBoard:
        if buttons[entry[0]][entry[1]].cget("text") == "":
            buttons[entry[0]][entry[1]].config(text = entry[2])
            break

clearAllButton = Button(frame, text = "CLEAR ALL", background = "dark gray", activebackground = "red", \
                        font = ("Helvetica", "12", "bold"), command=clearAll)
clearAllButton.grid(row = 10, column = 2, columnspan = 2)


hintButton = Button(frame, text = "HINT", background = "dark gray", activebackground = "blue", \
                    font = ("Helvetica", "12", "bold"), command = show_hint)
hintButton.grid(row = 10, column = 4, columnspan = 2)


solutionButton = Button(frame, text = "SOLUTION", background = "light gray", activebackground=  "green", \
                        font = ("Helvetica", "12", "bold"),command = showSolution)
solutionButton.grid(row = 10, column = 6, columnspan = 3 )

checkButton = Button(frame, text = "CHECK ANSWER", background = "dark gray", activebackground = "green", \
                     font = ("Helvetica", "12", "bold"), command = checkSolution)
checkButton.grid(row = 11, column = 3, columnspan = 3)

#gameStart(easy1)

root.mainloop()