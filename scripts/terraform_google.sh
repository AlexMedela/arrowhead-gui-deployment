#!/bin/sh

cd terraform/google_terraform
terraform init
terraform apply -var="project_id=${1}" -var="region=${2}" -var="credentials=${3}" -auto-approve
