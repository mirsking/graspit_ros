#!/bin/sh

docker run -it \
-p 5901:5900 \
-v $PWD/../models/kinova_hand:/root/graspit_kinova_hand \
mirsking/graspit_ros:precise_fuerte \
x11vnc -forever -usepw -create
