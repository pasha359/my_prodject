import json

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

my_task = {}
my_key=[]

def decorat (fun):
    def wrape (*args,**kwargs):
        while True:
            result=fun(*args,**kwargs)
            cont = input('do you want to continue ?, y/ or any press to exit')
            if cont in ('Y','y'):
                continue
            else:
                break
        return result
    wrape.__name__=fun.__name__
    wrape.__doc__=fun.__doc__
    return wrape

def show():
    """to show my tasks"""
    for i in my_task:
        print(i, '-', my_task[i])
    return "My Task's"

@decorat
def add_task():
    """to add new task"""
    while True:
        try:
            key = int(input('enter number your task'))
        except ValueError:
            print('Not number, reenter number')
            continue
        if key in my_task:
            print('Number is exist, enter new number')
            continue
        value = input('enter your task')
        my_task[key] = value
        break

@decorat
def dell():
    """to dell task"""
    while True:
        print(show())
        del_input = int(input('enter number to dell task'))
        if del_input not in my_task:
            print('Number is not found, enter number')
            continue
        delite=my_task.pop(del_input)
        print(delite, 'Is delite')
        break
    return 'Ready!'

@decorat
def update():
    """to update my task"""
    while True:
        print(show())
        task = int(input('enter number of task to rechange'))
        if task not in my_task:
            print('Number is not found, enter number')
            continue
        new_task = input('to change your task')
        my_task[task] = new_task
        break
    return "ready, task is change!"

@decorat
def complite():
    """to complite task"""
    while True:
        print(show())
        task_complite = int(input('enter number of task to complite'))
        if task_complite not in my_task:
            print('Number is not found, enter number')
            continue
        a = strike(my_task[task_complite])
        print(a,'Comlite!')
        my_task[task_complite] = a
        break
    return "ready, tasks are complited!"

def my_filter(completed=True):
    """to show complited task"""
    my_task_complite = {key: value for key, value in my_task.items() if '\u0336' in value}
    for key in my_task_complite:
        print(key, my_task_complite[key])
    return my_task_complite

@decorat
def mark_task():
    """to mark task"""
    while True:
        print(show())
        key = int(input('enter number your task'))
        if key not in my_task or key in my_key:
            print('No task or yet exist task')
            continue
        my_key.append(key)
        print('Number are mark!')
        break
    return my_key

def show_mark_task():
    """to see mark task"""
    for key in my_key:
        print(key, my_task[key])

def dell_mark_task ():
    """to del mark task"""
    for key in my_key:
        del my_task[key]
        print('Ready!')

def read_tasks(file_name):
    file = open(file_name)
    data = json.loads(file.read())
    file.close()
    global my_task


def write_tasks(file_name):
    file = open(file_name, 'w')
    file.write(json.dumps(my_task))
    file.close()

def command_read_file():
    """to read file"""
    file_name = input('Enter filename > ')
    read_tasks(file_name)

def command_write_file():
    """to write file"""
    file_name = input('Enter filename > ')
    write_tasks(file_name)

def do_exit ():
    """Exit from tasks"""
    a=input('Are you shure ? Y')
    if a in ('Y','y'):
        print('Bye!')
        exit()

choices_task = {1: show,
                2: add_task,
                3: update,
                4: dell,
                5: complite,
                6: my_filter,
                7: mark_task,
                8: show_mark_task,
                9: dell_mark_task,
                10: command_read_file,
                11: command_write_file,
                0: do_exit}

def get_commands ():
    return '\n'.join(f'{number} - {command.__doc__}' for number, command in choices_task.items())

while True:
    print(get_commands())
    user_input = int(input('enter option  =>'))
    action = choices_task.get(user_input)
    if not action:
        print('option is not exist')
        continue
    action()




