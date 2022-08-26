import tkinter as tk
from user import user
from PIL import ImageTk

window = tk.Tk()

username_var = tk.StringVar()
pin_var = tk.StringVar()
password_var = tk.StringVar()
message_var = tk.StringVar()
result_var = tk.StringVar()
image_num = -1
image_choice = -1
users = []

#stored variables
user_name = None
pin = None
password = None

#loading images
photo1 = ImageTk.PhotoImage(file="dog.jpg")
photo2 = ImageTk.PhotoImage(file="eagle.jpg")
photo3 = ImageTk.PhotoImage(file="gold.jpg")
photo4 = ImageTk.PhotoImage(file="lion.jpg")
photo5 = ImageTk.PhotoImage(file="parrot.jpg")
photo6 = ImageTk.PhotoImage(file="shark.jpg")
photo7 = ImageTk.PhotoImage(file="sheep.jpg")
photo8 = ImageTk.PhotoImage(file="tiger.jpg")
photo9 = ImageTk.PhotoImage(file="whale.jpg")

def search_username(username):
    global users
    user_found = -1
    for u in users:
        if u.user_name == username:
            user_found = u
            break
    return user_found

def switch_page(from_page, to_page):
    global page_dict

    page_dict[to_page].pack(fill='both', expand=1)
    page_dict[from_page].forget()

def create_login_page(f):
    global username_var
    global pin_var
    global message_var

    user_name_label = tk.Label(f, text="Enter User Name:").grid(row = 0, column = 0,padx = 10, pady = 10)
    user_name_entry = tk.Entry(f, textvariable = username_var, font=('calibre', 10, 'normal')).grid(row  = 0, column = 1,padx = 10, pady = 10)

    pin_label = tk.Label(f, text="Enter Pin:").grid(row = 1, column = 0,padx = 10, pady = 10)
    pin_entry = tk.Entry(f, textvariable = pin_var, show='*' ,font=('calibre', 10, 'normal')).grid(row = 1, column = 1,padx = 10, pady = 10)

    message_label = tk.Label(f, textvariable=message_var).grid(row = 2, column = 1)

    login_submit_button = tk.Button(f, text='Submit', command=verify_login). grid(row = 3, column = 1,padx = 10, pady = 10)
    reg_button = tk.Button(f, text='Register New User', command=lambda: switch_page(from_page=2, to_page=1)). grid(row = 4, column = 1,padx = 10, pady = 10)

def create_image_page(f):
    global image_num

    button_1 = tk.Button(f, image=photo1, command=lambda: check_image(1)).grid(row = 0, column = 0, padx = 10, pady = 10)
    button_2 = tk.Button(f, image=photo2, command=lambda: check_image(2)).grid(row = 0, column = 1, padx = 10, pady = 10)
    button_3 = tk.Button(f, image=photo3, command=lambda: check_image(3)).grid(row = 0, column = 2, padx = 10, pady = 10)
    button_4 = tk.Button(f, image=photo4, command=lambda: check_image(4)).grid(row = 1, column = 0, padx = 10, pady = 10)
    button_5 = tk.Button(f, image=photo5, command=lambda: check_image(5)).grid(row = 1, column = 1, padx = 10, pady = 10)
    button_6 = tk.Button(f, image=photo6, command=lambda: check_image(6)).grid(row = 1, column = 2, padx = 10, pady = 10)
    button_7 = tk.Button(f, image=photo7, command=lambda: check_image(7)).grid(row = 2, column = 0, padx = 10, pady = 10)
    button_8 = tk.Button(f, image=photo8, command=lambda: check_image(8)).grid(row = 2, column = 1, padx = 10, pady = 10)
    button_9 = tk.Button(f, image=photo9, command=lambda: check_image(9)).grid(row = 2, column = 2, padx = 10, pady = 10)

def create_password_page(f):
    global password_var

    password_label = tk.Label(f, text="Enter your password: ").grid(row = 0, column = 0, padx = 10, pady = 10)
    password_entry = tk.Entry(f, textvariable=password_var, show='*' ,font=('calibre', 10, 'normal')).grid(row = 0, column = 1, padx = 10, pady = 10)

    password_button = tk.Button(f, text="Check Password", command=lambda: check_password(password_var)).grid(row = 1, column = 1, padx = 10, pady = 10)

    result_label = tk.Label(f, textvariable=result_var).grid(row = 2, column = 1, padx = 10, pady = 10)

