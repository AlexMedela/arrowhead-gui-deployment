#!/bin/sh

if [ $# -eq 2 ]
then
    kubectl config --kubeconfig=$1 use-context $2
fi

kubectl apply -f "kubernetes/configmaps/" --kubeconfig=$1
