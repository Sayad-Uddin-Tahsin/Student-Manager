import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image


def splash_screen():
    splash_screen = tk.Tk()
    splash_screen.geometry("650x400+400+120")

    image_path = "./Assets/UCC.png"
    image = Image.open(image_path)
    image = image.resize((125, 125))
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(splash_screen, image=image_tk)
    image_label.place(x=245, y=135)

    splash_screen.overrideredirect(True)
    splash_screen.after(1000, lambda: [splash_screen.destroy()])
    splash_screen.mainloop()


def main():
    def handle_list_item_click(item):
        print("List item clicked:", item)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    icon = "./assets/UCC With BG.ico"
    classes = [5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
    options = [f"Class: {c}" for c in classes]

    window = tk.Tk()
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
    image_label.place(x=100, y=1)

    # Add Texts
    name_text = tk.Label(window, text="Assistant Discord", font=('Arial Black', 24))
    name_text.place(x=185, y=1.5)
    manager_text = tk.Label(window, text="Student Management", font=('Arial Black', 12))
    manager_text.place(x=185, y=45)


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

    for i, option in enumerate(options):
        label = tk.Label(frame, text=option, fg="blue", cursor="hand2")
        label.grid(row=i, column=0, padx=5, pady=2)
        label.bind("<Button-1>", lambda e, opt=option: handle_list_item_click(opt))

    window.mainloop()


if __name__ == "__main__":
    splash_screen()
    main()