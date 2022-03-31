# Repository structure
This document will explain the structure of the repo and the purpouse of each element.


* **.config**: This folder is a temporary file that will be created during the proccess execution to store the state of the deployment options.

* **docker**: This folder contains all the related elements to the docker container and images. Here we can find the Dockerfile for the creation of each image, and a docker compose file to test this images. This docker compose files creates an arrowhead compliance cloud using the docker network.

* **gui**: This folder contains the python code for the Graphical User Interface. Inside of this folder we can find the frames of the GUI and all the code that unifies the rest of the resources of the project automating them.

* **kubernetes**: This folder contains all the kubernetes resources already defined. Here we will find the database (the deployment and the service resources), the ingress controller (Ambassador), all the systems (deployment and service resources) and the configmaps (db init scripts and systems configuration files).

* **scripts**: This folder contains all the bash scripts to run all the resources. For example here we can find the scripts to deploy the kubernetes resources or the terraform resources. This is the intermediary between the resources and the GUI.

* **terraform**: This folder contains the terraform deployment for the Kubernetes services on Google Cloud and Azure. Each defined independently.

* **application.py**: This file is the main file of the project, executing this file will start the application to deploy the arrowhead framework. To use this file read the main readme of the repository and make sure you check the dependencies.
