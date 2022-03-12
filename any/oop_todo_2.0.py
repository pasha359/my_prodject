import json
import pickle
from termcolor import colored

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


class My_dikt():
    key = 0
    my_task = {}

    def __init__(self, rezults='Not Done'):
        self.rezults = rezults
        self.key = My_dikt.key
        My_dikt.key += 1
        self.my_task = My_dikt.my_task
        My_dikt.my_task = {}

    def add(self, task):
        while True:
            My_dikt.my_task = self.my_task
            self.my_task[My_dikt.key] = task
            print(colored('Added task', 'green'))
            return self.my_task

    def show(self):
        for key in self.my_task:
            return f'{self.key} - {self.my_task[key]} => {self.rezults}'

    def dell_task(self, key):
        My_dikt.my_task = self.my_task
        if key in self.my_task:
            My_dikt.my_task.pop(key)
            print(colored(f'task is delited', 'green'))
        else:
            print(colored('Number is not exist, reenter number', 'red'))
        return self.my_task

    def update(self, key, new_task):
        My_dikt.my_task = self.my_task
        self.my_task[key] = new_task
        print(colored(f'{new_task} is update','green'))
        return self.my_task


class Dict():
    my_key = []

    def __init__(self, status='Complited!'):
        self.status = status

    def complited(self, key):
        if key in My_dikt.my_task:
            a = strike(My_dikt.my_task[key])
            print(colored(f'{a} => {self.status}','green'))
            My_dikt.my_task[key] = a
        else:
            print(colored('Number of task is not exist', 'red'))
        return My_dikt.my_task

    def filter(self):
        task_complite = {key: value for key, value in My_dikt.my_task.items() if '\u0336' in value}
        for key in task_complite:
            print(colored(f'task => {task_complite[key]} is {self.status}','green'))
        return task_complite

    def mark_task(self, key):
        mark_task = My_dikt.my_task
        if key not in My_dikt.my_task:
            print(colored('Number is not exist => reenter number', 'red'))
        else:
            Dict.my_key.append(key)
            print(colored('Number are mark!', 'green'))
        return mark_task

    def show_mark_task(self):
        if len(Dict.my_key) == 0:
            print(colored('You dont have marking tasks', 'red'))
        for key in Dict.my_key:
            print('mark task', key, '=>', My_dikt.my_task[key])

    def dell_mark_task(self):
        if len(Dict.my_key) == 0:
            print(colored('You dont have marking tasks', 'red'))
        for key in Dict.my_key:
            del My_dikt.my_task[key]
            print(colored('Marked tasks are delited', 'green'))



class Save_json():
    def __init__(self,file_name):
        self.file_name = file_name

    def write_json(self,name):
        self.file_name = open(name, "w")
        self.file_name.write(json.dumps(My_dikt.my_task))
        self.file_name.close()

    def read_json(self,name):
        self.file_name = open(name, "r")
        My_dikt.my_task = json.loads(self.file_name.read())
        self.file_name.close()


class Save_pickle():
    def __init__(self,file_name):
        self.file_name = file_name

    def write_pickle(self,name):
        with open('name.pickle', 'wb') as f:
            pickle.dump(My_dikt.my_task, f)

    def read_pickle(self,name):
        with open('name.pickle', 'rb') as f:
            My_dikt.my_task = pickle.load(f)


def decorat(fun):
    def wrape(*args, **kwargs):
        while True:
            result = fun(*args, **kwargs)
            cont = input('do you want to continue ?, "Y" or any press to exit')
            if cont in ('Y', 'y'):
                continue
            else:
                break
        return result
    wrape.__name__ = fun.__name__
    wrape.__doc__ = fun.__doc__
    return wrape

@decorat
def print_add():
    """add task"""
    while True:
        task = My_dikt()
        task.add(input('enter your task'))
        return task

def print_show():
    """show task"""
    all = My_dikt.my_task
    if len(all) == 0:
        print(colored('You dont have actual tasks', 'red'))
    else:
        for i in all:
            print(colored(f'task number {i} - {all[i]}','green'))
    return 'chose'

@decorat
def dell():
    """to dell task"""
    print(print_show())
    delit = My_dikt()
    delit.dell_task(int(input('enter number to dell')))
    return delit


def print_update():
    """to change task"""
    print(print_show())
    key = int(input('enter number of task'))
    value = input('enter new task')
    task = My_dikt()
    task.update(key, value)
    return task

@decorat
def print_complite():
    """to complite task"""
    print(print_show())
    task = Dict()
    key = int(input('enter number of task'))
    task.complited(key)
    return task

def print_filter():
    """to show complited task"""
    task = Dict()
    task.filter()
    return task

@decorat
def print_mark_task():
    """to mark task"""
    print(print_show())
    task = Dict()
    key = int(input('enter number of task to mark'))
    task.mark_task(key)
    return task

def print_show_mark_task():
    """to see mark task"""
    task = Dict()
    task.show_mark_task()
    return task

def print_dell_mark_task():
    """to del mark task"""
    task = Dict()
    task.dell_mark_task()
    return (colored(f'task {Dict.my_key} is delited', 'green'))

def print_read_file():
    """to read file"""
    choices_task = int(input('what format do yot want to load:\n1-JSON format\n2-PICLE format?'))
    if choices_task == 1:
        file_name = input('Enter filename > ')
        task = Save_json(file_name)
        task.read_json(file_name)
        print(colored("Successfully Loaded!", 'green'))
    else:
        file_name = input('Enter filename > ')
        task = Save_pickle(file_name)
        task.read_pickle(file_name)
        print(colored("Successfully Loaded!", 'green'))

def print_write_file():
    """to write file"""
    choices_task = int(input('what format do yot want to save task:\n1-JSON format\n2-PICLE format?'))
    if choices_task == 1:
        file_name = input('Enter filename > ')
        task = Save_json(file_name)
        task.write_json(file_name)
        print(colored("Successfully Saved!",'green'))
    else:
        file_name = input('Enter filename > ')
        task = Save_pickle(file_name)
        task.write_pickle(file_name)
        print(colored("Successfully Saved!",'green'))

def do_exit():
    """Exit from tasks"""
    a = input('Are you shure ? Y')
    if a in ('Y', 'y'):
        print('Bye!')
        exit()

choices_task = {1: print_add,
                2: print_show,
                3: dell,
                4: print_update,
                5: print_complite,
                6: print_filter,
                7: print_mark_task,
                8: print_show_mark_task,
                9: print_dell_mark_task,
                10:print_write_file,
                11:print_read_file,
                0: do_exit}

def get_commands():
    return '\n'.join(f'{number} - {command.__doc__}' for number, command in choices_task.items())

while True:
    print(get_commands())
    user_input = int(input('enter option  =>'))
    action = choices_task.get(user_input)
    if not action:
        print(colored('option is not exist', 'red'))
        continue
    action()
