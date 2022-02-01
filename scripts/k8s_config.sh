#!/bin/sh

if [ $# -eq 3 ]
then
    kubectl config --kubeconfig=$2 use-context $3
fi

kubectl apply -f "kubernetes/configmaps/db_init.yml" --kubeconfig=$2

if [ "${1}" = "cluster" ]
then
    kubectl apply -f "kubernetes/configmaps/properties-cluster.yml" --kubeconfig=$2
fi

if [ "${1}" = "simple" ]
then
    kubectl apply -f "kubernetes/configmaps/properties-simple.yml" --kubeconfig=$2
fi


