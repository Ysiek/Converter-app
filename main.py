from tkinter import *
from tkinter import filedialog
from spire.doc import *
from spire.doc.common import *

#CONST
FILE_CONVERSE_CHOICE = ['PDF', 'WORD', 'TXT']
CREATE_NEW_FILES_PAR = []

#initialise tkinter
root = Tk()

#Screen setup
root.title("My first app without tutorials")
root.minsize(400, 400)
root.maxsize(400, 400)

def new_file(select):
    CREATE_NEW_FILES_PAR.insert(1, select)

def create_new_file():
    document = Document()
    document.LoadFromFile(CREATE_NEW_FILES_PAR[0])
    document.SaveToFile("TestToPDF.pdf", FileFormat.PDF)
    document.close()

def browseFiles():
    file_name = filedialog.askopenfilename(filetypes = [("all files", "*.*")])
    label_file_name = Label(root, text=f"File you've chosen: {file_name}", background='red')
    label_file_name.grid(column=1, row=1)
    CREATE_NEW_FILES_PAR.insert(0, file_name)

button_explore = Button(root, text="Browse Files", command=browseFiles)
button_explore.grid(column=1, row=2)

var = StringVar(root)
var.set("PDF")
choice = OptionMenu(root, var, *FILE_CONVERSE_CHOICE, command=new_file)
choice.grid(column=1, row=4)

final_button = Button(root, text="Create new file", command=create_new_file)
final_button.grid(column=1, row=5)

root.mainloop()