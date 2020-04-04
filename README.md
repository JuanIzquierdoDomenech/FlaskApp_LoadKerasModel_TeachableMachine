# FlaskApp_LoadKerasModel_TeachableMachine
This project is a Flask App that loads a Keras model that classifies images, so the project can be used as a reference for other projects.

## Installation
1. Pull the code
2. Create a Python environment and activate it

*e.g.* 
`virtualenv -p python3 .venv`
`source .venv/bin/activate`

3. Install requirements

*e.g.*
`pip install -r requirements.txt`

4. Run the server

*e.g.*
`python server.py`

The server accepts an image via **POST**, adding the image as form-data with the key *imagefile*

![Demo with Postman](https://raw.githubusercontent.com/JuanIzquierdoDomenech/FlaskApp_LoadKerasModel_TeachableMachine/master/images/postman_demo.png)

## Convert .h5 to .pb
In the models folder, there is a keras model `.h5` and a script that converts it to `.pb`
If you intend to use the model inside Unity, remember to rename the `.pb` file to `.bytes`

