import os
import datetime
import json
import tkinter as tk
import tkinter.ttk
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    mWindow: tk.Tk

icon = "./assets/UCC With BG.ico"
lFrame = None
mWindow = None
FContactOverwritten: bool = False
MContactOverwritten: bool = False


def isDBExists():
    # Define the root directory
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Define the path to the file you want to check
    file_path = os.path.join(ROOT_DIR, 'file_name')

    # Check if the file exists
    file_exists = os.path.exists(file_path)
    return file_exists


if not isDBExists():
    with open('data.json', 'w') as file:
        file.write('{\n    "classes": []\n}')


def assign_new_student(_class):
    global FContactOverwritten, MContactOverwritten
    FContactOverwritten = False
    MContactOverwritten = False

    def handle_id_lock():
        state = ID_Entey.cget("state")
        if state == "normal":
            ID_Entey.configure(state=tk.DISABLED)
            lock_button.configure(text="🔓")
        elif state == 'disabled':
            ID_Entey.configure(state=tk.NORMAL)
            lock_button.configure(text="🔒")

    def validate_Fcontact_entry(text):
        global FContactOverwritten

        if text.isdigit() or text != "":
            if text != "0" and not str(text).startswith("0"):
                x, y = FContactPrefix_Entey.winfo_x(), FContactPrefix_Entey.winfo_y()
                FContact_error.configure(text="* Number must start with 0!",
                                         font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
                                         fg='red')
                FContact_error.place(x=x, y=y + 19)
                return False
            elif len(text) <= 11:
                x, y = FContactPrefix_Entey.winfo_x(), FContactPrefix_Entey.winfo_y()
                FContact_error.configure(text="* Number must be 11 in length!", font=("./Assets/Segoe_UI.ttf", 8, 'italic'), fg='red')
                FContact_error.place(x=x, y=y + 19)
                FContactOverwritten = False
                if len(text) == 11:
                    FContact_error.configure(text="")
                    FContact_error.place(x=36000, y=10000)
                    return True
                return True
            else:
                return False
        else:
            x, y = FContactPrefix_Entey.winfo_x(), FContactPrefix_Entey.winfo_y()
            if text == "":
                FContact_error.configure(text=" ", font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
                                         fg='red')
                FContact_error.place(x=x, y=y + 19)
                return True
            else:
                FContact_error.configure(text="* Number must be integer!", font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
                                         fg='red')
                FContact_error.place(x=x, y=y + 19)
                return False

    def validate_Mcontact_entry(text):
        global MContactOverwritten

        if text.isdigit() or text != "":
            if str(MContact_Entey.get()) == "" and str(text) != "0":
                x, y = MContactPrefix_Entey.winfo_x(), MContactPrefix_Entey.winfo_y()
                MContact_error.configure(text="* Number must start with 0!", font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
                                         fg='red')
                MContact_error.place(x=x, y=y + 19)
                return False
            elif len(text) <= 11:
                x, y = MContactPrefix_Entey.winfo_x(), MContactPrefix_Entey.winfo_y()
                MContact_error.configure(text="* Number must be 11 in length!", font=("./Assets/Segoe_UI.ttf", 8, 'italic'), fg='red')
                MContact_error.place(x=x, y=y + 19)
                MContactOverwritten = False
                if len(text) == 11:
                    MContact_error.configure(text="")
                    MContact_error.place(x=36000, y=10000)
                    return True
                return True
            else:
                return False
        else:
            x, y = MContactPrefix_Entey.winfo_x(), MContactPrefix_Entey.winfo_y()
            if text == "":
                MContact_error.configure(text=" ", font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
                                         fg='red')
                MContact_error.place(x=x, y=y + 19)
                return True
            else:
                MContact_error.configure(text="* Number must be integer!", font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
                                         fg='red')
                MContact_error.place(x=x, y=y + 19)
                return False

    def toggle_check():
        if check_var.get() == 0:
            check_var.set(1)
            check_label.config(text="✔ | Same")
            PermanentAddress_text_box.configure(state=tk.DISABLED, bg="light gray")

        else:
            check_var.set(0)
            check_label.config(text="   | Same")
            PermanentAddress_text_box.configure(state=tk.NORMAL, bg="white")

    def save():
        global FContactOverwritten, MContactOverwritten

        e = False

        def overwrite(obj, x, y, fom):
            global FContactOverwritten, MContactOverwritten

            if TYPE_CHECKING:
                obj: tk.Label

            obj.configure(text="", fg="black", cursor="arrow")
            obj.place(x=x, y=y)
            if fom == "F":
                FContactOverwritten = True
            elif fom == "M":
                MContactOverwritten = True

        if Name1_Entey.get() == "":
            Name1_text.configure(fg='red')
            e = True
        else:
            Name1_text.configure(fg='black')
        if Name2_Entey.get() == "":
            Name2_text.configure(fg='red')
            e = True
        else:
            Name2_text.configure(fg='black')

        if FatherName_Entey.get() == "":
            FatherName_text.configure(fg='red')
            e = True
        else:
            FatherName_text.configure(fg='black')
        if MotherName_Entey.get() == "":
            MotherName_text.configure(fg='red')
            e = True
        else:
            MotherName_text.configure(fg='black')

        if FContact_Entey.get() == "" and FContactOverwritten is False:
            FContact_error.configure(text="Overwrite and skip contact!", fg="blue", cursor="hand2", font=("./Assets/Segoe_UI.ttf", 8, 'underline'))
            x, y = FContactPrefix_Entey.winfo_x(), FContactPrefix_Entey.winfo_y()
            FContact_error.place(x=x + 14, y=y + 19)
            FContact_error.bind("<Button-1>", lambda e, obj=FContact_error, x=x+14, y =y+19: overwrite(obj, x, y, "F"))
        else:
            FContact_text.configure(fg='black')
            x, y = FContactPrefix_Entey.winfo_x(), FContactPrefix_Entey.winfo_y()
            FContact_error.configure(text="", fg="black", cursor="arrow")
            FContact_error.place(x=x + 14, y=y + 19)

        if MContact_Entey.get() == "" and MContactOverwritten is False:
            MContact_error.configure(text="Overwrite and skip contact!", fg="blue", cursor="hand2", font=("./Assets/Segoe_UI.ttf", 8, 'underline'))
            x, y = MContactPrefix_Entey.winfo_x(), MContactPrefix_Entey.winfo_y()
            MContact_error.place(x=x + 14, y=y + 19)
            MContact_error.bind("<Button-1>", lambda e, obj=MContact_error, x=x+14, y =y+19: overwrite(obj, x, y, "M"))
        else:
            MContact_text.configure(fg='black')
            x, y = MContactPrefix_Entey.winfo_x(), MContactPrefix_Entey.winfo_y()
            MContact_error.configure(text="", fg="black", cursor="arrow")
            MContact_error.place(x=x + 14, y=y + 19)

        if e is False and (FContactOverwritten or FContact_Entey.get() != "") and (MContactOverwritten or MContact_Entey.get() != ""):
            with open("data.json", 'r') as f:
                data = json.load(f)
                
            if _class in data:
                data[_class][str(ID_Entey.get())] = {}
            else:
                data[_class] = {}
                data[_class][str(ID_Entey.get())] = {}
            data[_class][str(ID_Entey.get())]["First Name"] = Name1_Entey.get()
            data[_class][str(ID_Entey.get())]["Last Name"] = Name2_Entey.get()
            data[_class][str(ID_Entey.get())]["Father"] = {
                "Name": FatherName_Entey.get(),
                "Contact": "Not Provided!" if FContact_Entey.get() == "" else FContact_Entey.get()
            }
            data[_class][str(ID_Entey.get())]["Mother"] = {
                "Name": MotherName_Entey.get(),
                "Contact": "Not Provided!" if MContact_Entey.get() == "" else MContact_Entey.get()
            }
            data[_class][str(ID_Entey.get())]["Address"] = {
                "Current": CurrentAddress_text_box.get("1.0", "end-1c"),
                "Permanent": PermanentAddress_text_box.get("1.0", "end-1c") if check_var.get() == 0 else CurrentAddress_text_box.get("1.0", "end-1c")
            }
            data[_class][str(ID_Entey.get())]["status"] = "stable"

            with open("data.json", 'w') as f:
                json.dump(data, f, indent=4)

            window.update()
            for widget in window.winfo_children():
                widget.configure(state=tk.DISABLED)
            save_error.configure(text="Saved!", fg="green")
            save_error.place(x=window.winfo_width() - (save_error.winfo_reqwidth() + 15), y=save_button.winfo_y() - 20)
            save_error.configure(state=tk.NORMAL)
            back_button.configure(state=tk.NORMAL)
            save_button.configure(state=tk.NORMAL, text="Go Back", command=lambda cls=_class: handle_class_select(cls, False))

        else:
            window.update()
            save_error.configure(text="Please fill up all the required fields or Overwrite!", fg="red")
            save_error.place(x=window.winfo_width() - (save_error.winfo_reqwidth() + 10), y=save_button.winfo_y() - 20)
            return


    window = mWindow
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
    ID_text = tk.Label(window, text="ID:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    ID_text.place(x=10, y=12)
    ID_Entey.insert(tk.END, f"{datetime.datetime.today().strftime('%y')}{_class.replace('Class: ', '')}B{'01' if str(_class) not in classDB else '0' + str(len(classDB[_class]) + 1) if len(str(len(classDB[_class]))) == 1 else len(classDB[_class])}")
    ID_Entey.configure(state=tk.DISABLED)
    lock_button = tkinter.ttk.Button(window, text="🔓", style='W.TButton', command=handle_id_lock, width=3)
    lock_button.place(x=170, y=13)

    Name1_Entey = tk.Entry(window, width=35)
    Name1_Entey.place(x=105, y=45)
    Name1_text = tk.Label(window, text="First Name:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    Name1_text.place(x=10, y=42)
    Name2_Entey = tk.Entry(window, width=20)
    Name2_Entey.place(x=455, y=45)
    Name2_text = tk.Label(window, text="Last Name:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    Name2_text.place(x=360, y=42)

    FatherName_Entey = tk.Entry(window, width=35)
    FatherName_Entey.place(x=130, y=80)
    FatherName_text = tk.Label(window, text="Father's Name:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    FatherName_text.place(x=10, y=76)
    FContactPrefix_Entey = tk.Entry(window, width=4)
    FContactPrefix_Entey.place(x=435, y=80)
    FContactPrefix_Entey.insert(0, " +88")
    FContactPrefix_Entey.configure(state=tk.DISABLED)
    FContact_Entey = tk.Entry(window, width=20)
    FContact_Entey.place(x=462, y=80)
    FContact_text = tk.Label(window, text="Contact:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    FContact_text.place(x=360, y=77)
    validate_cmd = window.register(validate_Fcontact_entry)
    FContact_Entey.config(validate="key", validatecommand=(validate_cmd, "%P"))
    FContact_error = tk.Label(window, text="")
    FContact_error.place(x=1000, y=1000)

    MotherName_Entey = tk.Entry(window, width=35)
    MotherName_Entey.place(x=130, y=120)
    MotherName_text = tk.Label(window, text="Mother's Name:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    MotherName_text.place(x=10, y=117)
    MContactPrefix_Entey = tk.Entry(window, width=4)
    MContactPrefix_Entey.place(x=435, y=120)
    MContactPrefix_Entey.insert(0, " +88")
    MContactPrefix_Entey.configure(state=tk.DISABLED)
    MContact_Entey = tk.Entry(window, width=20)
    MContact_Entey.place(x=462, y=120)
    MContact_text = tk.Label(window, text="Contact:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    MContact_text.place(x=360, y=117)
    Mvalidate_cmd = window.register(validate_Mcontact_entry)
    MContact_Entey.config(validate="key", validatecommand=(Mvalidate_cmd, "%P"))
    MContact_error = tk.Label(window, text="")
    MContact_error.place(x=1000, y=1000)

    CurrentAddress_text = tk.Label(window, text="Current Address:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    CurrentAddress_text.place(x=10, y=160)
    CurrentAddress_text_box = tk.Text(window, height=5, width=40, font=("./Assets/Segoe_UI.ttf", 9))
    CurrentAddress_text_box.place(x=14, y=185)
    PermanentAddress_text = tk.Label(window, text="Permanent Address:", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    PermanentAddress_text.place(x=345, y=160)
    PermanentAddress_text_box = tk.Text(window, height=5, width=40, font=("./Assets/Segoe_UI.ttf", 9))
    PermanentAddress_text_box.place(x=349, y=185)
    check_var = tk.IntVar()
    check_label = tk.Label(window, text="   | Same", width=7, height=1, relief="solid",
                           highlightthickness=1, bd=1)
    check_label.bind("<Button-1>", lambda e: toggle_check())
    check_label.place(x=349, y=267)

    save_button = tkinter.ttk.Button(window, text="Save & Assign", style='W.TButton', command=save)
    save_button.place(x=555, y=370)
    save_error = tk.Label(window, text="", font=("./Assets/Segoe_UI.ttf", 9, 'italic'), fg='red')
    window.update()
    save_error.place(x=window.winfo_width() - (save_error.winfo_reqwidth() + 10), y=save_button.winfo_y() - 20)

    window.mainloop()


def handle_class_select(item, sendToNewClass):
    def search_items(event):
        search_text = search_entry.get()
        matching_items = []

        for item in students:
            if search_text.lower() in item[0].lower() or search_text.lower() in item[1].lower():
                matching_items.append(item)

        students_treeview.delete(*students_treeview.get_children())

        if matching_items:
            for item in matching_items:
                students_treeview.insert("", tk.END, values=item)
        else:
            students_treeview.insert("", tk.END, values=("", "No match found",))


    if sendToNewClass:
        return handle_new_class()

    with open("data.json", 'r') as f:
        db = json.load(f)

    if item in db:
        students = []
        classDB = db[item]
        for id in classDB:
            if classDB[id]['status'] == 'stable':
                students.append(
                    (id, f"{classDB[id]['First Name']} {classDB[id]['Last Name']}")
                )
    else:
        students = []

    window = mWindow

    def _on_mousewheel(event):
        students_treeview.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def handle_student_click(event):
        selected_item = students_treeview.focus()
        if selected_item:
            student_info = students_treeview.item(selected_item, "values")
            print("Selected student information:", student_info)

    def handle_student_delete_click(event):
        # Get the clicked item
        clicked_item = students_treeview.identify("item", event.x, event.y)

        # Skip if the clicked item is a column heading
        if clicked_item in students_treeview['columns']:
            return

        # Get the selected item
        selected_item = students_treeview.selection()
        if selected_item:
            delete_button.configure(state="normal")
        else:
            delete_button.configure(state="disabled")

    def clear_selection(event):
        selected_item = students_treeview.selection()
        if not selected_item:
            return
        x, y, _, _ = students_treeview.bbox(selected_item)
        if event.x < x or event.x > x + students_treeview.winfo_width() or event.y < y or event.y > y + students_treeview.winfo_height():
            students_treeview.selection_remove(selected_item)
            delete_button.configure(state="disabled")

    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("650x400+400+120")
    window.iconbitmap(icon)
    window.title(f"Viewing {item}")
    window.resizable(0, 0)

    students_treeview = tkinter.ttk.Treeview(window, columns=("id", "name"), show="headings", height=13)
    students_treeview.place(x=15, y=105, fill=None)

    students_treeview.column("id", width=200)
    students_treeview.column("name", width=400)
    students_treeview.heading("id", text="ID")
    students_treeview.heading("name", text="Name")

    def handle_delete():
        selected_item = students_treeview.focus()
        if selected_item:
            item_values = students_treeview.item(selected_item, "values")
            id, name = item_values
            with open("data.json", 'r') as f:
                data = json.load(f)
            data[item][id]['status'] = 'removed'
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            students_treeview.delete(selected_item)
            students.remove(item_values)

        if students_treeview.selection():
            delete_button.configure(state="normal")
        else:
            delete_button.configure(state="disabled")

    students_treeview.bind("<ButtonRelease-1>", handle_student_delete_click)

    window.bind("<ButtonRelease-1>", clear_selection)

    scrollbar = tkinter.ttk.Scrollbar(window, orient="vertical", command=students_treeview.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    students_treeview.configure(yscrollcommand=scrollbar.set)
    window.bind_all("<MouseWheel>", _on_mousewheel)

    for student in students:
        students_treeview.insert("", tk.END, values=student)

    students_treeview.bind("<Double-1>", handle_student_click)

    search_entry = tk.Entry(window, width=50)
    search_entry.place(x=15, y=85)
    search_entry.bind("<KeyRelease>", search_items)

    with open("data.json", 'r') as f:
        datum = json.load(f)

    class_text = tk.Label(window, text=item, font=("./Assets/Segoe_UI.ttf", 16, 'bold'))
    class_text.place(x=10, y=10)
    total_students = tk.Label(window, text=f"Total Students: {0 if item not in datum else len(datum[item])}", font=("./Assets/Segoe_UI.ttf", 9, 'bold'))
    total_students.place(x=12, y=48)

    add_button = tkinter.ttk.Button(window, text="Assign New Student", style='W.TButton', command=lambda cls=item: assign_new_student(cls))
    add_button.place(x=503, y=45)
    delete_button = tkinter.ttk.Button(window, text="Delete", style='W.TButton', command=handle_delete,
                                       state="disabled")
    delete_button.place(x=420, y=45)

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
        text = entry.get()

        if text == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def handle_focus_out(event):
        text = entry.get()

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
                    error.config(text="")
                    save_button.place(y=52)
                    error.config(text=f"* Class {int(text)} already exists!",
                                 font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
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
            error.config(text="* Class must be a number! Ex. 9", font=("./Assets/Segoe_UI.ttf", 8, 'italic'),
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

    classes_text = tk.Label(window, text="Enter the Class", font=("./Assets/Segoe_UI.ttf", 11, 'bold'))
    classes_text.place(x=5, y=5)
    error = tk.Label(window, text="")
    error.place(x=5, y=45)

    error_label = tk.Label(window, fg="red")
    error_label.place(x=10000, y=10000)

    placeholder = "Enter class here. Ex. 9"

    entry = tk.Entry(window, width=30, fg="gray")
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", handle_focus_in)
    entry.bind("<FocusOut>", handle_focus_out)
    entry.bind("<Return>", handle_class_entry_event)
    entry.place(x=8, y=30)

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

    image_path = "./Assets/UCC 125x125.png"
    img = tk.PhotoImage(file=image_path)
    img_label = tk.Label(splash_screen, image=img)
    img_label.place(x=250, y=135)

    splash_screen.overrideredirect(True)
    splash_screen.after(1500, lambda: [splash_screen.destroy()])
    splash_screen.mainloop()


def main(isBack: bool=None):
    global lFrame, mWindow

    def _on_mousewheel(event):
        canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def _on_canvas_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

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

    image_path = "./Assets/UCC 70x70.png"
    image_label = tk.Label(window)
    img = tk.PhotoImage(file=image_path)
    image_label.configure(image=img)
    image_label.image = img
    image_label.place(x=60, y=1)

    name_text = tk.Label(window, text="Unique Coaching Center", font=('Arial Black', 24))
    name_text.place(x=150, y=0)
    manager_text = tk.Label(window, text="Student Management", font=('Arial Black', 13))
    manager_text.place(x=150, y=44)
    classes_text = tk.Label(window, text="Classes:", font=("./Assets/Segoe_UI.ttf", 12, 'bold'))
    classes_text.place(x=5, y=107)

    list_frame = tk.Frame(window, highlightbackground="black", highlightthickness=0.7)
    list_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=None, expand=False, anchor=tk.S)

    canvas = tk.Canvas(list_frame, height=250, width=350)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    canvas.bind("<Configure>", _on_canvas_configure)

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    canvas.create_window((0, 0), window=frame, anchor="nw")
    lFrame = frame
    refresh_class_list(frame)
    add_button = tkinter.ttk.Button(window, text="New Class", style='W.TButton', command=handle_new_class)
    add_button.place(x=308, y=109)

    window.mainloop()


if __name__ == "__main__":
    splash_screen()
    main()
