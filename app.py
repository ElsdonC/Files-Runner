import tkinter as tk #helps to build GUI
from tkinter import filedialog , Text #filedialog helps to pick the apps, $text helps to display text
import os #enables us to run apps 

root = tk.Tk() #frame
root.title("Files Opener") #window title
apps = [] #array stores file names

if os.path.isfile('history.txt'):
    with open('history.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()] #gets rid of empty spaces in text file

def addApp():
    for widget in frame.winfo_children():
        widget.destroy() #removes duplicate file names

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*"))) #only allows .exe apps to be selected
    apps.append(filename) #adds file names to apps array
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

#attaches a canvas to the root
canvas = tk.Canvas(root, height=700, width=700, bg="#9DD6DF") 
canvas.pack()

#attach a frame to root
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.75, relheight=0.75, relx=0.125, rely=0.125)

#add open files button to root
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#9DD6DF", command=addApp) 
openFile.pack()

#add run button to root
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#9DD6DF", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

#when the app is closed, the filenames will be written to a text file called history.txt
with open('history.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')