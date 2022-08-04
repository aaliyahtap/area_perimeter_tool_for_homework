""" implementing rectangle calc into rectangle and rectangle calc """

import random as r
import math
import a as a
import b as b
import h as h


def program_start():
    t


answer_area_rectangle = 0
answer_perimeter_rectangle = 0


def rectangle_area():
    while answer_area_rectangle == 0:

        length = float(input("please input the length of the rectangle: "))
        height = float(input("please input the height of the rectangle: "))
        rectangle_area_calc = length * height
        # (f'__Area__\n A = LH\n A = {length}×{height}\n A = {length * height}')
        answer_rectangle_area = int(input("Please input the answer for the area: "))

        if answer_rectangle_area == rectangle_area_calc:
            print("That is the correct answer, well done!")
            answer_rectangle_area == "correct"
            answer_area_rectangle == +1
            rectangle_perimeter()


        else:
            print("Sorry, that is not the answer. The correct answer is ", rectangle_area_calc)
            answer_rectangle_area == "incorrect"
            answer_area_rectangle == +1
            rectangle_perimeter()


def rectangle_perimeter():
    while answer_perimeter_rectangle == 0:
        length = float(input("please input the length of the rectangle: "))
        height = float(input("please input the height of the rectangle: "))
        rectangle_perimeter_calc = length * 2 + height * 2
        rectangle_perimeter_int = int(rectangle_perimeter_calc)
        # (f'__Perimeter__\n P = (L×2)+(H×2)\n A = {length}×2+{height}×2 \n A = {length * 2 + height * 2}')
        answer_rectangle_perimeter = int(input("Please input the answer for the perimeter: "))

        if answer_rectangle_perimeter == rectangle_perimeter_int:
            print("That is the correct answer, well done!")
            answer_rectangle_perimeter == "correct"
            answer_perimeter_rectangle == answer_perimeter_rectangle + 1
            print("Thank you for playing :)")
            end()



        else:
            print("Sorry, that is not the answer. The correct answer is ", rectangle_perimeter_int)
            answer_rectangle_perimeter == "incorrect"
            answer_perimeter_rectangle == answer_perimeter_rectangle + 1
            print("Thank you for playing :)")
            end()



ending_rectangle = 0


def end():
    while ending_rectangle == 0:
        ending_rectangle == ending_rectangle + 1


print("welcome to my rectangle area and perimeter calculator")
rectangle_area()
