import re

print("Our Magical Calculator")
print('Type "quit" to exit\n')

previous = 0
run = True


def perform_match():
    global run
    global previous
    equation = ""
    if equation == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

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