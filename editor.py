import logging
import traceback
import platform             #used to get OS type for the clear command
import os

#global variables
running = False             #indicates if program is active or not
file_name = ""
txt_file = {}               #temp storage for content
current_line = 0            #indicates last line of file

#done
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

#done
def show_commands():
    print('##############################################################')
    print('Use these command for file:')
    print('*open    *close    *save    *delete    *help')
    print('Use these command for lines:')
    print('*write   *read    *edit     *edit_line    *insert')
    print('Enter *exit to exit program')

#done
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
            file = open(file_name, 'a+')
            for line in file:
                if not line:
                    break
                txt_file = {current_line : line}
                current_line = current_line + 1
            print ( file_name + ' opened')
            file.close()            #closing file because now content is in dict txt_file
        except Exception as e:
            logging.error(traceback.format_exc())       #this part found on stackoverflow need to understand
    else:
        print ('File could not be opened, incorrect name')

#done
def close_file():
    global txt_file
    global file_name
    global current_line
    
    
    try:
        if len(txt_file) > 0:       #if not empty
            write_file()
            txt_file.clear()        #reseting all global variables
            print(file_name + ' closed.')
            file_name = ""
            current_line = 0
        else:
            print ('did not write')
        
    except Exception as e:
         logging.error(traceback.format_exc())


def edit_file():
    global txt_file
    global current_line
    user_input = 'null'
    try:
        while (user_input != '*back'):
            user_input = raw_input()
            txt_file[current_line] = user_input
            current_line = current_line + 1
    except Exception as e:
         logging.error(traceback.format_exc())
    print ('Edit mode closed')


def edit_line():
    global txt_file
    user_row = input('Line to edit: ')
    user_input = raw_input()
    txt_file[user_row] = user_input
    

def read_file():
    global txt_file
    global current_line
    global file_name

    file = open(file_name, 'r')
    for line in file :
        (number, text) = line.split('\t')
        txt_file[number] = text

    #

#done
def write_file():
    global txt_file
    global file_name
    try:
        file = open(file_name, 'a+')
        for line, text in txt_file.items():
            file.write('%s\t%s\n' %(line, text))       #writing text from dictionary to file
        file.flush()
        file.close()
    except Exception as e:
         logging.error(traceback.format_exc())

#done
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

#done
def get_command():
    user_input = raw_input()
    check_input(user_input)

#done
def print_error():
    print('An error has occured, please try again.')

#done
def check_input(command):
    dict_of_commands = {   
        '*help' : show_commands,
        '*open' : open_file,
        '*close': close_file,
        '*exit' : exit_program,
        '*edit' : edit_file,
        '*edit_line' : edit_line
    }
    if dict_of_commands.has_key(command):
        dict_of_commands[command]()
    else:
        print_error()

#done
def clear():
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


welcome_screen()
show_commands()
global running
while(running):
    get_command()
