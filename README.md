# Mushroom-Map-Maker
This Flask web app generates a heat map of a specific mushroom's distribution across the globe.
The program uses the gmplot package and GPS data of mushroom observations from mushroomobserver.org.

## Usage case:

An example of searching for the mushroom with the genus amanita and the species muscaria:

![picture alt](/readme_images/input.png)

![picture alt](/readme_images/output.png)

In the app, this map can be scrolled to see the distribution of amanita muscaria across the globe. 


## Setup

1. Download the complete repo.

2. run `$pip install requirements.txt`

Note: gmplot is not a dependency, so do not pip install it as a package before running. gmplot was included directly in the repo because the source code has been (roughly) modified to communicate with flask.

3. Obtain google maps API key.
 
 This can be gotten from following these instructions: https://developers.google.com/maps/documentation/javascript/get-api-key
 The API key should be pasted into the config.py file.

4. Launch the app by:

`$python mushroom_map_maker_web_app.py` (recommended) 
 
 OR
 
 `$python mushroom_map_maker.py`





 


