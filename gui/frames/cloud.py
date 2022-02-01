import tkinter as tk
from PIL import ImageTk, Image

class Cloud(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image
        ah_logo = ImageTk.PhotoImage(Image.open("gui/images/arrowhead-logo.png").resize((100,100)))  

        # Labels
        logo = tk.Label(self, image=ah_logo)
        logo.photo = ah_logo
        subtitle = tk.Label(self, text="Choose the Cloud Provider for the cluster:", font='Helvetica 18 bold')

        # Buttons
        existing_button = tk.Button(self, text='Microsoft Azure', command=lambda: controller.show_frame("AzureCred"), width=60, height=3)
        newone_button = tk.Button(self, text='Google Cloud', command=lambda: controller.show_frame("GoogleCred"), width=60, height=3)
        return_button = tk.Button(self, text='Return', command=lambda: controller.show_frame("Services"))

        # Arrange objects
        logo.grid(row=0,column=0, padx=(0,107), pady=20)
        subtitle.grid(row=0,column=1, padx=(0,90), pady=(20,20))

        existing_button.grid(row=1, columnspan=2, padx=(125,0), pady=(30,15))
        newone_button.grid(row=2, columnspan=2, padx=(125,0))

        return_button.grid(row=3, column=0, padx=(0,101), pady=(105,10))
