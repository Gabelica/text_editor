
# cilj je maknit sve di se koristi global file i zaminit ga s rijecnikom 
# global file se triba koristit samo kad otvaram i kad zatvaram file
#global variables 
running = False             #if program is running or not
file_name = ""         
file = ""
txt_file = {} 
current_line = 0            #number of the last line in file
        

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
    print('*write   *read    *edit     *edit_line    *insert')
    print('Enter *exit to exit program')


def exit_program():
    global running
    global file 
    try: 
        file.readline()
        close_file()
    except:
        print('exiting program')
    running = False


def open_file():
    global file_name
    global file
    global current_line
    #check if another file is opened
    if file_name == "":
        try:
            tmp_name = raw_input("Enter name of the file: ")
            tmp_name += '.txt' #can not change global variable directly
            file_name = tmp_name
            file = open(tmp_name, 'a+')
            print(tmp_name + ' opened')
            try:
                for line in file:
                    if not line:
                        break
                    txt_file = {current_line : flie.readline()}
                    current_line = current_line + 1
            except:
                print ('File is empty\n')
        except:
            print 'Error occured while opening file'
    else:
        print 'Could not open file'
        file.close()


def close_file():
    try:
        global file_name
        global txt_file

        write_to_file()                     #writing text from dict to file before closing
        print ('%s closed' %file_name)
        txt_file.clear()               #empty everything
        file = ""
        file_name = ""
    except:
        print('File not oppened')

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
            if command == '*delete':
                delete_line()
                return            
            if command == '*write':
                write()
                return
            if command == '*edit':
                write()
                return
            if command == '*read':
                read()
                return
            if command == '*edit_line':
                edit_line()
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
    global current_line
    global txt_file
    user_input = 'null'
    try:
        while (user_input != '*back'):
            user_input = raw_input()
            txt_file = { current_line : user_input }
            current_line = current_line + 1
    except:
        print('No file opened\n')
    print ('Edit mode closed')


def write_to_file():
    global txt_file
    global file_name
    file = open(file_name, 'a+')
    for line, text in txt_file.items():
        file.write('%s\t%s\n' %(line, text))       #writing text from dictionary to file
    file.flush()


def read():
    print ('read')


def print_to_console(text):
    for line in text:
        print('%s\n' %line)


def edit_line():
    global file
    row = input('Which line to edit: ')
    text = raw_input('Text to replace: \n')
    lines = []
    for line in file:
        lines.append(line)
    lines[row] = text
    for line in lines:
        if line == row:
            file.write('%s\t%s\n' %(row, line))
        else:
            file.write('%s\n' %line)


# make edit write and read function 


welcome_screen()
show_commands()
global running 
while(running):
    get_command()


 

