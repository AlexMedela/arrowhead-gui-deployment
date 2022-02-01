#!/bin/sh

# Set kubeconfig file
export KUBECONFIG=$1

# Set kubeconfig context if especified
if [ $# -eq 2 ]
then
    export HELM_KUBECONTEXT=$2
fi

helm install mysql --set initdbScriptsConfigMap=db-init bitnami/mariadb-galera
sleep 120