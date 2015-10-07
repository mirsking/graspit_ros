FROM mirsking/ubuntu_ros:precise_fuerte
MAINTAINER Mirs King <mirsking@gamil.com>

RUN apt-get update && apt-get -y install ros-fuerte-graspit-simulator

RUN apt-get install -y x11vnc xvfb
RUN mkdir ~/.vnc
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

RUN echo GRASPIT=/opt/ros/fuerte/stacks/graspit_simulator/graspit:/opt/ros/fuerte/stacks/graspit_simulator/graspit/graspit_sources >> ~/.bashrc
