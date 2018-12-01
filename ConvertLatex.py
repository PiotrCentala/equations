#!/usr/bin/env python3.
import glob
import os



try:
    list_of_files = glob.glob('/home/piotr/Downloads/*.tex')
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    f = open(latest_file, "r", encoding="utf8")

    # Next, get all your lines from the file:

    lines = f.readlines()

    # Now you can close the file:

    f.close()

    # And reopen it in write mode:

    f = open(latest_file, "w", encoding="utf8")

    # Then, write your lines back, except the line you want to delete.

    code_line = False

    for line in lines:
        if code_line == False and "commandchars" in line:
            code_line = True
        elif code_line == True and "Verbatim" in line:
            code_line = False
        elif code_line == True and "Verbatim" not in line:
            pass
        elif code_line == False and "color{outcolor}" in line:
            pass
        elif code_line ==False and "\documentclass[11pt]{article}" in line:
            f.write(line + "\n" + "\\usepackage[export]{adjustbox}" + "\n" + "\\usepackage{float}" + "\n")
        elif code_line ==False and "\\usepackage{caption}" in line :
            f.write("\\usepackage[format=plain,font=it]{caption}")
        elif code_line ==False and "\\renewcommand{\\includegraphics}[1]{\\Oldincludegraphics[width=.8\\maxwidth]{#1}}" in line:
            f.write("\\renewcommand{\\figurename}{Rys.}")
        elif code_line ==False and "\DeclareCaptionLabelFormat{nolabel}{}" in line:
            pass
        elif code_line == False and "linkcolor=linkcolor," in line:
            f.write("linkcolor=black,")
        
        elif code_line ==False and "\captionsetup{labelformat=nolabel}" in line:
            pass        
        elif code_line == False and "geometry{verbose,tmargin=1in,bmargin=1in,lmargin=1in,rmargin=1in}" in line:
            f.write(line + "\\renewcommand{\\contentsname}{Spis treści}" + "\n")
        else:
            f.write(line)


    # At the end, close the file again.

    f.close()
except Exception as e:
    print(e)
    var = input("Please enter something error: ")
var = input("Please enter something: ")
