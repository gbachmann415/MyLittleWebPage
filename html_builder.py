"""
Gunnar Bachmann
12/03/2019
html_builder.py
CSCI141

Main file for this program. Builds .html files and outputs them to the user
in 2 different ways. The first way is website mode, where the user can run this program from the console and include
1 or more .txt file(s). It will then build .html files for each of the .txt files with the body information
in it. It will still prompt the user for style preferences. If there are more than one files
included by the user, it will link the different pages together with buttons as a nav bar.
The other way is wizard mode. It can be run if the user does not include any files or simply just runs the program.
It will prompt the user for style and body information (paragraph header, content, and images and whether
you would like to add another).
"""
import sys
from wizard_mode import wizard_main
from style import style_main
from cs_queue import Queue, make_empty_queue, enqueue, dequeue, front, back, is_empty

def get_body_txt(file):
    """
    saves the file from the user as a string
    :param file: file from user
    :return: returns file contents as string
    """
    body_txt = ""
    body_file = open(file)
    for line in body_file:
        body_txt += line
    return body_txt


def get_title(file):
    """
    get the title from the file
    :param file: file from user
    :return: the title
    """
    body_file = open(file)
    title = body_file.readline()
    return title


def get_header(body_txt):
    """
    get the header of the paragraph from body_txt

    :param body_txt: string
    :return: header of paragraph
    """
    end = body_txt.index("\n")
    header = body_txt[7:end]
    return header


def convert_image(image):
    """
    Converts the image to the appropriate link

    :param image: image string
    :return: appropriate string for image
    """
    image_lst= image.split()
    has_width = len(image_lst)
    img = ""
    if has_width > 1:
        img += "<img src='" + image_lst[0] + "' width='" + image_lst[1] + "' class='center'>"
    elif has_width == 1:
        img += "<img src='" + image_lst[0] + "' class='center'>"
    else:
        pass
    return img


def write_paragraph(body, name):
    """
    writes the paragraph header and image in the body queue

    :param body: queue
    :param name: name of file
    :return: body
    """
    name += ".html"
    if body is not None:
        file = open(name, "a")
        if body.size > 2:
            header = dequeue(body)
            paragraph = dequeue(body)

            file.write("<h2>")
            file.write(header)
            file.write("</h2>\n")

            file.write("<p>'")
            file.write(paragraph)
            file.write("'</p>\n")

            while body.size > 0:
                image = dequeue(body)

                file.write(image)
                file.write("\n")
        else:
            header = dequeue(body)
            paragraph = dequeue(body)

            file.write("<h2>")
            file.write(header)
            file.write("</h2>\n")

            file.write("<p>'")
            file.write(paragraph)
            file.write("'</p>\n")
        file.close()
    else:
        pass
    return body


def get_paragraph(body_txt, body, name):
    """
    gets the paragraph and its information into the queue, writes
    the paragraph, then repeats until no more paragraphs(etc) are to add

    :param body_txt: str
    :param body: queue
    :param name: name of file
    :return:
    """
    while "!new_paragraph" in body_txt:
        new_p = body_txt.index("!new_paragraph")
        body_txt = body_txt[new_p+15:]

        header = get_header(body_txt)
        end_of_title = body_txt.index("\n")
        body_txt = body_txt[end_of_title + 1:]

        paragraph = ""
        image = ""
        for i in body_txt:
            idx = body_txt.index(i)
            if body_txt[idx] != "!":
                paragraph += i
                body_txt = body_txt[idx:]
            else:
                break
        if body_txt[idx:7] == "!image":
            body_txt = body_txt[idx+7:]
            for i in body_txt:
                if i != "!":
                    image += i
                else:
                    break
        else:
            pass
        paragraph = paragraph[:-1]
        paragraph = paragraph.split("\n")
        final_p = "" #paragraph in string form without the \n included
        for i in paragraph:
            final_p += i
        image = image[:-2]
        img = convert_image(image)
        enqueue(body, header)
        enqueue(body, final_p)
        enqueue(body, img)
        write_paragraph(body, name)

    if "!new_paragraph" not in body_txt:
        return body_txt
    else:
        return get_paragraph(body_txt, body, name)


def end_file(name):
    """
    closes off the body and html tag in the file

    :param name: name of the file
    :return:
    """
    name += ".html"
    file = open(name, "a")
    file.write("</body>\n")
    file.write("</html>")
    file.close()


def build_index(style, title, name):
    """
    builds the file structure up to the closing of head, before body is created.
    within this, is the title and the style in the head section.

    :param style: style class
    :param title: title of the site
    :param name: name of the file
    :return:
    """
    name += ".html"
    index = open(name, "w")


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


def make_link(name, site_files):
    """
    creates and writes the link to the other pages if there are any

    :param name: name of file
    :param site_files: list of files user gave us
    :return:
    """
    name_link = name + ".html"
    file = open(name_link, "a")
    if len(site_files) > 1:
        file.write("<p allign='center'>\n")
        for i in site_files:
            file_link = i + ".html"
            lnk = "<a href='" + file_link + "'>" + i + "</a>"
            file.write(lnk)
            file.write("\n")
        file.write("</p>")
        file.close()
    else:
        file.close()
        pass


def start_body(name, title):
    """
    writes the opening body tag, the title has a header, and a boarder line
    as the hr tag

    :param name: name of file
    :param title: title of page
    :return:
    """
    file_name = name + ".html"
    file = open(file_name, "a")
    file.write("<body>\n")
    file.write("<h1>")
    file.write(title)
    file.write("</h1>")
    file.write("<hr>")
    file.close()


def website_main():
    """
    main file for website mode. gathers the style information and
    stores it. then builds the file(s) from the file(s) they
    ran the program with.

    :return:
    """
    style = style_main()
    site_files = sys.argv[1:]
    for i in site_files:
        name = i
        title = get_title(i)

        body = make_empty_queue()
        body_txt = get_body_txt(i)

        build_index(style, title, name)
        start_body(name, title)
        make_link(name, site_files)


        get_paragraph(body_txt, body, name)
        end_file(name)


def main():
    """
    determines which mode to use. Then goes to either
    wizard mode or website mode. Website mode if the user runs the program
    from the console and includes txt files. Otherwise if the user runs it without
    any other files, it will run in wizard mode.

    Outputs .html file(s)
    :return:
    """
    if len(sys.argv) > 1:
        website_main()
    else:
        wizard_main()

main()