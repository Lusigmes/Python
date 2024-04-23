from customtkinter import *

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

window = CTk()
window.geometry("300x300")

def clique():
    print("LOGIN")

txt = CTkLabel(window, text="Fazer Login")
txt.pack(padx=10, pady=10)

email = CTkEntry(window, placeholder_text="Digite o e-mail")
email.pack(padx=10, pady=10)

psw = CTkEntry(window, placeholder_text="Digite a senha", show="*")
psw.pack(padx=10, pady=10)

checkbox = CTkCheckBox(window, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

btn = CTkButton(window, text="Login", command=clique)
btn.pack(padx=10, pady=10)



window.mainloop()