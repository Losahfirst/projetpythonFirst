import tkinter
from tkinter import PhotoImage

window = tkinter.Tk()
window.overrideredirect(True)  # Supprime la barre de titre et les bordures
window.title("Login-Form")  

# Dimensions de la fenêtre
win_width = 800
win_height = 550

# Calcul pour centrer la fenêtre
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (win_width // 2)
y = (screen_height // 2) - (win_height // 2)

window.geometry(f"{win_width}x{win_height}+{x}+{y}")
window.config(bg="white")
window.resizable(False, False)

canvas = tkinter.Canvas(window, width=win_width, height=win_height, highlightthickness=0, bd=0, bg="white")
canvas.pack(fill="both", expand=True)



bg = PhotoImage(file="bg.png")
canvas.create_image(0, 0, anchor="nw", image=bg)

# Déplacement de la fenêtre
def start_move(event):
    window.x = event.x_root
    window.y = event.y_root

def do_move(event):
    deltax = event.x_root - window.x
    deltay = event.y_root - window.y
    new_x = window.winfo_x() + deltax
    new_y = window.winfo_y() + deltay
    window.geometry(f"+{new_x}+{new_y}")
    window.x = event.x_root
    window.y = event.y_root

canvas.bind("<ButtonPress-1>", start_move)
canvas.bind("<B1-Motion>", do_move)

# Exemple de label centré
label_title = tkinter.Label(window, text="Gestion de Budget", font=("Arial", 24), bg="#f0f0f0", fg="black")
label_title.place(relx=0.5, y=40, anchor="center")

window.mainloop()