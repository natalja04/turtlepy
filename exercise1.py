import csv
import turtle as t

dict = {'square': 0, 'pentagon': 0, 'triangle': 0}
list = []
bigList = []
name = " "
filename='shapes_colors.csv'

def draw():
    t.penup()
    t.goto(0,200)
    t.pendown()
    for k,v in enumerate(bigList):
        if v[0] == "square":
            t.fillcolor(v[1])
            t.begin_fill()
            t.circle(30, steps=4)
            t.end_fill()
            # moving the turtle down
            t.penup()
            t.goto(0, t.ycor() - 70)
            t.pendown()
        if v[0] == "pentagon":
            t.fillcolor(v[1])
            t.begin_fill()
            t.circle(30, steps=5)
            t.end_fill()
            t.penup()
            t.goto(0, t.ycor() - 70)
            t.pendown()
        if v[0] == "triangle":
            t.fillcolor(v[1])
            t.begin_fill()
            t.circle(30, steps=3)
            t.end_fill()
            t.penup()
            t.goto(0, t.ycor() - 70)
            t.pendown()

#check for input name
while name != filename:
    name = input("Kirjutage faili nimetus: ")
    if name == filename:
        with open(filename) as csvfile:
            #read from csv
            readCsv = csv.reader(csvfile, delimiter=';')
            
            for row in readCsv:
                # add types of figures to list
                list.append(row[0])
                # add csv data to bigList
                bigList.append(row)
            #count figure types
            print(bigList)
            for l in list:
                if l == "square":
                    dict['square'] +=1
                if l == "pentagon":
                    dict['pentagon'] +=1
                if l == "triangle":
                    dict['triangle'] +=1
        #call draw() function to draw figures
        draw()
        #print results of counting figures
        print("triangle", dict.get("triangle"), "times")
        print("pentagon", dict.get("pentagon"), "times")
        print("square", dict.get("square"), "times")
