import tkinter as tk
from tkinter import ttk


def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find
    ttk.Label(frame, text='Find: ').grid(column=0, row=0, sticky=tk.E)
    keyword = ttk.Entry(frame, width=90)
    keyword.grid(column=1, row=0, sticky=tk.E)

    # Replace 
    ttk.Label(frame, text='Replace: ').grid(column=0, row=1, sticky=tk.E)
    replacement = ttk.Entry(frame, width=90)
    replacement.grid(column=1, row=1, sticky=tk.E)

    # Direction:
    ttk.Label(frame, text='Direction:').grid(column=1, row=2)

    #Up Radiobutton
    up_button = tk.StringVar()
    up_button_check = ttk.Radiobutton(frame,text='Up',variable=up_button,
        command=lambda: print(up_button.get()))
    up_button_check.grid(column=1, row=3, ipadx=2, ipady=2)

    #Down Radiobutton
    down_button = tk.StringVar()
    down_button_check = ttk.Radiobutton(frame,text='Down',variable=down_button,
        command=lambda: print(down_button.get()))
    down_button_check.grid(column=2, row=3, ipadx=4, ipady=2)

    # Match word checkbox
    match_word = tk.StringVar()
    match_word_check = ttk.Checkbutton(frame,variable=match_word,text='Match whole world only',
        command=lambda: print(match_word.get()))
    match_word_check.grid(column=1, row=2, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(frame,text='Match case',variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=1, row=3, sticky=tk.W)

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(frame,variable=wrap_around,text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=1, row=4, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='Replace').grid(column=0, row=1)
    ttk.Button(frame, text='Replace All').grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame


def create_main_window():

    # root window
    root = tk.Tk()
    root.title('Find & Replace')
    root.geometry('800x180')
    root.resizable(1, 1)
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', False)

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(2, weight=2)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()