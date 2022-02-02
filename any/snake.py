from tkinter import *
import random
import time
Game_Running = True

screen_widht = 300
screen_height = 300
snake_item = 10
snake_color1 = 'red'
snake_color2 = 'black'
virtual_game_x = screen_widht//snake_item
virtual_game_y = screen_height//snake_item
snake_x = virtual_game_x//2
snake_y = virtual_game_y//2
snake_x_navigation = 0
snake_y_navigation = 0

snake_list = []
snake_size = 4

tk = Tk()
tk.title('Game snaike')
tk.wm_attributes('-topmost',1)
tk.resizable(0,0)
canvas = Canvas(tk, width=screen_widht, height=screen_height,bd=0)
canvas.pack()


present_color1 = 'black'
present_color2 = 'yellow'
present_list = []
prezent_size = 5

hill_color = 'green'
hill_list = []
hill_size = 2


for i in range(prezent_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x * snake_item, y * snake_item,
                                  x * snake_item + snake_item, y * snake_item + snake_item,
                                  fill=present_color1)
    id2 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2,
                                  x * snake_item + snake_item - 2, y * snake_item + snake_item - 2,
                                  fill=present_color2)
    present_list.append([x,y,id1,id2])
    print(present_list[-1])

for i in range(hill_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id = canvas.create_oval(x * snake_item, y * snake_item,
                             x * snake_item + snake_item, y * snake_item + snake_item,
                             fill=hill_color)
    hill_list.append([x, y, id])
    print(hill_list[-1])

def hill_action():
    global snake_size
    for i in range(len(hill_list)):
        if hill_list[i][0] == snake_x and hill_list[i][1] == snake_y:
            snake_size = snake_size-1
            canvas.delete(hill_list[i][2])
        print(snake_x,snake_y)


def snake_paint_item (canvas,x,y):
    global snake_list
    id1 = canvas.create_rectangle(x*snake_item,y*snake_item,
                            x*snake_item+snake_item,y*snake_item+snake_item,
                            fill=snake_color1)
    id2 = canvas.create_rectangle(x * snake_item+2, y * snake_item+2,
                            x * snake_item + snake_item-2, y * snake_item + snake_item-2,
                            fill=snake_color2)
    snake_list.append([x,y,id1,id2])
    print(snake_list)

snake_paint_item(canvas,snake_x,snake_y)

def chek_can_we_delit():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])
        # print(temp_item)

def check_we_find_present():
    global snake_size
    for i in range(len(present_list)):
        if present_list[i][0] == snake_x and present_list[i][1] == snake_y:
            snake_size = snake_size+1
            canvas.delete(present_list[i][2])
            canvas.delete(present_list[i][3])
        print(snake_x,snake_y)


def snake_move (event):
    global snake_x
    global snake_y
    global snake_x_navigation
    global snake_y_navigation

    if event.keysym == 'Up':
        snake_x_navigation = 0
        snake_y_navigation = -1
        chek_can_we_delit()
    elif event.keysym == 'Down':
        snake_x_navigation = 0
        snake_y_navigation = 1
        chek_can_we_delit()
    elif event.keysym == 'Right':
        snake_x_navigation = 1
        snake_y_navigation = 0
        chek_can_we_delit()
    elif event.keysym == 'Left':
        snake_x_navigation = -1
        snake_y_navigation = 0
        chek_can_we_delit()
    snake_x = snake_x + snake_x_navigation
    snake_y = snake_y + snake_y_navigation
    snake_paint_item(canvas, snake_x, snake_y)
    check_we_find_present()
    hill_action()

canvas.bind_all('<KeyPress-Left>', snake_move)
canvas.bind_all('<KeyPress-Right>',snake_move)
canvas.bind_all('<KeyPress-Up>',snake_move)
canvas.bind_all('<KeyPress-Down>',snake_move)

def game_over():
    global Game_Running
    canvas.create_text(250,250, text = 'Game Over')

def check_if_borders ():
    if snake_x > virtual_game_x or snake_x < 0 or snake_y > virtual_game_y or snake_y < 0:
        game_over()

def check_we_touch_self(future_x,future_y):
    global Game_Running
    if not (snake_x_navigation == 0 and snake_y_navigation == 0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == future_x and snake_list[i][1] == future_y:
                Game_Running = False


while Game_Running:
    chek_can_we_delit()
    check_we_find_present()
    check_if_borders ()
    hill_action()


    check_we_touch_self(snake_x + snake_x_navigation, snake_y + snake_y_navigation)
    snake_x = snake_x + snake_x_navigation
    snake_y = snake_y + snake_y_navigation
    snake_paint_item(canvas, snake_x, snake_y)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.15)




