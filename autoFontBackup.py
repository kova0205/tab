
# GLOBALS
title_font = "REPLACE TITLE"
dash_font = "DASH FONTTT"
text = ""
new_text = ""

def main_menu():
   print()
   print()
   print("************QA process automation program**************")
   print()

   choice = input("""
    1: Replace font
    2: 
    3: 

    Please enter your choice: """)
   
   return choice

# Finds total lines of page
def find_line():
    #The file is opened in read mode
    file = open("tabtry.txt", "r")

    #The contents of the file are read
    contents = file.read()

    # The current line number is fetched
    line_number = contents.count("\n") + 1

    # The file is closed
    file.close()

    # The current line number is printed
    print("Current line number:", line_number)

# starts at line 0
def line_num_for_phrase_in_file(filename, phrase):
    with open(filename,'r') as f:
        for (i, line) in enumerate(f):
            if phrase in line:
                return i + 1
    return 

# Replace the line at line_number in the file with the provided filename with 
# the text in the string text
def replace_line(filename, line_number, new_text):
  
    
  
  # Open the file and read all the lines from the file into a list 'lines'
  with open(filename) as file:
    lines = file.readlines()
  
  # if the line number is in the file, we can replace it successfully
  if (line_number <= len(lines)):
    
    # Replace the associated line in the list with the replacement text 
    # (followed by a newline \n to end the line), we need to use line_number - 1
    # as the index because lists are zero-indexed in Python.
    lines[line_number - 1] = new_text + "\n"
    
    # Open the file in 'writing mode' using the 2nd argument "w", this means 
    # that the file will be made blank, and any new text we write to the file 
    # will become the new file contents.
    with open(filename, "w") as file:

      # Loop through the list of lines, write each of them to the file
      for line in lines:
        file.write(line)
  
  # otherwise if the line number is past the length of the file, we can't 
  # replace the line so output an error message instead
  else:
  
    # Output the line number that was requested to be replaced and the number
    # of lines the file actually has to inform the user
    print("Line", line_number, "not in file.")
    print("File has", len(lines), "lines.")


def replace_font(text,new_text):
   # Prompt the user for the filename, line number and replacement text
    filename = input("File: ")
    #text = "<workbook source-platform='mac' version='9.0' xmlns:user='http://www.tableausoftware.com/xml/user'>"
    
    line_number = int(line_num_for_phrase_in_file(filename,text))

    # This is finding my line number of a phrase

    #line_num_for_phrase_in_file(filename,text)


    # Call the replace_line() function to replace the text at the line number 
    # 'line_number' in the file with the filename 'filename' with the replacement 
    # text 'text'.
    replace_line(filename, line_number, new_text)


    

# MAIN

choice = main_menu()

if choice == "1":
    print('''
    What font do you want to replace
    1.Dash Title
    2.Dash all text''')
    replace_type = input("Enter:")
    if replace_type == "1":
       new_text = "THIS IS A TITLE"
       text = "fSDdsdsfsdffsdffsdfsdff"
       replace_font(text,new_text)
    elif replace_type == "2":
       new_text = "<preference name='ui.shelf.height' value='280' />"
       text = "<preference name='ui.shelf.height' value='250' />"
       replace_font(text,new_text)
       





   



















  
    



    