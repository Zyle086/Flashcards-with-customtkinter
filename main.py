import customtkinter as ctk
from customtkinter import *
from PIL import Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


TOPIC = None
RUNNING = None

logo = CTkImage(light_image=Image.open('images/icon.png'),
                dark_image=Image.open('images/icon.png'),
                size=(200, 200))

check = CTkImage(light_image=Image.open('images/check.png'),
                 dark_image=Image.open('images/check.png'))


def center_window(window, width=650, height=500):
    window.title('Flashcards')
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y windowoordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def add_flashcards(master_window):

    subjects = ['Python', 'Javascript']

    def move_window(width=550, height=300):
        # get screen width and height
        screen_width = add_window.winfo_screenwidth()
        screen_height = add_window.winfo_screenheight()

        # calculate position x and y coordinates
        x = screen_width - width - 50
        y = (screen_height/2) - height
        add_window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def selected_sub(selected):
        global TOPIC
        TOPIC = selected

    add_window = CTkToplevel()
    add_window.geometry("550x300")
    add_window.title('Add flashcards')
    add_window.config(padx=20, pady=20)
    add_window.wm_transient(master_window)
    move_window()

    # ------ Labels

    sub_label = CTkLabel(add_window, text='Choose Topic :', font=('Arial', 15))
    sub_label.grid(column=0, row=0, padx=20, pady=20)

    add_question = CTkLabel(
        add_window, text='Add Question :', font=('Arial', 15))
    add_question.grid(column=0, row=1, padx=20, pady=20)

    add_answer = CTkLabel(add_window, text='Answer :', font=('Arial', 15))
    add_answer.grid(column=0, row=2, padx=20, pady=20)

    # ------ Entries

    question_entry = CTkEntry(
        add_window, width=200)
    question_entry.grid(column=1, row=1, padx=20, pady=20)
    question_entry.focus()

    answer_entry = CTkEntry(add_window, width=200)
    answer_entry.grid(column=1, row=2, padx=20, pady=20)

    # ------ Buttons

    add_btn = CTkButton(add_window, text='Add', width=50)
    add_btn.grid(column=2, row=2, padx=20, pady=20)

    done_btn = CTkButton(add_window, text='Done',
                         width=200, command=add_window.destroy)
    done_btn.grid(column=1, row=3, columnspan=2, padx=20, pady=20)

    add_topic = CTkButton(add_window, text='Add Topic', width=75)
    add_topic.grid(column=2, row=0, padx=20, pady=20)

    # ------ Menu

    menu = CTkOptionMenu(add_window, values=subjects,
                         width=200, command=selected_sub)
    menu.grid(column=1, row=0, padx=20, pady=20)
    menu.set('Choose Subject')

    add_window.mainloop()
    # get back to this later


def main_app():

    main_window = CTk()
    center_window(main_window, width=700)

    main_frame = CTkFrame(main_window, height=500,
                          width=550, fg_color='#222831', corner_radius=0)
    main_frame.pack(side='right')

    side_frame = CTkFrame(main_window, fg_color='#31363F',
                          border_width=2, height=500, width=170, corner_radius=0)
    side_frame.pack(side='left')

    # --------Buttons

    flashcard_btn = CTkButton(main_frame)
    flashcard_btn.grid(column=0, row=0, columnspan=3, padx=20, pady=50)

    check_btn = CTkButton(main_frame)
    check_btn.grid(column=2,  row=1, padx=20, pady=50)

    wrong_btn = CTkButton(main_frame, image=check)
    wrong_btn.grid(column=0,  row=1, padx=20, pady=50)

    skip_btn = CTkButton(main_frame, text='Skip')
    skip_btn.grid(column=1,  row=1, padx=20, pady=50)

    # -------Labels

    main_window.mainloop()


def starting_page():

    main_window = CTk()
    main_window.config(padx=50, pady=50)
    center_window(main_window)

    def end():
        main_window.destroy()
        main_window.quit()

    def launch_app():
        end()
        main_app()

    def add():
        global RUNNING
        add_running = add_flashcards(main_window)
        RUNNING = add_running

    # ------ labels

    # the icon still bad and i dont have money for photoshop lol
    icon_labels = CTkLabel(main_window, text='',  image=logo)
    icon_labels.grid(column=1, row=0, pady=50)

    # ----- buttons

    start_btn = CTkButton(main_window, text='Start', width=200,
                          height=50, corner_radius=32, fg_color='transparent',  border_color='#496989', border_width=3, command=launch_app)
    start_btn.grid(column=1, row=1, padx=10, pady=10)

    add_btn = CTkButton(main_window, text='Add Flashcards',
                        corner_radius=32, fg_color='transparent',  border_color='#496989', border_width=2, command=add)
    add_btn.grid(column=0, row=1, padx=10, pady=10)

    quit_btn = CTkButton(main_window, text='Quit',
                         corner_radius=32, fg_color='transparent',  border_color='#496989', border_width=2, command=end)
    quit_btn.grid(column=2, row=1, padx=10, pady=10)

    main_window.mainloop()


main_app()
