# Mushroom-Map-Maker
This program generates a heat map of a specific mushroom's distribution across the globe.

The program uses the gmplot package and GPS data of mushroom observations from mushroomobserver.org.

Installation:

Download the complete repo, install the dependencies, then launch either mushroom_map_maker_web_app.py (recommended) or mushroom_map_maker.py

Dependencies:

Flask_WTF==0.14.2

WTForms==2.1

Flask==0.12.2

setuptools==28.8.0

Flask_Bootstrap==3.3.7.1

requests==2.18.4

Note: gmplot is not a dependency, so do not pip install it as a package before running. gmplot was included directly in the repo because the source code has been (roughly) modified to communicate with flask. mushroom_map_maker.py can be run directly or can be run through the flask app mushroom_map_maker_web_app. The program was designed primarily for use through the flask app. 

An example of the output generated by a search for a mushroom with the genus amanita and the species muscaria:

https://imgur.com/a/BB9Tn

In the app, this map can be scrolled to see the distribution of amanita muscaria across the globe. 

A pull request was put in by Doug Skinner to improve the front-end. He describes the changes he made and the rationale behind each change in a great blog post: https://doug-skinner.com/writing/2018/01/19/Mushroom-Redesign.html 


