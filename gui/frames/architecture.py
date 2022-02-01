import tkinter as tk
import json
from PIL import ImageTk, Image


class Architecture(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image
        ah_logo = ImageTk.PhotoImage(Image.open("gui/images/arrowhead-logo.png").resize((100,100)))  

        # Labels
        logo = tk.Label(self, image=ah_logo)
        logo.photo = ah_logo
        subtitle = tk.Label(self, text="Choose the database type:", font='Helvetica 18 bold')

        # Buttons
        high_availavility_int = tk.IntVar()
        high_availavility_button = tk.Checkbutton(self, text = "High availability database", variable=high_availavility_int)
        standard_int = tk.IntVar()
        standard_button = tk.Checkbutton(self, text = "Standard database", variable=standard_int)


        next_window = tk.Button(self, text='Continue')
        return_button = tk.Button(self, text='Return', command=lambda: controller.show_frame("StartPage"))

        # Function for buttons
        def next_window_func():
            with open('.config/config.json', 'r') as openfile:
                    config_json = json.load(openfile)
                
            config_json['cluster_db'] = high_availavility_int.get()
            
            with open(".config/config.json", "w") as outfile:
                json.dump(config_json, outfile)

            controller.show_frame("Services")

        def check_button_high():
            if high_availavility_int.get():
                standard_int.set(0)
            high_availavility_int.set(1)

        def check_button_standard():
            if standard_int.get():
                high_availavility_int.set(0)
            standard_int.set(1)
        


        next_window.config(command=next_window_func)
        high_availavility_button.config(command=check_button_high)
        standard_button.config(command=check_button_standard)


        standard_button.select()

        # Arrange objects
        logo.grid(row=0,column=0, padx=(20,0), pady=20)
        subtitle.grid(row=0,column=1, padx=(0,100), pady=(20,20))

        high_availavility_button.grid(row=2, columnspan=2, padx=40, pady=(30,5))
        standard_button.grid(row=3, columnspan=2, padx=(40, 80), pady=15)

        return_button.grid(row=5, column=0, padx=(10,30), pady=(108,10))
        next_window.grid(row=5, column=1, padx=(560,20), pady=(108,10))