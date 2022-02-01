#!/bin/sh

if [ $# -eq 4 ]
then
    kubectl config --kubeconfig=$3 use-context $4
fi

kubectl scale "deployments/${1}" --replicas=$2 --kubeconfig=$3