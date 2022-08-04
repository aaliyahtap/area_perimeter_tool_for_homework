""" implementing trapezium calc into trapezium and trapezium calc """

import random as r
import math
import a as a
import b as b
import h as h


def program_start():
    t


answer_area_trapezium = 0
answer_perimeter_trapezium = 0


def trapezium_area():
    while answer_area_trapezium == 0:

        parallel_s1 = float(input("please enter side 1 of the parallel sides: "))
        parallel_s2 = float(input("please enter side 2 of the parallel sides: "))
        height = float(input("please enter the height: "))
        sloped_s1 = float(input("please enter side 1 of the sloped side: "))
        sloped_s2 = float(input("please enter side 2 of the sloped side: "))
        trapezium_area_calc = parallel_s1 + parallel_s2 / 2 * height
        # (f'__area__\n A = BH ÷ 2\n A = {base} × {height} ÷ 2\n A = {base * height / 2}')
        answer_trapezium_area = int(input("Please input the answer for the area: "))

        if answer_trapezium_area == trapezium_area_calc:
            print("That is the correct answer, well done!")
            answer_trapezium_area == "correct"
            answer_area_trapezium == +1
            trapezium_perimeter()


        else:
            print("Sorry, that is not the answer. The correct answer is ", trapezium_area_calc)
            answer_trapezium_area == "incorrect"
            answer_area_trapezium == +1
            trapezium_perimeter()


def trapezium_perimeter():
    while answer_perimeter_trapezium == 0:
        parallel_s1 = float(input("please enter side 1 of the parallel sides: "))
        parallel_s2 = float(input("please enter side 2 of the parallel sides: "))
        height = float(input("please enter the height: "))
        sloped_s1 = float(input("please enter side 1 of the sloped side: "))
        sloped_s2 = float(input("please enter side 2 of the sloped side: "))
        trapezium_perimeter_calc = parallel_s1 + parallel_s2 + sloped_s1 + sloped_s2
        trapezium_perimeter_int = int(trapezium_perimeter_calc)
        # (f'__perimeter__\n P = B + S1 + S2\n P = {base} + {side_1} + {side_2}\n P = {base + side_1 + side_2}')
        answer_trapezium_perimeter = int(input("Please input the answer for the perimeter: "))

        if answer_trapezium_perimeter == trapezium_perimeter_int:
            print("That is the correct answer, well done!")
            answer_trapezium_perimeter == "correct"
            answer_perimeter_trapezium == answer_perimeter_trapezium + 1
            print("Thank you for playing :)")
            end()



        else:
            print("Sorry, that is not the answer. The correct answer is ", trapezium_perimeter_int)
            answer_trapezium_perimeter == "incorrect"
            answer_perimeter_trapezium == answer_perimeter_trapezium + 1
            print("Thank you for playing :)")
            end()



ending_trapezium = 0


def end():
    while ending_trapezium == 0:
        ending_trapezium == ending_trapezium + 1


print("welcome to my trapezium area and perimeter calculator")
trapezium_area()
