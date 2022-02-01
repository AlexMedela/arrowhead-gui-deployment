#!/bin/sh

if [ $# -eq 3 ]
then
    kubectl config --kubeconfig=$2 use-context $3
fi

if [ "${1}" = "eventhandler" ]
then
    kubectl apply -f "kubernetes/ambassador/eh-mapping.yml" --kubeconfig=$2
    sleep 20
fi

if [ "${1}" = "gateway" ]
then
    kubectl apply -f "kubernetes/ambassador/gw-mapping.yml" --kubeconfig=$2
    sleep 20
fi

if [ "${1}" = "gatekeeper" ]
then
    kubectl apply -f "kubernetes/ambassador/gk-mapping.yml" --kubeconfig=$2
    sleep 20
fi
