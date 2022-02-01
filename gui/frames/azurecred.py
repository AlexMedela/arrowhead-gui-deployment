import tkinter as tk
import json
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
from tkinter import messagebox


class AzureCred(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image
        ah_logo = ImageTk.PhotoImage(Image.open("gui/images/arrowhead-logo.png").resize((100,100)))  

        # Labels
        logo = tk.Label(self, image=ah_logo)
        logo.photo = ah_logo
        subtitle = tk.Label(self, text="Enter Azure Service Principal Information:", font='Helvetica 18 bold')
        subid_label = tk.Label(self, text= "Subscription Id:")
        tenantid_label = tk.Label(self, text= "Tenant Id:")
        appid_label = tk.Label(self, text= "App Id:") # Or Client Id
        password_label = tk.Label(self, text= "Password:")


        # Text Input
        subid = tk.Entry(self)
        tenant = tk.Entry(self)
        appid = tk.Entry(self)
        password = tk.Entry(self, show='*')
        

        # Functions
        def continue_func():
            with open('.config/config.json', 'r') as openfile:
                config_json = json.load(openfile)

            config_json['subscription_id'] = subid.get()
            config_json['tenant_id'] = tenant.get()
            config_json['client_id'] = appid.get()
            config_json['client_secret'] = password.get()
            config_json['provider'] = 'azure'
            config_json['create_cluster'] = 'azure'
            
            with open(".config/config.json", "w") as outfile:
                json.dump(config_json, outfile)

            if not (config_json['subscription_id'] and config_json['tenant_id'] and config_json['client_id'] and config_json['client_secret']):
                messagebox.showinfo(title="Error", message="All fields must be especified")
            else:
                controller.show_frame("Deployment")
                
        # Buttons
        next_window = tk.Button(self, text='Continue', command=continue_func)
        return_button = tk.Button(self, text='Return', command=lambda: controller.show_frame("Cloud"))

        # Arrange objects
        logo.grid(row=0,column=0, padx=(20,22), pady=(20,40))
        subtitle.grid(row=0,column=1, padx=(0,190), pady=(20,40))

        subid_label.grid(row=1, columnspan=2, padx=(0,276), pady=(20,0))
        subid.grid(row=1, columnspan=2, padx=(100,0), pady=(20,0))
        tenantid_label.grid(row=2, columnspan=2, padx=(0,276), pady=(10,0))
        tenant.grid(row=2, columnspan=2, padx=(100,0), pady=(10,0))
        appid_label.grid(row=3, columnspan=2, padx=(0,276), pady=(10,0))
        appid.grid(row=3, columnspan=2, padx=(100,0), pady=(10,0))
        password_label.grid(row=4, columnspan=2, padx=(0,276), pady=(10,0))
        password.grid(row=4, columnspan=2, padx=(100,0), pady=(10,0))

        return_button.grid(row=5, column=0, padx=(0,43), pady=(100,10))
        next_window.grid(row=5, column=1, padx=(550,20), pady=(100,10))