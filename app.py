from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
  return "<p>Hello, I am using Flask with the poke api!</p>"


@app.route("/pokeapi")
def endpoint():

  _list = []

  data = requests.get('https://pokeapi.co/api/v2/pokemon?limit=30')
    
  data = data.json()  

  _list = []
  for pokemon in data["results"]:
      _list.append({"name": pokemon["name"]})


  return jsonify(_list)


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
