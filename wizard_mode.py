"""
Gunnar Bachmann
12/3/2019
CS1
wizard_mode.py

Wizard mode for the project. Collects both body and style information
from the user through asking and storing the information. Then outputs an html file,
called index.html, containing the users preferred content and style.
"""
from cs_queue import Queue, make_empty_queue, enqueue, dequeue, front, back, is_empty
from style import style_main



def ask_header(wizard_body):
    """
    collects the header and adds it to the queue.
    :param wizard_body: queue
    :return: queue with header saved in it.
    """
    p_title = input("Header for your paragraph: ")
    enqueue(wizard_body, p_title)
    return wizard_body

def ask_paragraph(wizard_body):
    """
    collects the paragraph content for the user
    and adds it to the queue

    :param wizard_body: queue
    :return: queue with paragraph content added to it.
    """
    paragraph = input("Content of your paragraph (single line):")
    enqueue(wizard_body, paragraph)
    return wizard_body

def ask_images(wizard_body, any_images):
    """
    if the user wants to enter an image, it will do so then we will
    store it and ask again if they want to add another.

    :param wizard_body: queue
    :param any_images: yes or no on whether the user wanted to add images
    :return: queue with images saved in it
    """
    if any_images == "no" or any_images == "No" or any_images == "NO":
        return wizard_body
    else:
        image = input("Image file name: ")
        enqueue(wizard_body, image)
        another_image = input("Would you like to add another image? [yes]: ")
        if another_image == "no" or another_image == "No" or another_image == "NO":
            return wizard_body
        else:
            return ask_images(wizard_body, any_images)

def write_paragraph(body):
    """
    Writes the body content

    :param body:
    :return: writes to the file
    """
    if body is not None:
        index = open("index.html", "a")
        header = dequeue(body)
        paragraph = dequeue(body)

        index.write("<h2>")
        index.write(header)
        index.write("</h2>\n")

        index.write("<p>'")
        index.write(paragraph)
        index.write("'</p>\n")
        index.close()
    else:
        pass

def write_images(body):
    """
    writes the images into the file

    :param body: queue
    :return:
    """
    if body.front is not None:
        index = open("index.html", "a")
        image_link = dequeue(body)
        image = "<img src='" + image_link + "' class='center'"
        index.write(image)
        index.write("\n")
        index.close()
        write_images(body)
    else:
        pass

def wizard_body():
    """
    makes and empty queue, asks for the header, paragraph, and images, and returns it all saved in a queue
    :return: all info saved in a queue
    """
    wizard_body = make_empty_queue()
    ask_header(wizard_body)  # header
    ask_paragraph(wizard_body)  # paragraph
    any_images = input("Would you like to add any images? [yes]: ")  # asks whether want to ask images or not
    ask_images(wizard_body, any_images)  # either passes or adds however many images to wizard_body

    return wizard_body

def write_body():
    """
    writes the body portion of the file
    :return:
    """
    body = wizard_body()
    write_paragraph(body)
    write_images(body)
    another_p = input("Would you like to add another paragraph to your website? [yes]: ")
    if another_p == "no" or another_p == "No" or another_p == "NO":
        pass
    else:
        return write_body()

def build_index(style, title):
    """
    builds the index and starts it off by writing the
    doctype, and head section (including title and style).
    """
    index = open("index.html", "w")


    index.write("<!DOCTYPE html>\n")
    index.write("<html>\n")
    index.write("\n")


    index.write("<head>\n")
    index.write("<meta charset='UTF-8'>\n")
    index.write("<title>")
    index.write(title)
    index.write("</title>\n")
    index.write(style)
    index.write("\n")
    index.write("</head>\n")


    index.close()

def wizard_main():
    """
    wizards main function that does all of the required tasks and closes off the file
    including finishing off the closing tags.
    :return:
    """
    title = input("What is the title of your website?: ")
    style = style_main()
    build_index(style, title) #creates and builds index.html for doctype and head section

    index = open("index.html", "a")
    index.write("<body>\n")
    index.close()

    write_body()

    index = open("index.html", "a")
    index.write("\n")
    index.write("</body>\n")
    index.write("</html>")
    index.close()