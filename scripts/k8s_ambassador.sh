#!/bin/sh

if [ $# -eq 2 ]
then
    kubectl config --kubeconfig=$1 use-context $2
fi

kubectl apply -f "kubernetes/ambassador/aes-crds.yaml" --kubeconfig=$1
sleep 20
kubectl apply -f "kubernetes/ambassador/aes.yaml" --kubeconfig=$1
sleep 20
kubectl apply -f "kubernetes/ambassador/core-mapping.yml" --kubeconfig=$1