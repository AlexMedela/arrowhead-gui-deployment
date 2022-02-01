#!/bin/sh

cd terraform/azure_terraform
terraform init
terraform apply -var="subscription_id=${1}" -var="tenant_id=${2}" -var="client_id=${3}" -var="client_secret=${4}" -auto-approve
terraform output -raw kube_config > kubeconfig