"""
game to help with area and perimeter homework
base component
v1 - set up the skeleton of the program


"""
# import library************************************************
import random as r


# set up functions**********************************************

# function to check for integers. will loop until an integer is input
def int_checker():
    print("placeholder")


# function to check string is within an allowable list. Will loop until an allowable word is input
def string_checker(list_of_allowable):
    print("placeholder")


# function to identify shape
def circle():
    radius = float(input("print please enter radius of the circle: "))
    print(f'__Circumference__\n C = 2πR\n C = 2(π × {radius})\n C = {2 * (radius * math.pi)}')
    print(f'__Area__\n A = πr²\n A = π×{radius}²\n A = {pow(radius, 2) * math.pi}')


# function to identify square shape
def square():
    length = float(input("please input the length of the square: "))
    height = float(input("please input the height of the square: "))
    print(f'__Area__\n A = LH\n A = {length}×{height}\n A = {length * height}')
    print(f'__Perimeter__\n P = (L×2)+(H×2)\n A = {length}×2+{height}×2 \n A = {length * 2 + height * 2}')


# function to identify rectangle shape
def rectangle():
    length = float(input("please input the length of the rectangle: "))
    height = float(input("please input the height of the rectangle: "))
    print(f'__Area__\n A = LH\n A = {length}×{height}\n A = {length * height}')
    print(f'__Perimeter__\n P = (L×2)+(H×2)\n A = {length}×2+{height}×2 \n A = {length * 2 + height * 2}')


# function to identify triangle shape
def triangle():
    base = float(input("please input the base length of the triangle: "))
    height = float(input("please input the height of the triangle: "))
    side_1 = float(input("please input the left side of triangle: "))
    side_2 = float(input("please input the right side of triangle: "))
    print(f'__Area__\n A = BH ÷ 2\n A = {base} × {height} ÷ 2\n A = {base * height / 2}')
    print(f'__Perimeter__\n P = B + S1 + S2\n P = {base} + {side_1} + {side_2}\n P = {base + side_1 + side_2}')


# function to identify parallelogram shape
def parallelogram():
    base = float(input("please enter the base: "))
    height = float(input("please enter the height: "))
    sloped_side = float(input("please enter sloped side length: "))
    print(f'__Area__\n A = BH\n A = {base} × {height}\n A = {base * height}')
    print(f'__Perimeter__\n P = 2(a + b)\n P = 2({base} + {height})\n P = {base + height + base + height}')


# function to identify trapezium shape
def trapezium():
    parallel_s1 = float(input("please enter side 1 of the parallel sides: "))
    parallel_s2 = float(input("please enter side 2 of the parallel sides: "))
    height = float(input("please enter the height: "))
    sloped_s1 = float(input("please enter side 1 of the sloped side: "))
    sloped_s2 = float(input("please enter side 2 of the sloped side: "))
    (a + b) / 2 * h
    print(f'__area__\n A = (a+b)/2*h \n A = ({parallel_s1} + {parallel_s2}/2 × {height}')
    print(f'__perimeter__\n P = A + B + C + D\n P = {parallel_s1}+{parallel_s2}+{sloped_s1}+{sloped_s2}\n P = {parallel_s1 + parallel_s2 + sloped_s1 + sloped_s2}')


# trialling random generator as part of v1 base component
def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_nu


# random generator component works well.


# set up lists and constants************************************
answer_list = []
yes_no_list = [["yes", "y"], ["no", "n"]]
shape_list = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]


# set up main***************************************************
if __name__ == "__main__":
    # set local variables within the main routine
    min_num = 0
    max_num = 5

    print("placeholder")
    # ask users for input
    print("******************* AREA AND PERIMETER GAME ****************************")
    print("**")
    print("** Welcome to my Area and Perimeter Game. ")
    operand = input("""** Please choose a shape (circle, square, rectangle, 
    triangle, parallelogram, or trapezium): """).lower()
    # check operand for legitimacy
    # string check - send the list of shape_list

    # ask user if they wish to use negatives?
    # yes/no list and answer sent to string checker

    # ask user for low and high numbers.
    # int checker to check it's an integer, loop until suitable integer

    # ask user for number of questions to be asked
    # int checker to check on the integer
    num_questions = 1

    # loop until number of questions is asked
    for questions in (0, num_questions):
        print("placeholder")
        if operand == "circle":
            print("go to circle")
            circle()
        elif operand == "square":
            print("got to square")
            square()
        elif operand == "rectangle":
            print("go to rectangle")
            rectangle()
        elif operand == "triangle":
            print("go to triangle")
            triangle()
        elif operand == "parallelogram":
            print("go to parallelogram")
            parallelogram()
        elif operand == "trapezium":
            print("go to trapezium")
            trapezium()

        # print("go to random generator, send min_num and max_num (1 and 5)")
        # print("then randomly go to each of the operand functions")
