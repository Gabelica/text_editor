import time
import os
#global variables 
running = False             #if program is running or not
file_name = "empty"         
file = ""
current_line = 0            #number of the last line in file

def get_curr_line():
    global current_line
    return current_line


def curr_line_inc():
    global current_line
    current_line = current_line + 1


def welcome_screen():
    print('##############################################################')
    print('#                                                            #')
    print('#                                                            #')
    print('#        A SIMPLE CONSOLE TEXT EDITOR MADE IN PYTHON         #')
    print('#                                                            #')
    print('#                                                            #')
    print('##############################################################')
    print('')
    print('')
    global running
    running = True


def show_commands():
    print('##############################################################')
    print('Use these command for file:')
    print('*open    *close    *save    *delete    *help')
    print('Use these command for lines:')
    print('*write   *delete    *edit    *insert')
    print('Enter *exit to exit program')


def exit_program():
    global running
    global file 
    try: 
        file.readline()
        close_file()
    except:
        print'exiting program'
    running = False


def open_file():
    global file_name
    global file
    global current_line
    #check if another file is opened
    if file_name == "empty":
        try:
            tmp_name = raw_input("Enter name of the file: ")
            tmp_name += '.txt' #can not change global variable directly
            file_name = tmp_name
            file = open(tmp_name, 'a+')
            print(tmp_name + ' opened')

        except:
            print 'Error occured while opening file'
    else:
        print 'File already opened, please close it first'


def close_file():
    try:
        global file
        global file_name
        file.close()
        print ('%s closed' %file_name)
        file = ""
        file_name = "empty"
        return 0
    except:
        print('File not oppened')
        return 0

#gets number of lines in file so it can continue to write line numbers, still have to make it work
#def get_last_line():            


def get_command():
    user_input = raw_input()
    check_input(user_input)
    
#implementing sort of switch case  maybe better do it with list and iterator
def check_input(command):  

    if command[0] == '*':
        for case in command:
            if command == '*open':
                open_file()
                return
            if command == '*close':
                close_file()
                return
            if command == '*save':
                return
            if command == '*write':
                write_line()
                return
            if command == '*delete':
                delete_line()
                return
            if command == '*edit':
                write()
                return
            if command == '*edit':
                write()
                return  
            if command == '*help':
                show_commands()
                return
            if command == '*exit':
                exit_program()
                return
        print('unknown command')
        return
    else:
        print 'unknown command'
        return


def write():
    global file
    global current_line
    if file:
        content = 'null'
        lines = {}
        print('To exit write mode enter *back')
        while (content != '*back'):
            content = raw_input()
            lines[current_line] = content       #adding curent input to dictionary
            current_line = current_line + 1     #incrementing last line in file

        for line, text in lines.items():
            file.write('%s\t%s\n' %(line, text))       #writing text from dictionary to file

        file.flush()
        print('Edit mode closed.')
        return 
    else:
        print ('No file opened')

# make edit write and read function 


welcome_screen()
show_commands()
global running 
while(running):
    get_command()


 

