import logging
import traceback
import platform             #used to get OS type for the clear command
import os
from resource import getrusage         #to measure memory usage
#global variables
running = False             #indicates if program is active or not
file_name = ""
txt_file = {}               #temp storage for content
current_line = 1            #indicates last line of file

 
def welcome_screen():
    print('##############################################################')
    print('#                                                            #')
    print('#                                                            #')
    print('#        A SIMPLE CONSOLE TEXT EDITOR MADE IN PYTHON         #')
    print('#                                                            #')
    print('#                                                            #')
    print('##############################################################\n\n')

    global running
    running = True

 
def show_commands():
    print('##############################################################')
    print('Use these command for file:')
    print('*open    *close    *edit    *show    *delete    *help')
    print('Use these command for lines:')
    print('*edit_line')
    print('Enter *exit to exit program')

 
def open_file():
    global file_name
    global txt_file
    global current_line
    clear()
    if file_name == "":
        tmp_name = raw_input('Enter name of the file: ')
        tmp_name += '.txt' 
        file_name = tmp_name
        try:
            if not empty():
                clear()
                read_file()
            #show_file()
        except Exception as e:
            logging.error(traceback.format_exc())       #this part found on stackoverflow need to understand
        print (file_name + ' opened')
    else:
        print ('File could not be opened, incorrect name')

 
def close_file():
    global txt_file
    global file_name
    global current_line
      
    try:
        write_file()
        txt_file.clear()                #reseting all globals
        print(file_name + ' closed.')
        file_name = ""
        current_line = 0
    except Exception as e:
         logging.error(traceback.format_exc())


def edit_file():
    global txt_file
    global current_line
    user_input = 'null'

    print('To exit "edit" mode enter *back command.')
    show_file()
    try:
        while (user_input != '*back'):
            user_input = raw_input()
            if user_input == '*back':
                break
            txt_file[current_line] = user_input
            current_line = current_line + 1
    except Exception as e:
         logging.error(traceback.format_exc())
    print ('Edit mode closed')


def edit_line():
    global txt_file
    global current_line

    user_row = input('Line to edit: ') - 1
    user_input = raw_input()
    if user_row in txt_file:
        txt_file[user_row] = user_input
    else:
        limit = user_row-current_line-1
        for i in range (0, limit):
            txt_file[current_line] = ''
            current_line += 1
        txt_file[current_line] = user_input 


def read_file():
    global txt_file
    global current_line
    global file_name

    file = open(file_name, 'a+')            
    file.seek(0)             
    last = 0                                #counting lines in file
    for line in file.readlines():
        txt_file[last] = line.rstrip('\n')   #getting rid of new line     
        last += 1                           #saving content in temp storage
    current_line = last
    file.close()                                       


def show_file():
    global txt_file
    global current_line
    if not empty():
        for line in range (0, current_line):
            print(txt_file[line])
    else:
        print('File is empty')


def write_file():
    global txt_file
    global file_name
    try:
        file = open(file_name, 'w+')
        for line, text in txt_file.items():
            file.writelines(text + '\n')       #writing text from temp storage to file
        file.flush()
        file.close()
    except Exception as e:
         logging.error(traceback.format_exc())

 
def exit_program():
    global running
    global file_name
    global txt_file
    global current_line
    try:
        if file_name != "" :      #if globals have value means file is still active
            close_file()
        else:           
            file_name = ""
            txt_file.clear()            
            current_line = 0   
    except Exception as e:
         logging.error(traceback.format_exc())
    print('Program ended')
    running = False

 
def get_command():
    user_input = raw_input()
    check_input(user_input)

 
def print_error():
    print('An error has occured, please try again.')

 
def check_input(command):
    dict_of_commands = {   
        '*help' : show_commands,
        '*open' : open_file,
        '*close': close_file,
        '*read' : read_file,
        '*exit' : exit_program,
        '*edit' : edit_file,
        '*show' : show_file,
        '*edit_line' : edit_line
    }
    if dict_of_commands.has_key(command):
        dict_of_commands[command]()
    else:
        print_error()

 
def clear():
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def empty():
    global file_name
 
    if os.path.isfile(file_name):            #if file exist 
        if os.stat(file_name).st_size > 0:   #if not empty
            return False
        else:
            return True
    else:
        file = open(file_name, 'a+')        #if don't exist make one
        file.close()
        return True


def memory_check():
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    kmem = (mem/1024)
    mmem = kmem /1024
    print ( mem )


welcome_screen()
show_commands()
global running
while(running):
    get_command()
