""" implementing triangle calc into triangle and triangle calc """

import random as r
import math
import a as a
import b as b
import h as h


def program_start():
    t


answer_area_triangle = 0
answer_perimeter_triangle = 0


def triangle_area():
    while answer_area_triangle == 0:

        base = float(input("please input the base length of the triangle: "))
        height = float(input("please input the height of the triangle: "))
        side_1 = float(input("please input the left side of triangle: "))
        side_2 = float(input("please input the right side of triangle: "))
        triangle_area_calc = base * height / 2
        # (f'__area__\n A = BH ÷ 2\n A = {base} × {height} ÷ 2\n A = {base * height / 2}')
        answer_triangle_area = int(input("Please input the answer for the area: "))

        if answer_triangle_area == triangle_area_calc:
            print("That is the correct answer, well done!")
            answer_triangle_area == "correct"
            answer_area_triangle == +1
            triangle_perimeter()


        else:
            print("Sorry, that is not the answer. The correct answer is ", triangle_area_calc)
            answer_triangle_area == "incorrect"
            answer_area_triangle == +1
            triangle_perimeter()


def triangle_perimeter():
    while answer_perimeter_triangle == 0:
        base = float(input("please input the base length of the triangle: "))
        height = float(input("please input the height of the triangle: "))
        side_1 = float(input("please input the left side of triangle: "))
        side_2 = float(input("please input the right side of triangle: "))
        triangle_perimeter_calc = base + side_1 + side_2
        triangle_perimeter_int = int(triangle_perimeter_calc)
        # (f'__perimeter__\n P = B + S1 + S2\n P = {base} + {side_1} + {side_2}\n P = {base + side_1 + side_2}')
        answer_triangle_perimeter = int(input("Please input the answer for the perimeter: "))

        if answer_triangle_perimeter == triangle_perimeter_int:
            print("That is the correct answer, well done!")
            answer_triangle_perimeter == "correct"
            answer_perimeter_triangle == answer_perimeter_triangle + 1
            print("Thank you for playing :)")
            end()



        else:
            print("Sorry, that is not the answer. The correct answer is ", triangle_perimeter_int)
            answer_triangle_perimeter == "incorrect"
            answer_perimeter_triangle == answer_perimeter_triangle + 1
            print("Thank you for playing :)")
            end()



ending_triangle = 0


def end():
    while ending_triangle == 0:
        ending_triangle == ending_triangle + 1


print("welcome to my triangle area and perimeter calculator")
triangle_area()
