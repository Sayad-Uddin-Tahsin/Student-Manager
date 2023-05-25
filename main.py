import datetime
import json
import tkinter as tk
import tkinter.ttk
from typing import TYPE_CHECKING
from tkinter import font
from PIL import ImageTk, Image, ImageFont

# Declare the type of the window variable
if TYPE_CHECKING:
    mWindow: tk.Tk

icon = "./assets/UCC With BG.ico"
lFrame = None
mWindow = None


def assign_new_student(_class):
    def handle_id_lock():
        state = ID_Entey.cget("state")
        if state == "normal":
            ID_Entey.configure(state=tk.DISABLED)
            lock_button.configure(text="🔓")
        elif state == 'disabled':
            ID_Entey.configure(state=tk.NORMAL)
            lock_button.configure(text="🔒")

    def validate_Fcontact_entry(text):
        if text.isdigit() or text == "":
            if len(text) <= 11:
                x, y = FContactPrefix_Entey.winfo_x(), FContactPrefix_Entey.winfo_y()
                FContact_error.configure(text="* Number must be 11 in length!", font=("./Assets/Segoe UI.ttf", 8, 'italic'), fg='red')
                FContact_error.place(x=x, y=y + 19)
                if len(text) == 11:
                    FContact_error.configure(text="")
                    FContact_error.place(x=36000, y=10000)
                    return True
                return True
            else:
                return False
        else:
            x, y = FContactPrefix_Entey.winfo_x(), FContactPrefix_Entey.winfo_y()
            FContact_error.configure(text="* Number must be integer!", font=("./Assets/Segoe UI.ttf", 8, 'italic'),
                                     fg='red')
            FContact_error.place(x=x, y=y + 19)
            return False

    def validate_Mcontact_entry(text):
        if text.isdigit() or text == "":
            if len(text) <= 11:
                x, y = MContactPrefix_Entey.winfo_x(), MContactPrefix_Entey.winfo_y()
                MContact_error.configure(text="* Number must be 11 in length!", font=("./Assets/Segoe UI.ttf", 8, 'italic'), fg='red')
                MContact_error.place(x=x, y=y + 19)
                if len(text) == 11:
                    MContact_error.configure(text="")
                    MContact_error.place(x=36000, y=10000)
                    return True
                return True
            else:
                return False
        else:
            x, y = MContactPrefix_Entey.winfo_x(), MContactPrefix_Entey.winfo_y()
            MContact_error.configure(text="* Number must be integer!", font=("./Assets/Segoe UI.ttf", 8, 'italic'),
                                     fg='red')
            MContact_error.place(x=x, y=y + 19)
            return False

    window = mWindow
    # Clear the existing content of the window
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("650x400+400+120")
    window.iconbitmap(icon)
    window.title(f"Assigning Student on {_class}")
    window.resizable(0, 0)

    with open('data.json', 'r') as f:
        classDB = json.load(f)

    back_button = tkinter.ttk.Button(window, text="🡸", style='W.TButton', command=lambda cls=_class: handle_class_select(cls, False), width=3)
    back_button.place(x=590, y=5)

    ID_Entey = tk.Entry(window)
    ID_Entey.place(x=40, y=15)
    ID_text = tk.Label(window, text="ID:", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    ID_text.place(x=10, y=12)
    ID_Entey.insert(tk.END, f"{datetime.datetime.today().strftime('%y')}{_class.replace('Class: ', '')}B{'01' if str(_class) not in classDB else '0' + str(len(classDB[_class]) + 1) if len(str(len(classDB[_class]))) == 1 else len(classDB[_class])}")
    ID_Entey.configure(state=tk.DISABLED)
    lock_button = tkinter.ttk.Button(window, text="🔓", style='W.TButton', command=handle_id_lock, width=3)
    lock_button.place(x=170, y=13)

    Name1_Entey = tk.Entry(window, width=35)
    Name1_Entey.place(x=105, y=45)
    Name1_text = tk.Label(window, text="First Name:", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    Name1_text.place(x=10, y=42)
    Name2_Entey = tk.Entry(window, width=20)
    Name2_Entey.place(x=455, y=45)
    Name2_text = tk.Label(window, text="Last Name:", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    Name2_text.place(x=360, y=42)

    FatherName_Entey = tk.Entry(window, width=35)
    FatherName_Entey.place(x=130, y=80)
    FatherName_text = tk.Label(window, text="Father's Name:", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    FatherName_text.place(x=10, y=76)
    FContactPrefix_Entey = tk.Entry(window, width=4)
    FContactPrefix_Entey.place(x=435, y=80)
    FContactPrefix_Entey.insert(0, " +88")
    FContactPrefix_Entey.configure(state=tk.DISABLED)
    FContact_Entey = tk.Entry(window, width=20)
    FContact_Entey.place(x=462, y=80)
    FContact_text = tk.Label(window, text="Contact:", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    FContact_text.place(x=360, y=77)
    validate_cmd = window.register(validate_Fcontact_entry)
    FContact_Entey.config(validate="key", validatecommand=(validate_cmd, "%P"))
    FContact_error = tk.Label(window, text="")
    FContact_error.place(x=1000, y=1000)

    MotherName_Entey = tk.Entry(window, width=35)
    MotherName_Entey.place(x=130, y=120)
    MotherName_text = tk.Label(window, text="Mother's Name:", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    MotherName_text.place(x=10, y=117)
    MContactPrefix_Entey = tk.Entry(window, width=4)
    MContactPrefix_Entey.place(x=435, y=120)
    MContactPrefix_Entey.insert(0, " +88")
    MContactPrefix_Entey.configure(state=tk.DISABLED)
    MContact_Entey = tk.Entry(window, width=20)
    MContact_Entey.place(x=462, y=120)
    MContact_text = tk.Label(window, text="Contact:", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    MContact_text.place(x=360, y=117)
    validate_cmd = window.register(validate_Mcontact_entry)
    MContact_Entey.config(validate="key", validatecommand=(validate_cmd, "%P"))
    MContact_error = tk.Label(window, text="")
    MContact_error.place(x=1000, y=1000)

    window.mainloop()


def handle_class_select(item, sendToNewClass):
    if sendToNewClass:
        return handle_new_class()

    with open("data.json", 'r') as f:
        db = json.load(f)

    if f"Class: {item}" in db:
        students = []
        classDB = db[f"Class: {item}"]
        for id in classDB:
            students.append(
                (id, classDB[id]['Name'])
            )
    else:
        students = []

    window = mWindow
    # Clear the existing content of the window
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("650x400+400+120")
    window.iconbitmap(icon)
    window.title(f"Viewing {item}")
    window.resizable(0, 0)

    def handle_student_click(event):
        selected_item = students_treeview.focus()
        if selected_item:
            student_info = students_treeview.item(selected_item, "values")
            print("Selected student information:", student_info)

    # Create a Treeview to display the student information
    students_treeview = tkinter.ttk.Treeview(window, columns=("id", "name"), show="headings", height=13)
    students_treeview.place(x=15, y=105, fill=None)

    students_treeview.column("id", width=200)
    students_treeview.column("name", width=400)
    # Add columns to the Treeview
    students_treeview.heading("id", text="ID")
    students_treeview.heading("name", text="Name")

    # Create a Scrollbar
    scrollbar = tkinter.ttk.Scrollbar(window, orient="vertical", command=students_treeview.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Treeview to use the Scrollbar
    students_treeview.configure(yscrollcommand=scrollbar.set)

    for student in students:
        students_treeview.insert("", tk.END, values=student)

    # Bind the click event to the Treeview
    students_treeview.bind("<Double-1>", handle_student_click)

    with open("data.json", 'r') as f:
        datum = json.load(f)

    class_text = tk.Label(window, text=item, font=("./Assets/Segoe UI.ttf", 16, 'bold'))
    class_text.place(x=10, y=10)
    total_students = tk.Label(window, text=f"Total Students: {0 if item not in datum else len(datum[item])}", font=("./Assets/Segoe UI.ttf", 9, 'bold'))
    total_students.place(x=12, y=48)

    add_button = tkinter.ttk.Button(window, text="Assign New Student", style='W.TButton', command=lambda cls=item: assign_new_student(cls))
    add_button.place(x=503, y=45)

    back_button = tkinter.ttk.Button(window, text="🡸", style='W.TButton', command=lambda: main(True), width=3)
    back_button.place(x=590, y=5)

    window.mainloop()


def handle_back_to_main():
    main(isBack=True)


def handle_new_class():
    def save_class():
        global lFrame

        class_int = int(entry.get())
        with open("data.json", 'r') as f:
            datum = json.load(f)
        if 'classes' in datum:
            datum['classes'].append(class_int)
        else:
            datum['classes'] = [class_int]
        with open('data.json', 'w') as f:
            json.dump(datum, f, indent=4)

        window.destroy()
        refresh_class_list(lFrame)

    def handle_class_entry_event(event):
        save_class()

    def handle_focus_in(event):
        # Get the current text
        text = entry.get()

        # If the current text is the placeholder, clear it
        if text == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def handle_focus_out(event):
        # Get the current text
        text = entry.get()

        # If the current text is empty, set the placeholder
        if text.strip() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    def validate_entry(text):
        with open("data.json", 'r') as f:
            datum = json.load(f)
        if text.isdigit() or text == "":
            if text == "":
                error.config(text="")
                save_button.config(state=tk.NORMAL)
                save_button.place(y=52)
                return True
            else:
                if text != "" and int(text) in datum['classes']:
                    # The entered text is valid (either digits or empty)
                    error.config(text="")
                    save_button.place(y=52)
                    # The entered text contains non-digit characters
                    error.config(text=f"* Class {int(text)} already exists!",
                                 font=("./Assets/Segoe UI.ttf", 8, 'italic'),
                                 fg="red")
                    error.place(x=65, y=47)
                    save_button.config(state=tk.DISABLED)
                    save_button.place(y=68)
                    return True
                else:
                    error.config(text="")
                    save_button.config(state=tk.NORMAL)
                    save_button.place(y=52)
                    return True
        elif not text.isdigit():
            # The entered text contains non-digit characters
            error.config(text="* Class must be a number! Ex. 9", font=("./Assets/Segoe UI.ttf", 8, 'italic'),
                         fg="red")
            error.place(x=28, y=47)
            save_button.place(y=68)
            return False
        else:
            pass

    window = tk.Tk()
    window.geometry("250x130+400+120")
    window.iconbitmap(icon)
    window.title("New Class")
    window.resizable(0, 0)

    classes_text = tk.Label(window, text="Enter the Class", font=("./Assets/Segoe UI.ttf", 11, 'bold'))
    classes_text.place(x=5, y=5)
    error = tk.Label(window, text="")
    error.place(x=5, y=45)

    # Create a label to show the error message
    error_label = tk.Label(window, fg="red")
    error_label.place(x=10000, y=10000)

    # Placeholder text
    placeholder = "Enter class here. Ex. 9"

    # Create the entry widget
    entry = tk.Entry(window, width=30, fg="gray")
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", handle_focus_in)
    entry.bind("<FocusOut>", handle_focus_out)
    entry.bind("<Return>", handle_class_entry_event)
    entry.place(x=8, y=30)

    # Set the validation command
    validate_cmd = window.register(validate_entry)
    entry.config(validate="key", validatecommand=(validate_cmd, "%P"))

    save_button = tkinter.ttk.Button(window, text="Save", style='W.TButton', command=save_class)
    save_button.place(x=117, y=52)

    window.mainloop()


def refresh_class_list(frame):
    with open("data.json", 'r') as f:
        datum = json.load(f)

    if "classes" in datum and datum['classes'] != []:
        for label in frame.winfo_children():
            label.destroy()
        classes = datum['classes']
        classes.sort()
        classes = [f"Class: {c}" for c in classes]
        for i, option in enumerate(classes):
            label = tk.Label(frame, text=f"{option}", fg="blue", cursor="hand2")
            label.grid(row=i, column=0, padx=5, pady=2)
            label.bind("<Button-1>", lambda e, opt=option: handle_class_select(opt, False))
    else:
        label = tk.Label(frame, text=f"No Class Registered yet! Click here to register!", fg="blue", cursor="hand2")
        label.grid(column=0, padx=5, pady=2)
        label.bind("<Button-1>", lambda e, opt="No Classes": handle_class_select(opt, True))


def splash_screen():
    splash_screen = tk.Tk()
    splash_screen.geometry("650x400+400+120")

    image_path = "./Assets/UCC.png"
    image = Image.open(image_path)
    image = image.resize((125, 125))
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(splash_screen, image=image_tk)
    image_label.place(x=250, y=135)

    splash_screen.overrideredirect(True)
    splash_screen.after(1500, lambda: [splash_screen.destroy()])
    splash_screen.mainloop()


def main(isBack: bool=None):
    global lFrame, mWindow

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    if isBack:
        window = mWindow
        window.geometry("650x400+400+120")
        window.iconbitmap(icon)
        window.title("Student Manager")
        window.resizable(0, 0)
        for widget in window.winfo_children():
            widget.destroy()
    else:
        window = tk.Tk()
        mWindow = window
        window.geometry("650x400+400+120")
        window.iconbitmap(icon)
        window.title("Student Manager")
        window.resizable(0, 0)

    # Load the ICON
    image_path = "./Assets/UCC.png"
    image = Image.open(image_path)
    image = image.resize((70, 70))
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=image_tk)
    image_label.place(x=60, y=1)

    # Add Texts
    name_text = tk.Label(window, text="Unique Coaching Center", font=('Arial Black', 24))
    name_text.place(x=150, y=0)
    manager_text = tk.Label(window, text="Student Management", font=('Arial Black', 13))
    manager_text.place(x=150, y=44)
    classes_text = tk.Label(window, text="Classes:", font=("./Assets/Segoe UI.ttf", 12, 'bold'))
    classes_text.place(x=5, y=107)

    # Frame for Classes
    list_frame = tk.Frame(window, highlightbackground="black", highlightthickness=0.7)
    list_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=None, expand=False, anchor=tk.S)

    canvas = tk.Canvas(list_frame, height=250, width=350)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    try:
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    except:
        pass

    canvas.create_window((0, 0), window=frame, anchor="nw")
    lFrame = frame
    refresh_class_list(frame)
    # Buttons
    add_button = tkinter.ttk.Button(window, text="New Class", style='W.TButton', command=handle_new_class)
    add_button.place(x=308, y=109)

    window.mainloop()


if __name__ == "__main__":
    splash_screen()
    main()
