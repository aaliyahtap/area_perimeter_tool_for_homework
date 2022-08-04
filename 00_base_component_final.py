"""
game to help with area and perimeter homework
base component
v2 - set up the skeleton of the program


"""
# import library************************************************
import random as r
import math
import a as a
import b as b
import h as h


def program_start():
    t


# set up functions**********************************************

# function to check string is within an allowable list. Will loop until an allowable word is input
def string_checker(shape_lst):
    print("placeholder")


# function to identify shape




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


# function to identify square shape




def square_area():
    while answer_area_square == 0:

        length = float(input("please input the length of the square: "))
        height = float(input("please input the height of the square: "))
        square_area_calc = length * height
        # (f'__Area__\n A = LH\n A = {length}×{height}\n A = {length * height}')
        answer_square_area = int(input("Please input the answer for the area: "))

        if answer_square_area == square_area_calc:
            print("That is the correct answer, well done!")
            answer_square_area == "correct"
            answer_area_square == +1
            square_perimeter()


        else:
            print("Sorry, that is not the answer. The correct answer is ", square_area_calc)
            answer_square_area == "incorrect"
            answer_area_square == +1
            square_perimeter()
def square_perimeter():
    while answer_perimeter_square == 0:
        length = float(input("please input the length of the square: "))
        height = float(input("please input the height of the square: "))
        square_perimeter_calc = length * 2 + height * 2
        square_perimeter_int = int(square_perimeter_calc)
        # (f'__Perimeter__\n P = (L×2)+(H×2)\n A = {length}×2+{height}×2 \n A = {length * 2 + height * 2}')
        answer_square_perimeter = int(input("Please input the answer for the perimeter: "))

        if answer_square_perimeter == square_perimeter_int:
            print("That is the correct answer, well done!")
            answer_square_perimeter == "correct"
            answer_perimeter_square == answer_perimeter_square + 1
            print("Thank you for playing :)")
            end()



        else:
            print("Sorry, that is not the answer. The correct answer is ", square_perimeter_int)
            answer_square_perimeter == "incorrect"
            answer_perimeter_square == answer_perimeter_square + 1
            print("Thank you for playing :)")
            end()



ending_square = 0


def end():
    while ending_square == 0:
        ending_square == ending_square + 1


# function to identify rectangle shape


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


# function to identify triangle shape


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


# function to identify parallelogram shape



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


# function to identify trapezium shape



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







# set up lists and constants************************************

shape_list = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

answer_area_trapezium = 0
answer_perimeter_trapezium = 0
answer_area_parallelogram = 0
answer_perimeter_parallelogram = 0
answer_area_triangle = 0
answer_perimeter_triangle = 0
answer_area_rectangle = 0
answer_perimeter_rectangle = 0
answer_area_square = 0
answer_perimeter_square = 0
answer_area_circ = 0
answer_circum_circ = 0
# set up main***************************************************



if __name__ == "__main__":
    # set local variables within the main routine


    # ask users for input
    print("******************* AREA AND PERIMETER GAME ****************************")
    print("**")
    print("** Welcome to my Area and Perimeter Homework Helper ")

for shape_choice in shape_list:
    shape = input("""** Please choose a shape (circle, square, rectangle, 
**  triangle, parallelogram, or trapezium): """)
    if shape == shape_list:
        continue
    else:
        break

# check shape for legitimacy
# string check - send the list of shape_list

# ask user if they wish to use negatives?
# yes/no list and answer sent to string checker

# ask user for low and high numbers.
# int checker to check it's an integer, loop until suitable integer

# ask user for number of questions to be asked
# int checker to check on the integer
num_shapes = 0

# loop until number of questions is asked
for questions in (0, num_shapes):
    print("************************************************************************")
    if shape == "circle":
        print("************************************************************************")
        circle_area()
    elif shape == "square":
        print("************************************************************************")
        square_area()
    elif shape == "rectangle":
        print("************************************************************************")
        rectangle_area()
    elif shape == "triangle":
        print("************************************************************************")
        triangle_area()
    elif shape == "parallelogram":
        print("************************************************************************")
        parallelogram_area()
    elif shape == "trapezium":
        print("************************************************************************")
        trapezium_area()
