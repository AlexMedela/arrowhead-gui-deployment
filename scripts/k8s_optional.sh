#!/bin/sh

if [ $# -eq 3 ]
then
    kubectl config --kubeconfig=$2 use-context $3
fi

if [ "${1}" = "eventhandler" ]
then
    kubectl apply -f "kubernetes/eventhandler" --kubeconfig=$2
    sleep 60
fi

if [ "${1}" = "gateway" ]
then
    kubectl apply -f "kubernetes/gateway" --kubeconfig=$2
    sleep 60
fi

if [ "${1}" = "gatekeeper" ]
then
    kubectl apply -f "kubernetes/gatekeeper" --kubeconfig=$2
    sleep 60
fi
