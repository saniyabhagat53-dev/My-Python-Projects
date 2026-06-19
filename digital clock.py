from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("600x300")
root.configure(bg="#1e1e36")

title = Label(root,
              text="PYTHON DIGITAL CLOCK",
              font=("Arial", 18, "bold"),
              bg="#1e1e2f",
              fg="#ffd166")
title.pack(pady=(30, 20))

clock = Label(root,
              font=("Arial", 42, "bold"),
              bg="#2b2d42",
              fg="#00f5d4",
              padx=30, pady=30,
              relief="raised", bd=8)
clock.pack(pady=30)

date_label = Label(root,
                   font=("Arial", 14),
                   bg="#1e1e2f",
                   fg="#ffffff")
date_label.pack()
name_label = Label(root,
                   text="Created By Saniya Bhagat | InternPe",
                   font=("Arial", 12, "bold"),
                   bg="#1e1e2f",
                   fg="#ffb703")
name_label.pack(pady=30)


def update_time():
    current_time = strftime("%I:%M:%S %p")
    current_date = strftime("%A, %d %B %Y")

    clock.config(text=current_time)
    date_label.config(text=current_date)
    clock.after(1000, update_time)

update_time()
root.mainloop()
