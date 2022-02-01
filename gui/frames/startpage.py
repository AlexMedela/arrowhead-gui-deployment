import tkinter as tk
from PIL import ImageTk, Image


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image
        ah_logo = ImageTk.PhotoImage(Image.open("gui/images/arrowhead-logo.png").resize((100,100)))  

        # Labels
        logo = tk.Label(self, image=ah_logo)
        logo.photo = ah_logo
        subtitle = tk.Label(self, text="Welcome to the Arrowhead Framework deployment application", font='Helvetica 18 bold')
        description = tk.Label(self, text="Welcome to the Arrowhead Framework deployment application.")
        description2 = tk.Label(self, text="This application will let you choose between different type of deployments.")
        description3 = tk.Label(self, text="Click continue to start.")

        # Buttons
        next_window = tk.Button(self, text='Continue', command=lambda: controller.show_frame("Architecture"))
        close_app = tk.Button(self, text='Close App', command=lambda: self.master.master.destroy())

        # Arrange objects
        logo.grid(row=0,column=0, padx=(20,0), pady=20)
        subtitle.grid(row=0,column=1, padx=(10,20), pady=(20,20))
        description.grid(row=1, columnspan=2, padx=40, pady=(0,0))
        description2.grid(row=1, columnspan=2, padx=40, pady=(50,0))
        description3.grid(row=1, columnspan=2, padx=40, pady=(100,0))
        close_app.grid(row=2, column=0, padx=(10,30), pady=(180,10))
        next_window.grid(row=2, column=1, padx=(560,20), pady=(180,10))