#!/bin/bash

#DATE=$(date +"%Y-%m-%d_%H%M%S")
#FILENAME="image_$DATE.jpg"
FILENAME="snapshot_image.jpg"
EMAILADDR=$1

rm $FILENAME
raspistill -vf -hf -w 1024 -h 768 -t 1 -o $FILENAME

python snapshot_email.py $FILENAME $EMAILADDR