def create_reg_page(f):
    name_label = tk.Label(f, text="Enter New User Name:").grid(row = 0, column = 0, padx = 10, pady = 10)
    name_var = tk.StringVar()
    name_entry = tk.Entry(f, textvariable=name_var).grid(row = 0, column = 1, padx = 10, pady = 10)

    pin_label = tk.Label(f, text="Enter New Pin:").grid(row = 1, column = 0, padx = 10, pady = 10)
    pin_var = tk.StringVar()
    pin_entry = tk.Entry(f, textvariable=pin_var).grid(row = 1, column = 1, padx = 10, pady = 10)

    button_1 = tk.Button(f, image=photo1, command=lambda: choose_image(1)).grid(row = 2, column = 0, padx = 10, pady = 10)
    button_2 = tk.Button(f, image=photo2, command=lambda: choose_image(2)).grid(row = 2, column = 1, padx = 10, pady = 10)
    button_3 = tk.Button(f, image=photo3, command=lambda: choose_image(3)).grid(row = 2, column = 2, padx = 10, pady = 10)
    button_4 = tk.Button(f, image=photo4, command=lambda: choose_image(4)).grid(row = 3, column = 0, padx = 10, pady = 10)
    button_5 = tk.Button(f, image=photo5, command=lambda: choose_image(5)).grid(row = 3, column = 1, padx = 10, pady = 10)
    button_6 = tk.Button(f, image=photo6, command=lambda: choose_image(6)).grid(row = 3, column = 2, padx = 10, pady = 10)
    button_7 = tk.Button(f, image=photo7, command=lambda: choose_image(7)).grid(row = 4, column = 0, padx = 10, pady = 10)
    button_8 = tk.Button(f, image=photo8, command=lambda: choose_image(8)).grid(row = 4, column = 1, padx = 10, pady = 10)
    button_9 = tk.Button(f, image=photo9, command=lambda: choose_image(9)).grid(row = 4, column = 2, padx = 10, pady = 10)

    password_label = tk.Label(f, text="Enter New Password:").grid(row = 5, column = 0, padx = 10, pady = 10)
    password_var = tk.StringVar()
    password_entry = tk.Entry(f, textvariable=password_var).grid(row = 5, column = 1, padx = 10, pady = 10)

    create_user_button = tk.Button(f, text="Create User", command=lambda: create_new_user(user_name_string=name_var, user_pin_string=pin_var, user_image_choice=image_choice, user_password_string=password_var)).grid(row = 6, column = 1, padx = 10, pady = 10)

    return_to_login = tk.Button(f, text="Go to Login Page", command=lambda: switch_page(from_page=1, to_page=2)).grid(row=6,column=0,padx=10,pady=10)

def create_new_user(user_name_string, user_pin_string, user_image_choice, user_password_string):
    global users
    new_user = user(_name = user_name_string.get(), _pin = user_pin_string.get(), _image = user_image_choice,_password = user_password_string.get())
    users.append(new_user)

def choose_image(num):
    global image_choice
    image_choice = num

def check_password(password_entry):
    u = search_username(user_name)
    
    if u.user_password == password_entry.get():
        result_var.set("Login Successful!")
    else:
        result_var.set("Login Failed")

def verify_login():
    global username_var
    global user_name
    global pin_var
    global pin
    global message_var

    user_name = username_var.get()
    pin = pin_var.get()

    check = len(pin)!=6 or not(pin.isnumeric())

    if check:
        label_text = "PIN must be 6 characters long and must only contain numbers"
    else:
        res = search_username(user_name)
        if(res!=-1):
            if(res.user_pin == pin):
                message_var
                switch_page(from_page=2, to_page=3)
        else:
            label_text="User Not Found"

    message_var.set(label_text)

def check_image(image_num):
    global page_dict
    
    u = search_username(user_name)

    if u.user_image == image_num:
        switch_page(from_page=3, to_page=4)

window.title("Log-in-Page")
window.geometry("600x700")

reg_page = tk.Frame(window)
login_page = tk.Frame(window)
image_page = tk.Frame(window)
password_page = tk.Frame(window)

create_login_page(login_page)
create_image_page(image_page)
create_password_page(password_page)
create_reg_page(reg_page)

page_dict = {1: reg_page, 2:login_page, 3:image_page, 4:password_page}

login_page.pack(fill='both', expand = 1)

window.mainloop()