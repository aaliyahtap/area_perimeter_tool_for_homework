""" implementing parallelogram calc into parallelogram and parallelogram calc """

import random as r
import math
import a as a
import b as b
import h as h


def program_start():
    t


answer_area_parallelogram = 0
answer_perimeter_parallelogram = 0


def parallelogram_area():
    while answer_area_parallelogram == 0:

        base = float(input("please enter the base: "))
        height = float(input("please enter the height: "))
        sloped_side = float(input("please enter sloped side length: "))
        parallelogram_area_calc = base * height
        # (f'__area__\n A = BH ÷ 2\n A = {base} × {height} ÷ 2\n A = {base * height / 2}')
        answer_parallelogram_area = int(input("Please input the answer for the area: "))

        if answer_parallelogram_area == parallelogram_area_calc:
            print("That is the correct answer, well done!")
            answer_parallelogram_area == "correct"
            answer_area_parallelogram == +1
            parallelogram_perimeter()


        else:
            print("Sorry, that is not the answer. The correct answer is ", parallelogram_area_calc)
            answer_parallelogram_area == "incorrect"
            answer_area_parallelogram == +1
            parallelogram_perimeter()


def parallelogram_perimeter():
    while answer_perimeter_parallelogram == 0:
        base = float(input("please enter the base: "))
        height = float(input("please enter the height: "))
        sloped_side = float(input("please enter sloped side length: "))
        parallelogram_perimeter_calc = base + height + base + height
        parallelogram_perimeter_int = int(parallelogram_perimeter_calc)
        # (f'__perimeter__\n P = B + S1 + S2\n P = {base} + {side_1} + {side_2}\n P = {base + side_1 + side_2}')
        answer_parallelogram_perimeter = int(input("Please input the answer for the perimeter: "))

        if answer_parallelogram_perimeter == parallelogram_perimeter_int:
            print("That is the correct answer, well done!")
            answer_parallelogram_perimeter == "correct"
            answer_perimeter_parallelogram == answer_perimeter_parallelogram + 1
            print("Thank you for playing :)")
            end()



        else:
            print("Sorry, that is not the answer. The correct answer is ", parallelogram_perimeter_int)
            answer_parallelogram_perimeter == "incorrect"
            answer_perimeter_parallelogram == answer_perimeter_parallelogram + 1
            print("Thank you for playing :)")
            end()



ending_parallelogram = 0


def end():
    while ending_parallelogram == 0:
        ending_parallelogram == ending_parallelogram + 1


print("welcome to my parallelogram area and perimeter calculator")
parallelogram_area()
