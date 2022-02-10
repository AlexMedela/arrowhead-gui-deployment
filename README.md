# Arrowhead GUI Deployment 
![Operative-system](https://img.shields.io/badge/OS-MacOS%2FLinux-blue)
![python-version](https://img.shields.io/badge/Python-3.8.8-blue)
![kubernetes-version](https://img.shields.io/badge/k8s-1.20.0-blueviolet)
![Terraform-version](https://img.shields.io/badge/Terraform-1.1.3-brigthgreen)

This repository contains a Graphical User Interface that automates the deployment of the Arrowhead Framework. By using this GUI you will be able to easily deploy the Arrowhead Framework on a Kubernetes cluster just following some instructions. 

The GUI offers the next options:
- Which optional services to deploy
- How many replicas of each service to deploy 
- Use a simple database or a database cluster (_feature to add own db will be implemented in the future_)
- Create a new Kubernetes cluster on the cloud, in case you don't have one (On Microsoft Azure or Google Cloud)

This few options allows you to modify the deployment architecture so it can fit for your own use case.

## Dependencies
Before trying to use the GUI you will need to fill the next requirements:

- The operative system must be MacOS or Linux
- Python 3.8 or higher with pillow package installed (recommended to use a virtual enviroment)
- Kubectl 1.21 or higher ([installation link](https://kubernetes.io/docs/tasks/tools/))
- Terraform 1.1 or higher, only if you need to create a new cluster ([installation link](https://www.terraform.io/downloads))
- Helm 3.7 or higher, only if you want to deploy the db cluster ([installation link](https://helm.sh/docs/intro/install/)) 
- The kubernetes cluster must be 1.20 or lower


## Como desplegarlo y usarlo


## Como probar la docker test network
## Como utilizar los recursos de Kubernetes (o scripts) para desplegarlo) manualmente
## Como utilizar la parte de terraform para desplegarlo manualmente
## Documentacion sobre que es cada carpeta y como funciona el codigo
Meterlo en un fichero aparte y enlazarlo
## Author
- Alex Medela - [alexm.mede98@gmail.com](mailto:alexm.mede98@gmail.com)



