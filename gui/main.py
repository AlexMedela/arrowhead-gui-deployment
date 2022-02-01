import tkinter as tk
import json

from gui.frames.architecture import Architecture
from gui.frames.azurecred import AzureCred
from gui.frames.cloud import Cloud
from gui.frames.cluster import Cluster
from gui.frames.clustercred import ClusterCred
from gui.frames.deployment import Deployment
from gui.frames.googlecred import GoogleCred
from gui.frames.services import Services
from gui.frames.startpage import StartPage


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("ArrowHead Framework Deployment")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        default_config = {
            "cluster_db": 0,
            "services": [0,0,0,0],
            "replicas": [1,1,1,0,0,0,0],
            "kubeconfig_path": None,
            "context": None,
            "create_cluster": None,
            "google_key": None,
            "project_id": None,
            "subscription_id": None,
            "tenant_id": None,
            "client_id": None,
            "client_secret": None
        }
        with open(".config/config.json", "w+") as outfile:
            json.dump(default_config, outfile)

        self.frames = {}
        for F in (StartPage, Architecture, Services, Cluster, GoogleCred, Cloud, Deployment, ClusterCred, AzureCred):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
