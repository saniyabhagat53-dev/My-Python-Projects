import tkinter as tk
import random

WIDTH = 600
HEIGHT = 500
SIZE = 20

root = tk.Tk()
root.title("Advanced Snake Game")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#101820")
canvas.pack()


snake = []
food = []
direction = "Right"

score = 0
high_score = 0
speed = 120

game_running = False
paused = False


def create_snake():
    global snake
    snake = [
        [120,100],
        [100,100],
        [80,100]
    ]


def create_food():
    global food

    food = [
        random.randint(0,(WIDTH-SIZE)//SIZE)*SIZE,
        random.randint(0,(HEIGHT-SIZE)//SIZE)*SIZE
    ]


def draw():

    canvas.delete("all")

    canvas.create_oval(
        food[0],
        food[1],
        food[0]+SIZE,
        food[1]+SIZE,
        fill="orange",
        outline=""
    )

    
    for i,part in enumerate(snake):
        color = "#00ff99" if i==0 else "#00cc66"

        canvas.create_rectangle(
            part[0],
            part[1],
            part[0]+SIZE,
            part[1]+SIZE,
            fill=color,
            outline=""
        )


    canvas.create_text(
        70,
        20,
        text=f"Score : {score}",
        fill="white",
        font=("Arial",16,"bold")
    )



def move():

    global score,speed

    if not game_running or paused:
        return

    head = snake[0].copy()

    if direction=="Up":
        head[1]-=SIZE

    elif direction=="Down":
        head[1]+=SIZE

    elif direction=="Left":
        head[0]-=SIZE

    else:
        head[0]+=SIZE


    if (
        head in snake or
        head[0]<0 or
        head[1]<0 or
        head[0]>=WIDTH or
        head[1]>=HEIGHT
    ):
        end_game()
        return


    snake.insert(0,head)


    if head==food:
        score+=1
        speed=max(50,speed-5)
        create_food()

    else:
        snake.pop()


    draw()

    root.after(speed,move)



def change(event):

    global direction

    key=event.keysym

    if key=="Up" and direction!="Down":
        direction="Up"

    elif key=="Down" and direction!="Up":
        direction="Down"

    elif key=="Left" and direction!="Right":
        direction="Left"

    elif key=="Right" and direction!="Left":
        direction="Right"



def start():

    global game_running,score,speed,direction

    score=0
    speed=120
    direction="Right"

    create_snake()
    create_food()

    game_running=True
    move()



def pause():

    global paused
    paused = not paused



def end_game():

    global game_running

    game_running=False

    canvas.create_text(
        WIDTH/2,
        HEIGHT/2,
        text="GAME OVER",
        fill="red",
        font=("Arial",40,"bold")
    )



start_btn=tk.Button(
    root,
    text="START GAME",
    command=start,
    font=("Arial",14)
)

start_btn.pack(pady=5)


pause_btn=tk.Button(
    root,
    text="PAUSE / RESUME",
    command=pause,
    font=("Arial",12)
)

pause_btn.pack()


root.bind("<KeyPress>",change)

root.mainloop()
