import tkinter as tk
import json
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
from tkinter import messagebox


class ClusterCred(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image
        ah_logo = ImageTk.PhotoImage(Image.open("gui/images/arrowhead-logo.png").resize((100,100)))  

        # Labels
        logo = tk.Label(self, image=ah_logo)
        logo.photo = ah_logo
        subtitle = tk.Label(self, text="Enter Cluster Information:", font='Helvetica 18 bold')
        kubeconfig_label = tk.Label(self, text= "Kubeconfig file:")
        context_label = tk.Label(self, text= "Specify context (if needed):")
        file_label = tk.Label(self, text=" ")

        # Text Input
        context = tk.Entry(self)

        # Functions
        def open_file():
            file_path = askopenfile(mode='r', filetypes=[('Config files', '*')])
            if file_path is not None:
                kubeconfig_path = file_path.name
                with open('.config/config.json', 'r') as openfile:
                    config_json = json.load(openfile)
                
                config_json['kubeconfig_path'] = kubeconfig_path

                with open(".config/config.json", "w") as outfile:
                    json.dump(config_json, outfile)

                file_name = file_path.name.split("/")[-1]
                file_label.config(text="File '"+file_name+"' selected")

        def continue_func():
            with open('.config/config.json', 'r') as openfile:
                config_json = json.load(openfile)

            config_json['context'] = context.get()
            
            with open(".config/config.json", "w") as outfile:
                json.dump(config_json, outfile)

            if not config_json['kubeconfig_path']:
                messagebox.showinfo(title="Error", message="Kubeconfig file must be especified")
            else:
                controller.show_frame("Deployment")
                
        # Buttons
        choose_file = tk.Button(self, text='Choose file', command=open_file)
        next_window = tk.Button(self, text='Continue', command=continue_func)
        return_button = tk.Button(self, text='Return', command=lambda: controller.show_frame("Cluster"))

        # Arrange objects
        logo.grid(row=0,column=0, padx=(20,22), pady=(20,40))
        subtitle.grid(row=0,column=1, padx=(0,190), pady=(20,40))

        kubeconfig_label.grid(row=1, columnspan=2, padx=(0,350))
        choose_file.grid(row=1, columnspan=2, padx=(0,150))
        file_label.grid(row=1, columnspan=2, padx=(200,0))
        context_label.grid(row=2, columnspan=2, padx=(0,276), pady=(20,0))
        context.grid(row=2, columnspan=2, padx=(100,0), pady=(20,0))

        return_button.grid(row=3, column=0, padx=(0,43), pady=(162,10))
        next_window.grid(row=3, column=1, padx=(550,20), pady=(162,10))