#!/usr/bin/env bash

tmp=$ENV_FOR_DYNACONF

function reset_env(){
    if [[ -z $tmp ]]; then
        unset ENV_FOR_DYNACONF
    else
        export ENV_FOR_DYNACONF="$tmp"
    fi
}

trap reset_env INT

export ENV_FOR_DYNACONF="testing"
python -m pytest "$1" --cov=src --cov-report=html

reset_env
