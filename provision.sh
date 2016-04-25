#!/usr/bin/env bash

echo "---------------------------------------------"
echo "Running vagrant bootstrap to install requirements"
echo "---------------------------------------------"

sudo apt-get update
sudo apt-get install -y git
sudo apt-get install -y python-pip
sudo pip install virtualenv

echo "---------------------------------------------"
echo " Finished."
echo "---------------------------------------------"
