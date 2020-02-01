#!/usr/bin/python3
"""Init the application"""
from flask import Flask, jsonify, render_template
from firebase_admin import credentials, firestore, initialize_app
from models import str_to_number
app = Flask(__name__)
cities = [
    "amazonas", "antioquia", "arauca", "atlantico", "bolivar",
    "boyaca", "caldas", "caqueta", "casanare", "cauca",
    "cesar", "choco", "cordoba", "cundinamarca", "huila",
    "magdalena", "meta", "nariño", "putumayo", "quindio",
    "risaralda", "santander", "tolima"
]

# establishing connection with firebase
credential = credentials.Certificate('fb-psl-key.json')
def_app = initialize_app(credential)
db = firestore.client()
data_ref = db.collection("tusa-virus")


@app.route('/', strict_slashes=False)
def basic_page():
    info_city = {}
    for city in cities:
        data = data_ref.document(city).get()
        info_city[city] = data.to_dict()["infected"]
    return render_template("index.html", obj=info_city)


@app.route('/update', strict_slashes=False)
def update():
    pass


if __name__ == "__main__":
    app.run(debug=True)