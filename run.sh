#!/bin/bash

export SETTINGS='config.DevelopmentConfig'
export ELASTICSEARCH_HOST='localhost'
export ELASTICSEARCH_PORT='9200'
export ELASTICSEARCH_USESSL=''
export ELASTICSEARCH_USERPASS=''

python run_dev.py
