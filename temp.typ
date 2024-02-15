
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
    [Name : ], [ARSATH KHAN A] , [Sec :], [A],
    [Year :], [IV], [Sem :], [II]
    )

    #set text(size:14pt, weight: "regular")

    #table(
    columns: (auto, auto, auto, auto),
    inset: 10pt,
    [*S.No*], [*Subject Code*], [*Subject Name*], [*Marks*],
    [1],[AD8501],[Mathematics],[60],[2],[CW8691],[Data Mining],[60],[3],[AD8502],[Machine Learning],[60],[4],[AD8551],[Deep Learning],[60],[5],[AD8552],[Natural Language Processing],[73],[6],[nan],[GIS],[60]
    )


    #table(
    columns: (1fr, 0.7fr, 1fr, 0.7fr, 1fr, 0.7fr, 1fr, 0.7fr),
    stroke: none,
    align: (right, left, right, left, right, left, right, left),
    [*Present :*], [49], [*Absent :*], [6], [*Total :*],  [55],[*Att. % :*], [80], 
    )

    #set align(left)
    #h(15pt) *Comments:* Good
    