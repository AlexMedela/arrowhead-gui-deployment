#!/bin/sh

if [ $# -eq 2 ]
then
    kubectl config --kubeconfig=$1 use-context $2
fi

kubectl apply -f "kubernetes/serviceregistry" --kubeconfig=$1
sleep 60
kubectl apply -f "kubernetes/orchestrator" --kubeconfig=$1
sleep 60
kubectl apply -f "kubernetes/authorization" --kubeconfig=$1
sleep 60