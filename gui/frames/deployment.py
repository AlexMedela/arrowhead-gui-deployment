import os
import json
import tkinter as tk
from PIL import ImageTk, Image


class Deployment(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image
        ah_logo = ImageTk.PhotoImage(Image.open("gui/images/arrowhead-logo.png").resize((100,100)))  

        # Labels
        logo = tk.Label(self, image=ah_logo)
        logo.photo = ah_logo
        subtitle = tk.Label(self, text="Arrowhead Framework deployment", font='Helvetica 18 bold')

        # Text
        scroll = tk.Scrollbar(self)
        updates = tk.Text(self, height=15, width=70)
        scroll.config(command=updates.yview)
        updates.config(yscrollcommand=scroll.set)
        updates.insert(tk.END, "Press 'Deploy' button to start the deployment.\n")
        updates.configure(state='disabled')


        # Function
        def update_text(text):
            updates.configure(state='normal')
            updates.insert(tk.END,text+'\n')
            updates.configure(state='disabled')
            self.update()

        def deploy_cluster():
            deploy.config(state='disabled') # Don't allow to press the button again. Would cause problems.

            # Load configuration
            with open('.config/config.json', 'r') as openfile:
                config_json = json.load(openfile)

            if not(config_json['create_cluster']):
                kubeconfig_file = config_json['kubeconfig_path']
                if config_json['context'] != "": # Add context
                    kubeconfig_file = kubeconfig_file+f" {config_json['context']}"
            
            
            if config_json['create_cluster']:
                update_text('Starting with the cluster creation...')

                update_text('Initializing terraform...')
            
                if config_json['provider'] == 'azure':
                    update_text('Creating cluster on Azure (This can take up to 10 minutes)...')
                    os.system(f"sh scripts/terraform_azure.sh {config_json['subscription_id']} {config_json['tenant_id']} {config_json['client_id']} {config_json['client_secret']}")
                    kubeconfig_file = 'terraform/azure_terraform/kubeconfig'
                else:
                    update_text('Creating cluster on Google Cloud (This can take up to 10 minutes)...')
                    os.system(f"sh scripts/terraform_google.sh {config_json['project_id']} {config_json['region']} {config_json['google_key']}")
                    kubeconfig_file = 'terraform/google_terraform/kubeconfig'
                
                update_text('The cluster has been created.')

            


            update_text(' ')
            update_text('Starting with the deployment...')

            update_text('Adding configuration files...')
            # Add configuration files
            os.system(f"sh scripts/k8s_config.sh {kubeconfig_file}")
            update_text('Configuration files added.')

            # Deploy database
            if config_json['cluster_db']:
                update_text('Deploying database cluster...')
                os.system(f"sh scripts/k8s_cluster_db.sh {kubeconfig_file}")
                update_text('Database cluster deployed.')
            else:
                update_text('Deploying database...')
                os.system(f"sh scripts/k8s_simple_db.sh {kubeconfig_file}")
                update_text('Database deployed.')
            
            # Deploy core services
            update_text('Deploying core services...')
            os.system(f"sh scripts/k8s_core.sh {kubeconfig_file}")
            update_text('Core services deployed.')

            # Deploy optional services
            services = config_json['services']
            if services[1]==1:
                os.system(f"sh scripts/k8s_optional.sh gateway {kubeconfig_file}")
            elif services[2]==1:
                os.system(f"sh scripts/k8s_optional.sh gatekeeper {kubeconfig_file}")
            elif services[3]==1:
                os.system(f"sh scripts/k8s_optional.sh eventhandler {kubeconfig_file}")

            # Update services replicas
            replicas = config_json['replicas']
            if replicas[0]>1:
                os.system(f"sh scripts/k8s_scale.sh sr-deployment {replicas[0]} {kubeconfig_file}")
            elif replicas[1]>1:
                os.system(f"sh scripts/k8s_scale.sh orch-deployment {replicas[1]} {kubeconfig_file}")
            elif replicas[2]>1:
                os.system(f"sh scripts/k8s_scale.sh auth-deployment {replicas[2]} {kubeconfig_file}")
            elif replicas[4]>1:
                os.system(f"sh scripts/k8s_scale.sh gw-deployment {replicas[4]} {kubeconfig_file}")
            elif replicas[5]>1:
                os.system(f"sh scripts/k8s_scale.sh gk-deployment {replicas[5]} {kubeconfig_file}")
            elif replicas[6]>1:
                os.system(f"sh scripts/k8s_scale.sh eh-deployment {replicas[6]} {kubeconfig_file}")

            # Deploy ambassador
            # Ambassador
            update_text('Configuring network to expose services...')
            os.system(f"sh scripts/k8s_ambassador.sh {kubeconfig_file}")
            if services[1]==1:
                os.system(f"sh scripts/k8s_ambassador_optional.sh gateway {kubeconfig_file}")
            elif services[2]==1:
                os.system(f"sh scripts/k8s_ambassador_optional.sh gatekeeper {kubeconfig_file}")
            elif services[3]==1:
                os.system(f"sh scripts/k8s_ambassador_optional.sh eventhandler {kubeconfig_file}")
            update_text('Network configured.')


            os.system('sleep 1')
            update_text('')
            os.system('sleep 1')
            update_text('Deployment finished.')
            os.system('sleep 1')
            update_text('The ArrowHead Framework has been deployed.')

            

        # Buttons
        deploy = tk.Button(self, text='Deploy', command=deploy_cluster)
        close_app = tk.Button(self, text='Close App', command=lambda: self.master.master.destroy())

        # Arrange objects
        logo.grid(row=0,column=0, padx=(20,0), pady=20)
        subtitle.grid(row=0,column=1, padx=(10,20), pady=(20,20))
        updates.grid(row=1, columnspan=2, padx=(80,0), pady=(20,0))
        scroll.grid(row=1,columnspan=2, padx=(0,450), pady=(20,0), sticky=tk.NS)
        close_app.grid(row=2, column=0, padx=(10,30), pady=(30,10))
        deploy.grid(row=2, column=1, padx=(560,20), pady=(30,10))
