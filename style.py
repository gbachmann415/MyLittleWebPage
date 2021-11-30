"""
Gunnar Bachmann
12/3/2019
CS1
style.py

All of the functions and code working with style for the "My Little Web Page" project.
Is imported into the files which need to collect style information and output the final
string of <style>
"""

from font_popup import font_popup
from dataclasses import dataclass



#valid colors for <style>
valid_colors = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen', 'lawngreen',
                'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen', 'chocolate', 'yellowgreen',
                'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink',
                'gray', 'indianred ', 'antiquewhite', 'royalblue', 'yellow', 'indigo ', 'lightcoral', 'darkslategrey', 'sienna',
                'lightslategray', 'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise',
                'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen',
                'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred', 'dimgray',
                'floralwhite', 'orangered', 'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue',
                'silver', 'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson',
                'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold',
                'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen',
                'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple', 'olivedrab',
                'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen',
                'deepskyblue', 'pink', 'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen',
                'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow',
                'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite',
                'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid'}


#valid fonts to be used (and their corresponding number)
fonts = {0:'Arial',
         1:'Comic Sans MS',
         2:'Lucida Grande',
         3:'Tahoma',
         4:'Verdana',
         5:'Helvetica',
         6:'Times New Roman'}


#Valid hex code characters
valid_hex = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}


#Style dataclass for storing each input from the user to be used in creating their style options
@dataclass
class Style:
    __slots__ = 'background', 'paragraph_color', 'heading_color', 'font_style'
    background: str
    paragraph_color: str
    heading_color: str
    font_style: str


def create_empty_style():
    """
    Creates an empty Style class and returns it to the user.
    :return: empty Style dataclass
    """
    return Style(background=None, paragraph_color=None, heading_color=None, font_style=None)


def create_style_template(style_template):
    """
    Uses the provided template in the same directory for the <style> section of the html.
    This function returns a string with the exact contents of the template saved. This
    will be used in order to fill in the style information from the user when writing this
    template into the actual html file being created.

    :param style_template: style_template.txt located in the same directory of this project
    :return: string copy of style_template.txt file
    """
    open_style_template = open(style_template)
    style_temp = ""
    for line in open_style_template:
        style_temp += line
    open_style_template.close()
    return style_temp


def sub_style(style_txt, style):
    """
    Replaces the variables in style_txt (the string style outline)
    with the contents of the stored information in the style class.

    :param style_txt: string copy of the style_template
    :param style: style dataclass with stored information from user
    :return: style_txt with the variables swapped out. Final version of style saved as a string.
    """
    style_txt = style_txt.replace("@BACKCOLOR", style.background)
    style_txt = style_txt.replace("@HEADCOLOR", style.heading_color)
    style_txt = style_txt.replace("@FONTSTYLE", style.font_style)
    style_txt = style_txt.replace("@FONTCOLOR", style.paragraph_color)

    return style_txt


def validate_color(color):
    """
    Checks the inputted color and returns True or False on whether the color is valid

    :param color: color entered by user
    :return: Bool value -- True if valid, False if not
    """
    if color[0] != "#":
        color = color.lower()
        if color in valid_colors:
            return True
        else:
            return False
    elif color[0] == "#":
        color = color.upper()
        if len(color) != 7:
            return False
        else:
            for i in color[1:]:
                if i not in valid_hex:
                    return False
                else:
                    return True


def select_font(style):
    """
    Function to select the font to be used.

    :param style: Style class to store the selected font
    :return: Style class with the selected font, or prints invalid and calls the function again
    until a valid response is entered.
    """
    print("You will now choose a font")
    view_fonts = input("Do you want to see what the fonts look like? [yes]: ")
    if view_fonts == "no" or view_fonts == "No" or view_fonts == "NO":
        pass
    else:
        font_popup()
    print("Choose a font by it's number: ")
    print("0: Arial, size 14")
    print("1: Impact, size 14")
    print("2: Lucida Grande, size 14")
    print("3: Tahoma, size 14")
    print("4: Verdana, size 14")
    print("5: Helvetica, size 14")
    print("6: Times New Roman, size 14")
    font_choice = int(input(">>"))
    if font_choice == 0:
        font = fonts[0]
        style.font_style = font
        return style
    elif font_choice == 1:
        font = fonts[1]
        style.font_style = font
        return style
    elif font_choice == 2:
        font = fonts[2]
        style.font_style = font
        return style
    elif font_choice == 3:
        font = fonts[3]
        style.font_style = font
        return style
    elif font_choice == 4:
        font = fonts[4]
        style.font_style = font
        return style
    elif font_choice == 5:
        font = fonts[5]
        style.font_style = font
        return style
    elif font_choice == 6:
        font = fonts[6]
        style.font_style = font
        return style
    else:
        print("Invalid choice...")
        return select_font(style)


def heading_color(style):
    """
    Asks and collects the preferred heading color from the user.

    :param style: Style class to store the selected heading color
    :return: Style class with the selected color, or prints invalid and calls the function again
    until a valid response is entered.
    """
    print("Heading Color")
    selected_heading_clr = input("Choose the name of a color, or in format '#XXXXXX': ")
    if selected_heading_clr[0] == "#":
        selected_heading_clr = selected_heading_clr.upper()
    else:
        selected_heading_clr = selected_heading_clr.lower()

    validate_heading_clr = validate_color(selected_heading_clr)
    if validate_heading_clr == True:
        style.heading_color = selected_heading_clr
        return style
    else:
        print("Invalid choice...")
        heading_color(style)


def select_paragraph_color(style):
    """
    Asks the user for paragraph text color and stores/returns it

    :param style: Style class to store the selected paragraph color
    :return: Style class with the selected paragraph color, or prints invalid and calls the function again
    until a valid response is entered.
    """
    print("Paragraph Text Color")
    selected_text_clr = input("Choose the name of a color, or in format '#XXXXXX': ")
    if selected_text_clr[0] == "#":
        selected_text_clr = selected_text_clr.upper()
    else:
        selected_text_clr = selected_text_clr.lower()

    validate_txt_clr = validate_color(selected_text_clr)
    if validate_txt_clr == True:
        style.paragraph_color = selected_text_clr
        return style
    else:
        print("Invalid choice...")
        select_paragraph_color(style)


def select_background(style):
    """
    Asks the user for background color and stores/returns it.

    :param style: Style class to store the selected background color
    :return: Style class with the selected background color, or prints invalid and calls the function again
    until a valid response is entered.
    """
    print("Background Color")
    selected_background = input("Choose the name of a color, or in format '#XXXXXX': ")
    if selected_background[0] == "#":
        selected_background = selected_background.upper()
    else:
        selected_background = selected_background.lower()

    validate_bckgrnd = validate_color(selected_background)
    if validate_bckgrnd == True:
        style.background = selected_background
        return style
    else:
        print("Invalid choice...")
        select_background(style)


def style_main():
    """
    Calls all the functions in the correct order/way to
    build and return a string version of the finalized
    <style>

    :return: string version of the finalized <style>
    """
    style = create_empty_style()
    style_txt = create_style_template("style_template")

    select_font(style)
    heading_color(style)
    select_paragraph_color(style)
    select_background(style)

    return sub_style(style_txt, style)
