from flask import Flask, request, jsonify
# from flask_cors import CORS
#///
# app = Flask(__name__)
# cors = CORS(app, resources={"/api"})

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/topten', methods=['GET'])
def ReturnJSON():
    if (request.method == 'GET'):
        data ={
            "name": ['Pepas - Farrukou' ,
                     'Essence - WizKid ft. Justin Bieber and Tems',
                     'All Too Well - Taylor Swift',
                     'VBS- Lucy Dacus',
                     'Monster - Yoasobi',
                    'Twerkulator - City Girls',
                     'Good 4 U - Olivia Rodrigo',
                     'La Mama de La Mama - El Alfa',
                    'Wilder Days - Morgan Wade',
                    'Woman - Doja Cat' ]}
        return jsonify(data)


if __name__ == "__main__":
    app.run()