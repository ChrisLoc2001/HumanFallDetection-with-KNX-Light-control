# HumanFallDetection-with-KNX-Light-control

<br>Setup Environment(HumanFallDetectionWithLightControl):</br>

1---> conda create --name FallDetectionEnv python=3.8

2---> conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 pytorch-cuda=11.7 -c pytorch -c nvidia

3---> install requirements.txt

<br>Setup Environment(ServerFallDetection):</br>

1---> Create a environment in python=3.9

2---> Install xknx library

<br>Usage:</br>

1---> Run ServerFallDetection main

2---> Run HumanFallDetection with this command-line:
	python fall-detector.py


# HumanFallDetection Alghorithms
The Fall Detection Algorithms used in this project is <br>[Multi-camera, multi-person, and real-time fall detection using long short term memory](https://doi.org/10.1117/12.2580700)</br>
