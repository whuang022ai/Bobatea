#!/usr/bin/env bash
shopt -s expand_aliases
source ../bobatea.sh

head -n 20 testy.csv | index | curve -x Date -y Births
head -n 20 testy.csv | index | curve -x Date -y Births -s
