# Arrowhead GUI Deployment 
![Operative-system](https://img.shields.io/badge/OS-MacOS%2FLinux-blue)
![python-version](https://img.shields.io/badge/Python-3.8.8-blue)
![kubernetes-version](https://img.shields.io/badge/k8s-1.20.0-blueviolet)
![Terraform-version](https://img.shields.io/badge/Terraform-1.1.3-brigthgreen)
![kubectl-version](https://img.shields.io/badge/kubectl-1.21.2-blueviolet)
![Terraform-version](https://img.shields.io/badge/Helm-3.7.1-green)

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
- Python 3.8 or higher with pillow package installed (recommended to use a virtual environment)
- Kubectl 1.21 or higher ([Installation link](https://kubernetes.io/docs/tasks/tools/))
- Terraform 1.1 or higher, only if you need to create a new cluster ([Installation link](https://www.terraform.io/downloads))
- Helm 3.7 or higher, only if you want to deploy the db cluster ([Installation link](https://helm.sh/docs/intro/install/)) 
- The kubernetes cluster must be 1.20 or lower


## Running the GUI
To use the GUI you only need to run the application.py file. You can do so by running the next command on the root directoty of the repository:

``` 
python application.py
```

Now that you have the GUI running just follow the instructions.

## Running the docker test network
This repository contains a docker-compose file with all the containers used for the deployment. So if you want to run the arrowhead framework on docker to test it you can run the docker compose file on _docker/0_docker_compose_test_. If you want to make any changes to the configuration you can alse check the files on the folder _docker/0_docker_compose_test/core_system_config_.

You can also find the Dockerfiles used to create the images on the docker folder.

## Running the k8s resources
In case you want to deploy the cluster manually or make any changes you can use the kubernetes resources defined in the _kubernetes/_ folder.

And if you don't know how to use those resources you can also use the scripts found in the _scripts/_ folder. In this folder you will find different scripts to deploy individualy each resource.

On the other hand, the scripts to create the clusters on Azure and GCloud won't work.
 
## Creating cloud k8s clusters manually
In the case you want to create the cluster you will need to go to the corresponding folder depending if you want to deploy it on Azure (_terraform/azure_terraform_) or Gcloud (_terraform/google_terraform_). Inside this folders you will need to run the following commands:

``` 
terraform init
terraform apply -auto-aprove
```

After the second command you will be asked for the credentials and it will start creating the cluster.

## Additional information
Additional information can be found in the docs folder.

* [Repostory structure explained](docs/repo_structure.md)
* [Project development documentation](docs/) (Master Thesis)

## Author
- Alexander Medela - [alexm.mede98@gmail.com](mailto:alexm.mede98@gmail.com)



