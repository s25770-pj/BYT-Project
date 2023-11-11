#!/bin/bash
npm run build

sudo rm -rf /var/www/BYT-EDUPJATK/*
sudo cp -r dist/* /var/www/BYT-EDUPJATK
