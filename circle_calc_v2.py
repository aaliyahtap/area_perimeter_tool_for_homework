import random as r
import math
import a as a
import b as b
import h as h


def program_start():
    t


answer_area_circ = 0
answer_circum_circ = 0


def circle_area():
    while answer_area_circ == 0:

        radius = float(input("please enter radius of the circle to find the area: "))
        circle_area_calc = {pow(radius, 2) * math.pi}

        # f'__area__\n A = πr²\n A = π×{radius}²\n A = {pow(radius, 2) * math.pi}'
        answer_circle_area = int(input("Please input the answer for the area: "))

        if answer_circle_area == circle_area_calc:
            print("That is the correct answer, well done!")
            answer_circle_area == "correct"
            answer_area_circ == +1
            circle_circumference()


        else:
            print("Sorry, that is not the answer. The correct answer is ", circle_area_calc)
            answer_circle_area == "incorrect"
            answer_area_circ == +1
            circle_circumference()


def circle_circumference():
    while answer_circum_circ == 0:
        radius = float(input("please enter radius of the circle to find the circumference: "))
        circle_circumference_calc = 2 * (radius * math.pi)
        circle_circumference_int = int(circle_circumference_calc)
        # f'__area__\n A = πr²\n A = π×{radius}²\n A = {pow(radius, 2) * math.pi}'
        answer_circle_circumference = int(input("Please input the answer for the circumference: "))

        if answer_circle_circumference == circle_circumference_int:
            print("That is the correct answer, well done!")
            answer_circle_circumference == "correct"
            answer_circum_circ == answer_circum_circ + 1
            print("Thank you for playing :)")
            end()



        else:
            print("Sorry, that is not the answer. The correct answer is ", circle_circumference_int)
            answer_circle_circumference == "incorrect"
            answer_circum_circ == answer_circum_circ + 1
            print("Thank you for playing :)")
            end()



ending_circ = 0


def end():
    while ending_circ == 0:
        ending_circ == ending_circ + 1


print("welcome to my circle area calculator")
circle_area()
