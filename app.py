#!/usr/bin/python3
"""Init the application"""
from flask import Flask, jsonify, render_template, request
from firebase_admin import credentials, firestore, initialize_app
from models.str_to_number import str_to_num
app = Flask(__name__)

cities = [
    "amazonas", "antioquia", "arauca", "atlantico", "bolivar",
    "boyaca", "caldas", "caqueta", "casanare", "cauca",
    "cesar", "choco", "cordoba", "cundinamarca", "huila",
    "magdalena", "meta", "nariño", "putumayo", "quindio",
    "risaralda", "santander", "tolima"
]

# establishing connection with firebase
credential = credentials.Certificate('psl-key.json')
def_app = initialize_app(credential)
db = firestore.client()
data_ref = db.collection("tusa-virus")


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def basic_page():
    """
    GET - get all the dato form db and show in dashboard
    POST - update data in db, using a form to updated
    """
    message = None
    total = 0
    if request.method == 'POST':
        # Try to put the data in database
        try:
            new_data = {}
            req = request.form
            city = req["city"]
            num_infected = req["infected"]
            # Verify if the data are integer or string
            try:
                new_data["infected"] = int(num_infected)
                data_ref.document(city).set(new_data)
            except ValueError:
                wtn = str_to_num(num_infected)
                print(wtn)
                if wtn is None:
                    message = "Data unsaved. Check if the data has correct"
                else:
                    new_data["infected"] = wtn
                    message = "Updated"
                    data_ref.document(city).set(new_data)
        except Exception as er:
            print(er)
    info_city = {}
    for city in cities:
        data = data_ref.document(city).get()
        info_city[city] = data.to_dict()["infected"]
    return render_template(
            "index.html", obj=info_city,
            msg=message, total=total
        )


@app.route('/update', strict_slashes=False)
def update():
    return render_template("update.html")


if __name__ == "__main__":
    app.run(debug=False, port=5000)
