"""
Gunnar Bachmann
12/3/2019
CS1
font_popup.py

Python file which creates a popup displaying the fonts
to be selected from (the user does not select from the popup).
This is imported into other files when wanting to use.
"""

import turtle as t


def new_line():
    """
    moves the turtle to the "next line" of where the next font will be displayed

    starts by lifting turtle up, then ends pendown.
    :return:
    """
    t.up()
    t.right(90)
    t.fd(20)
    t.left(90)
    t.down()

def popup_setup():
    """
    Sets up the turtle window, adding a title, changing the turtle speed, and hiding the turtle icon.
    :return:
    """
    t.title("Font Options")
    t.setup(250, 300)
    t.setworldcoordinates(-25, -200, 100, 100)
    t.hideturtle()
    t.speed(0)

def font_popup():
    """
    First calls the popup_setup() function.
    Then writes out each font name in the corresponding font.
    Between writing each word, the turtle moves to the newline spot.
    At the end the popup waits for the user to close the window.
    :return:
    """
    popup_setup()
    t.write("Arial", False, "left", font=("Arial", 14, "normal"))
    new_line()
    t.write("Comic Sans MS", False, "left", font=("Comic Sans MS", 14, "normal"))
    new_line()
    t.write("Lucida Grande", False, "left", font=("Lucida Grande", 14, "normal"))
    new_line()
    t.write("Tahoma", False, "left", font=("Tahoma", 14, "normal"))
    new_line()
    t.write("Verdana", False, "left", font=("Verdana", 14, "normal"))
    new_line()
    t.write("Helvetica", False, "left", font=("Helvetica", 14, "normal"))
    new_line()
    t.write("Times New Roman", False, "left", font=("Times New Roman", 14, "normal"))
    print("Please close the window to continue choosing your font...")
    t.done()