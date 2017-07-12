#!/usr/bin/env python3

import tkinter as tk
import random, os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from time import sleep

class Data:
    people = []
    x = 0

def empty():
    pass

def decide(n, repeat):
    i = random.randrange(n)
    output_label["text"] = Data.people[i]
    if Data.x < repeat:
        root.after(50, decide, n, repeat)
        Data.x += 1
    else:
        Data.x = 0

def run():
    n = len(Data.people)
    if n >= 1:
        decide(n, 100)
    else:
        clear_output_labels()
        output_label["text"] = "You need at least 1 people."

def run_event(event):
    run()

def add():
    new_person = add_person_text.get()
    if new_person != "":
        Data.people.append(new_person)
        people_listbox.insert("end", new_person)
    add_person_text.set("")

def add_event(event):
    add()

def save_to_file():
    path = asksaveasfilename(defaultextension=".txt")
    with open(path, "w", encoding="utf-8") as lines:
        for person in Data.people:
            lines.writelines(person)
            lines.write("\n")

def load_from_file():
    path = askopenfilename()
    with open(path, "r", encoding="utf-8") as lines:
        Data.people.extend(lines)

    for person in Data.people:
        people_listbox.insert("end", person)

    people_label["text"] = "People (367 Submissions)"


def remove():
    try:
        i = people_listbox.curselection()[0]
        Data.people.pop(i)
        people_listbox.delete(i)
        clear_output_labels()
    except IndexError:
        clear_output_labels()
        output_label["text"] = "You haven't selected anyone."

def remove_event(event):
    remove()

def clear():
    Data.people = []
    people_listbox.delete(0, "end")
    clear_output_labels()

def clear_output_labels():
    output_label["text"] = ""
    arrow_label["text"] = ""
    people_label["text"] = "People"

root = tk.Tk()
root.title("Raffler by @dorukgezici")
root.geometry("1000x700+150+50")
root.minsize(width=1000, height=700)

header = tk.Label(root, text="Raffler", font=("Roboto", 44), padx=10, pady=10)
header.pack()

img_path = os.path.dirname(os.path.abspath(__file__)) + "/logo.gif"
img = tk.PhotoImage(file=img_path)
img_size = (310, 161)
logo = tk.Canvas(width=img_size[0], height=img_size[1])
logo.create_image(img_size[0]/2, img_size[1]/2, image=img, anchor=tk.CENTER)
logo.pack()

left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=30, pady=30, fill="both")

people_label = tk.Label(left_frame, text="People")
people_label.pack()

people_listbox = tk.Listbox(left_frame)
people_listbox.pack(side="left", fill="y")
people_listbox.bind("<BackSpace>", remove_event)

right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=30, pady=30, fill="both")

add_person_text = tk.StringVar()
add_person_entry = tk.Entry(right_frame, textvariable=add_person_text, width=200)
add_person_entry.pack()
add_person_entry.bind("<Return>", add_event)

list_buttons = tk.Frame(right_frame)
list_buttons.pack()

add_person_button = tk.Button(list_buttons, text="ADD", command=add)
add_person_button.pack(side="left")

remove_person_button = tk.Button(list_buttons, text="REMOVE", command=remove)
remove_person_button.pack(side="left")

load_from_file_button = tk.Button(list_buttons, text="LOAD FROM FILE", command=load_from_file)
load_from_file_button.pack(side="right")

save_to_file_button = tk.Button(list_buttons, text="SAVE TO FILE", command=save_to_file)
save_to_file_button.pack(side="right")

output_frame = tk.Frame(right_frame)
output_frame.pack(pady=80)

output_label = tk.Label(output_frame, font=("Roboto", 50))
output_label.pack()

arrow_label = tk.Label(output_frame)
arrow_label.pack()

buttons_frame = tk.Frame(right_frame)
buttons_frame.pack(side="bottom")

credits = tk.Label(buttons_frame, text="coded by @dorukgezici")
credits.pack(side="right", padx=50)

quit_button = tk.Button(buttons_frame, text="QUIT", command=root.destroy)
quit_button.pack(side="right")

clear_button = tk.Button(buttons_frame, text="CLEAR", command=clear)
clear_button.pack(side="right")

run_button = tk.Button(buttons_frame, text="RUN", command=run)
run_button.pack(side="left")

root.lift()
root.bind("<Command-r>", run_event)
root.mainloop()
