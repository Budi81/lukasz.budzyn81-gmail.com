'''
   Program: Magic Calculator
   Autor: Nick G.
   Copyright: 2016
'''
import re

print("Our Magical Calculator")
print('Type "quit" to exit\n')

previous = 0
run = True


def perform_match():
    global run
    global previous
    equation = ""

    # If there has been a previous calculation, ude that result as a promt
    if equation == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    # If user quits -->
    if equation == "quit":
        print("Goodbye Human!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:;()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_match()