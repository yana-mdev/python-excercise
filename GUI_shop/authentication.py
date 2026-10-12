
import json
import tkinter as tk

from GUI_shop.helpers import clean_screen
from canvas import app
from products import render_products_screen


def login(username, password):
    with open("db/user_credentials_db.txt") as file:
        for line in file:
            name, pwd = line.strip().split(", ", 1)
            if name == username and pwd == password:
                with open("db/current_user.txt", "w") as f:
                    f.write(username)
                render_products_screen()
                return

    render_login_screen(error="Username or password is incorrect")


def render_login_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)

    password = tk.Entry(app, show="*")
    password.grid(row=1, column=0)

    tk.Button(
        app,
        text="Enter",
        bg="green",
        command=lambda: login(username.get(), password.get())
    ).grid(row=2, column=0)

    if error is not None:
        tk.Label(
            app,
            text=error,
            bg="red",
        ).grid(row=3, column=0)


def register(**user):
    user.update({"products": []})

    with open("db/user_credentials_db.txt", "r+", newline="\n") as file:
        users = [line.strip().split(", ", 1)[0] for line in file]

        if user["username"] in users:
            render_register_screen(error="User already exists")
            return

        file.seek(0, 2)
        file.write(f"{user['username']}, {user['password']}\n")

    with open("db/users.txt", "a", newline="\n") as f:
        f.write(json.dumps(user) + "\n")

    render_login_screen()


def render_register_screen(error=None):
    clean_screen()

    username = tk.Entry(app)
    username.grid(row=0, column=0)

    password = tk.Entry(app, show="*")
    password.grid(row=1, column=0)

    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)

    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)

    tk.Button(
        app,
        text="Register",
        bg="green",
        command=lambda: register(
            username=username.get(),
            password=password.get(),
            first_name=first_name.get(),
            last_name=last_name.get()
        )
    ).grid(row=4, column=0)

    if error is not None:
        tk.Label(
            app,
            text=error,
            bg="red",
        ).grid(row=5, column=0)


def render_main_enter_screen():
    clean_screen()

    tk.Button(
        app,
        text="Login",
        bg="green",
        command=render_login_screen
    ).grid(row=0, column=0)

    tk.Button(
        app,
        text="Register",
        bg="yellow",
        command=render_register_screen
    ).grid(row=0, column=1)
