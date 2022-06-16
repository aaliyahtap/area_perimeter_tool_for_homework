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
    print("placeholder")


# function to identify square shape
def square():
    print("placeholder")


# function to identify rectangle shape
def rectangle():
    print("placeholder")


# function to identify triangle shape
def triangle():
    print("placeholder")


# function to identify parallelogram shape
def parallelogram():
    print("placeholder")


# function to identify trapezium shape
def trapezium():
    print("placeholder")


# trialling random generator as part of v1 base component
def random_generator(num_1, num_2):
    rand_num = r.randint(num_1, num_2)
    return rand_num


# random generator component works well.


# set up lists and constants************************************
answer_list = []
yes_no_list = [["yes", "y"], ["no", "n"]]
operands = ["circle", "square", "rectangle", "triangle", "parallelogram", "trapezium"]

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
    # string check - send the list of operands

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
        else:
            # this is called when user inputs all
            min_num = 1
            max_num = 5
            random_num = random_generator(min_num, max_num)
            print(random_num)
        # print("go to random generator, send min_num and max_num (1 and 5)")
        # print("then randomly go to each of the operand functions")
