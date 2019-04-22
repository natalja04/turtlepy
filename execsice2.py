import csv
import turtle as t
import os

dict = {'square': 0, 'pentagon': 0, 'triangle': 0}
list = []
bigList = []
name = ""

def draw():
        t.penup()
        t.goto(0, 200)
        t.pendown()
        for k, v in bigList:
            if k == "square":
                t.fillcolor(v)
                t.begin_fill()
                t.circle(30, steps=4)
                t.end_fill()
                # moving the turtle down
                t.penup()
                t.goto(0, t.ycor() - 70)
                t.pendown()
            if k == "pentagon":
                t.fillcolor(v)
                t.begin_fill()
                t.circle(30, steps=5)
                t.end_fill()
                t.penup()
                t.goto(0, t.ycor() - 70)
                t.pendown()
            if k == "triangle":
                t.fillcolor(v)
                t.begin_fill()
                t.circle(30, steps=3)
                t.end_fill()
                t.penup()
                t.goto(0, t.ycor() - 70)
                t.pendown()


#check for input name
try:
    name = input("Kirjutage faili nimetus: ")
    if os.path.isfile(name):
        with open(name) as csvfile:
            # read from csv
            readCsv = csv.reader(csvfile, delimiter=';')
            for row in readCsv:
                # add types of figures to list
                list.append(row[0])
                # add csv data to bigList
                bigList.append(row)
            # count figure types
            for l in list:
                dict[l] += 1
        # call draw() function to draw figures
        draw()

        # print results of counting figures
        for key in dict:
            print(key, dict[key], "times")
    else:
        print("Wrong filename")
except:
    print("Error!Wrong file format")


