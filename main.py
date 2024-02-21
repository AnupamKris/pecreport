import pandas as pd
import os

template = """
    #set page(
    paper: "a4",
    margin: (
        top: 20pt,
        bottom: 20pt,
        left: 40pt,
        right: 40pt
    ),
    footer: [
        #set text(size: 14pt, weight: "bold")
        #table(
        columns: (1fr, 1fr, 1fr),
        stroke: none,
        align: center,
        [Class Incharge], [HOD], [Principal],
        )
    ],
    footer-descent: -30pt

    )

    #set align(center) 

    #image("image.png", width: 80pt)

    #set text(size:24pt, weight: "bold")
    PRATHYUSHA ENGINEERING COLLEGE

    #set text(size:24pt)
    DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE

    IAT 1 PROGRESS REPORT


    #set text(size:16pt)
    #table(
    columns: (1fr, 2fr, 1fr, 1fr),
    // inset: 10pt,
    stroke: none,
    align: (right, left, right, left),
    [Name : ], [{}] , [Sec :], [{}],
    [Year :], [{}], [Sem :], [{}]
    )

    #set text(size:14pt, weight: "regular")

    #table(
    columns: (auto, auto, auto, auto),
    inset: 10pt,
    [*S.No*], [*Subject Code*], [*Subject Name*], [*Marks*],
    {}
    )


    #table(
    columns: (1fr, 0.7fr, 1fr, 0.7fr, 1fr, 0.7fr, 1fr, 0.7fr),
    stroke: none,
    align: (right, left, right, left, right, left, right, left),
    [*Present :*], [{}], [*Absent :*], [{}], [*Total :*],  [{}],[*Att. % :*], [{}], 
    )

    #set align(left)
    #h(15pt) *Comments:* {}
    """


def read_file(path):
    df = pd.read_excel(path)
    col = df.columns
    subcodes = list(col)[4:-4]
    subjects = list(df.iloc[0])[4:-4]
    df.columns = df.iloc[0]
    # remove first row
    df = df.drop(0)
    df = df.set_index("S.No")

    return df, subcodes, subjects


def create_reports(df, section, year, sem, subcodes, subjects):
    n = len(df)
    for i in range(0, n):
        if n == 1:
            break
        rec = list(df.iloc[i])
        regno = rec[0]
        name = rec[1]
        marks = rec[3:-4]
        total = rec[-3]
        percentage = rec[-1]
        absent = rec[-2]
        present = total - absent

        rec = [regno, name, present, absent, total, percentage, marks, subcodes]

        

        # rec = [
        #     111420243001,
        #     "AJAY B",
        #     27,
        #     8,
        #     35,
        #     80,
        #     ["AB", 56, 60, 60, 60],
        #     ["AD8501", "CW8691", "AD8502", "AD8551", "AD8552"],
        # ]

        regno = rec[0]
        name = rec[1]
        sec = section
        year = year
        sem = sem

        marks = rec[6]
        marks = [str(i) for i in marks]
        subnames = subjects
        snos = [i for i in range(1, len(subcodes) + 1)]

        tabledata = []
        for i in range(len(subcodes)):
            tabledata.extend([snos[i], subcodes[i], subnames[i], marks[i]])
        print(['['+str(i)+']' for i in tabledata])
        tabledata = ",".join(['['+str(i)+']' for i in tabledata])
        present = rec[2]
        absent = rec[3]
        total = rec[4]
        attper = rec[5]

        comments = "Good"

        temp = template.format(name, sec, year, sem, tabledata, present, absent, total, attper, comments)

        f = open(f"temp.typ", "w")
        f.write(temp)
        f.close()
        os.system(f"typst compile temp.typ pdfs/{regno}.pdf")


