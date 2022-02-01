import tkinter as tk
import json
from tkinter.constants import NSEW
from PIL import ImageTk, Image

class Services(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image
        ah_logo = ImageTk.PhotoImage(Image.open("gui/images/arrowhead-logo.png").resize((100,100)))  

        # Labels
        logo = tk.Label(self, image=ah_logo)
        logo.photo = ah_logo
        subtitle = tk.Label(self, text="Choose the deployment configuration:", font='Helvetica 18 bold')

        # Functions
        def check_db():
            db_int.set(1)

        def check_db_cluster():
            db_cluster_int.set(1)

        def check_sr():
            registry_int.set(1)

        def check_auth():
            auth_int.set(1)

        def check_orch():
            orch_int.set(1)

        def check_mngt():
            if mngt_int.get():
                mngt_replicas.config(text='1')
            else:
                mngt_replicas.config(text='0')

        def check_gw():
            if gw_int.get():
                gw_replicas.config(text='1')
            else:
                gw_replicas.config(text='0')

        def check_gk():
            if gk_int.get():
                gk_replicas.config(text='1')
            else:
                gk_replicas.config(text='0')

        def check_eventhandler():
            if eventhandler_int.get():
                eventhandler_replicas.config(text='1')
            else:
                eventhandler_replicas.config(text='0')

        def increase_replicas_registry():
            new_value = str(int(registry_replicas.cget("text"))+1)
            registry_replicas.config(text=new_value)
        
        def decrease_replicas_registry():
            new_value = int(registry_replicas.cget("text"))-1
            if new_value>=1:
                registry_replicas.config(text=str(new_value))

        def increase_replicas_auth():
            new_value = str(int(auth_replicas.cget("text"))+1)
            auth_replicas.config(text=new_value)

        def decrease_replicas_auth():
            new_value = int(auth_replicas.cget("text"))-1
            if new_value>=1:
                auth_replicas.config(text=str(new_value))

        def increase_replicas_orch():
            new_value = str(int(orch_replicas.cget("text"))+1)
            orch_replicas.config(text=new_value)

        def decrease_replicas_orch():
            new_value = int(orch_replicas.cget("text"))-1
            if new_value>=1:
                orch_replicas.config(text=str(new_value))

        def increase_replicas_mngt():
            new_value = str(int(mngt_replicas.cget("text"))+1)
            if mngt_int.get():
                mngt_replicas.config(text=new_value)

        def decrease_replicas_mngt():
            new_value = int(mngt_replicas.cget("text"))-1
            if new_value>=1:
                mngt_replicas.config(text=str(new_value))

        def increase_replicas_gw():
            new_value = str(int(gw_replicas.cget("text"))+1)
            if gw_int.get():
                gw_replicas.config(text=new_value)

        def decrease_replicas_gw():
            new_value = int(gw_replicas.cget("text"))-1
            if new_value>=1:
                gw_replicas.config(text=str(new_value))
    
        def increase_replicas_gk():
            new_value = str(int(gk_replicas.cget("text"))+1)
            if gk_int.get():
                gk_replicas.config(text=new_value)

        def decrease_replicas_gk():
            new_value = int(gk_replicas.cget("text"))-1
            if new_value>=1:
                gk_replicas.config(text=str(new_value))

        def increase_replicas_eventhandler():
            new_value = str(int(eventhandler_replicas.cget("text"))+1)
            if eventhandler_int.get():
                eventhandler_replicas.config(text=new_value)
        
        def decrease_replicas_eventhandler():
            new_value = int(eventhandler_replicas.cget("text"))-1
            if new_value>=1:
                eventhandler_replicas.config(text=str(new_value))

        def increase_replicas_db_cluster():
            new_value = str(int(db_cluster_replicas.cget("text"))+1)
            if db_cluster_int.get():
                db_cluster_replicas.config(text=new_value)
        
        def decrease_replicas_db_cluster():
            new_value = int(db_cluster_replicas.cget("text"))-1
            if new_value>=3:
                db_cluster_replicas.config(text=str(new_value))

        def next_window_func():
            with open('.config/config.json', 'r') as openfile:
                    config_json = json.load(openfile)

            config_json['services'] = [mngt_int.get(),gw_int.get(),gk_int.get(),eventhandler_int.get()]
            config_json['replicas'] = [int(registry_replicas.cget("text")),int(orch_replicas.cget("text")),int(auth_replicas.cget("text")), int(mngt_replicas.cget("text")), int(gw_replicas.cget("text")), int(gk_replicas.cget("text")), int(eventhandler_replicas.cget("text"))]

            with open(".config/config.json", "w") as outfile:
                json.dump(config_json, outfile)

            controller.show_frame("Cluster")

        # Buttons
        db_int = tk.IntVar()
        db_button = tk.Checkbutton(self, text = "Simple database (Mandatory)", variable=db_int, command=check_db)
        db_cluster_int = tk.IntVar()
        db_cluster_button = tk.Checkbutton(self, text = "Database cluster (Mandatory)", variable=db_cluster_int, command=check_db_cluster)
        registry_int = tk.IntVar()
        registry_button = tk.Checkbutton(self, text = "Service Registry (Mandatory)", variable=registry_int, command=check_sr)
        auth_int = tk.IntVar()
        auth_button = tk.Checkbutton(self, text = "Authorization (Mandatory)", variable=auth_int, command=check_auth)
        orch_int = tk.IntVar()
        orch_button = tk.Checkbutton(self, text = "Orchestrator (Mandatory)", variable=orch_int, command=check_orch)
        mngt_int = tk.IntVar()
        mngt_button = tk.Checkbutton(self, text = "Management Tool (Available soon)", variable=mngt_int, command=check_mngt)
        gw_int = tk.IntVar()
        gw_button = tk.Checkbutton(self, text = "Gateway", variable=gw_int, command=check_gw)
        gk_int = tk.IntVar()
        gk_button = tk.Checkbutton(self, text = "Gatekeeper", variable=gk_int, command=check_gk)
        eventhandler_int = tk.IntVar()
        eventhandler_button = tk.Checkbutton(self, text = "EventHandler", variable=eventhandler_int, command=check_eventhandler)

        registry_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_registry)
        registry_replicas = tk.Label(self, text= '2')
        registry_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_registry)

        auth_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_auth)
        auth_replicas = tk.Label(self, text= '2')
        auth_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_auth)

        orch_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_orch)
        orch_replicas = tk.Label(self, text= '2')
        orch_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_orch)

        mngt_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_mngt)
        mngt_replicas = tk.Label(self, text= '0')
        mngt_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_mngt)

        gw_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_gw)
        gw_replicas = tk.Label(self, text= '0')
        gw_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_gw)

        gk_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_gk)
        gk_replicas = tk.Label(self, text= '0')
        gk_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_gk)

        eventhandler_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_eventhandler)
        eventhandler_replicas = tk.Label(self, text= '0')
        eventhandler_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_eventhandler)

        db_replicas = tk.Label(self, text= '1')

        db_cluster_replicas_minus_button = tk.Button(self, text='-', command=decrease_replicas_db_cluster)
        db_cluster_replicas = tk.Label(self, text= '3')
        db_cluster_replicas_plus_button = tk.Button(self, text='+', command=increase_replicas_db_cluster)
        

        registry_button.select()
        auth_button.select()
        orch_button.select()
        #mngt_button.select()
        mngt_button.config(state='disabled')
        mngt_replicas_minus_button.config(state='disabled')
        mngt_replicas_plus_button.config(state='disabled')

        next_window = tk.Button(self, text='Continue', command=next_window_func)
        return_button = tk.Button(self, text='Return', command=lambda: controller.show_frame("Architecture"))

        # Arrange objects
        logo.grid(row=0,column=0, padx=(20,0), pady=20)
        subtitle.grid(row=0,column=1, padx=(0,100), pady=(20,20))

        registry_button.grid(row=2, columnspan=2, padx=(0,158))
        registry_replicas_minus_button.grid(row=2, columnspan=2, padx=(250,0))
        registry_replicas.grid(row=2, columnspan=2, padx=(300,0))
        registry_replicas_plus_button.grid(row=2, columnspan=2, padx=(350,0))

        auth_button.grid(row=3, columnspan=2, padx=(0,177))
        auth_replicas_minus_button.grid(row=3, columnspan=2, padx=(250,0))
        auth_replicas.grid(row=3, columnspan=2, padx=(300,0))
        auth_replicas_plus_button.grid(row=3, columnspan=2, padx=(350,0))

        orch_button.grid(row=4, columnspan=2, padx=(0,180))
        orch_replicas_minus_button.grid(row=4, columnspan=2, padx=(250,0))
        orch_replicas.grid(row=4, columnspan=2, padx=(300,0))
        orch_replicas_plus_button.grid(row=4, columnspan=2, padx=(350,0))

        mngt_button.grid(row=5, columnspan=2, padx=(0,122))
        mngt_replicas_minus_button.grid(row=5, columnspan=2, padx=(250,0))
        mngt_replicas.grid(row=5, columnspan=2, padx=(300,0))
        mngt_replicas_plus_button.grid(row=5, columnspan=2, padx=(350,0))

        gw_button.grid(row=6, columnspan=2, padx=(0,283))
        gw_replicas_minus_button.grid(row=6, columnspan=2, padx=(250,0))
        gw_replicas.grid(row=6, columnspan=2, padx=(300,0))
        gw_replicas_plus_button.grid(row=6, columnspan=2, padx=(350,0))

        gk_button.grid(row=7, columnspan=2, padx=(0,265))
        gk_replicas_minus_button.grid(row=7, columnspan=2, padx=(250,0))
        gk_replicas.grid(row=7, columnspan=2, padx=(300,0))
        gk_replicas_plus_button.grid(row=7, columnspan=2, padx=(350,0))

        eventhandler_button.grid(row=8, columnspan=2, padx=(0,255))
        eventhandler_replicas_minus_button.grid(row=8, columnspan=2, padx=(250,0))
        eventhandler_replicas.grid(row=8, columnspan=2, padx=(300,0))
        eventhandler_replicas_plus_button.grid(row=8, columnspan=2, padx=(350,0))

        return_button.grid(row=9, column=0, padx=(10,30), pady=(94,10))
        next_window.grid(row=9, column=1, padx=(560,20), pady=(94,10))