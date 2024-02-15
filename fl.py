from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame, CTkComboBox, filedialog
from main import  template, read_file, create_reports
win = CTk()

win.title("PEC Report")
win.geometry("300x300")

section, year, sem = "", "", ""


def chooseFile():
    global fileLabel
    file = filedialog.askopenfilename()
    fileLabel.configure(text=file)

    global df
    df = read_file(file)
    print(df.head())

def createReport():
    global df
    global section, year, sem
    section = sectionCombo.get()
    year = yearCombo.get()
    sem = semCombo.get()

    create_reports(df, section, year, sem)
    

frame = CTkFrame(win, bg_color='#141414')

getFileButton = CTkButton(frame, text="Choose File...", command=chooseFile, corner_radius=32)
getFileButton.pack()


fileLabel = CTkLabel(frame, text="No file chosen")
fileLabel.pack()

yearLabel = CTkLabel(frame, text="Year")
yearLabel.pack()
yearCombo = CTkComboBox(frame, values=["I", "II", "III", "IV"])
yearCombo.pack()


semLabel = CTkLabel(frame, text="Semester")
semLabel.pack()
semCombo = CTkComboBox(frame, values=["I", "II", "III", "IV", "V", "VI", "VII", "VIII"])
semCombo.pack()

sectionCombo = CTkComboBox(frame, values=["A", "B", "-"])


createReportButton = CTkButton(frame, text="Create Report", command=createReport, corner_radius=32)
createReportButton.pack()


frame.place(relx=0.5, rely=0.5, anchor="center")



win.mainloop()