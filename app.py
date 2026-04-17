from src.utils import *
from src.data_prep import *
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.json.sort_keys = False
API_KEY = "99VEOSMART99"

@app.route('/data_marque_modele', methods=['GET'])
def get_df_marque_modèle():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        try:
            df_marque_modèle_json = df_marque_modèle.to_json(force_ascii=False)
        except ValueError:
            return jsonify({"error": "Error in values"}), 400

        return jsonify(df_marque_modèle_json), 200

@app.route('/data_marque', methods=['GET'])
def get_df_marque():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        try:
            df_marque_json = df_marque.to_json(force_ascii=False)
        except ValueError:
            return jsonify({"error": "Error in values"}), 400

        return jsonify(df_marque_json), 200

@app.route('/data_modele', methods=['GET'])
def get_df_modèle():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        try:
            df_modèle_json = df_modèle.to_json(force_ascii=False)
        except ValueError:
            return jsonify({"error": "Error in values"}), 400

        return jsonify(df_modèle_json), 200

@app.route('/data_sous_modele', methods=['GET'])
def get_df_sous_modèle():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        try:
            df_sous_modèle_json = df_sous_modèle.to_json(force_ascii=False)
        except ValueError:
            return jsonify({"error": "Error in values"}), 400

        return jsonify(df_sous_modèle_json), 200

@app.route('/add_marque', methods=['GET'])
def add_marque_api():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        marque = request.args.get("marque")
        try:
            add_marque(marque)
        except ValueError as e:
            print(e)
            return jsonify({"error": "Error in values"}), 400

        save_df_marque()
        save_df_marque_modèle()
        return "Marque added", 200

@app.route('/add_modele', methods=['GET'])
def add_modèle_api():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        marque = request.args.get("marque")
        modèle = request.args.get("modele")
        try:
            add_modèle(modèle, marque)
        except ValueError as e:
            print(e)
            return jsonify({"error": "Error in values"}), 400

        save_df_modèle()
        save_df_marque_modèle()
        return "Modèle added", 200

@app.route('/add_sous_modele', methods=['GET'])
def add_sous_modèle_api():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        marque = request.args.get("marque")
        modèle = request.args.get("modele")
        sous_modèle = request.args.get("sous_modele")
        try:
            add_sous_modèle(sous_modèle, modèle, marque)
        except ValueError as e:
            print(e)
            return jsonify({"error": "Error in values"}), 400
        save_df_sous_modèle()
        save_df_marque_modèle()

        return "Sous-Modèle added", 200

@app.route('/save_data', methods=['GET'])
def save_data_api():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':

        save_df_marque()
        save_df_modèle()
        save_df_sous_modèle()
        save_df_marque_modèle()

        return "Data Saved", 200


@app.route('/marque_list', methods=['GET'])
def marque_list_api():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        marque_list = get_marque_list()
        return marque_list , 200

@app.route('/modele_list', methods=['GET'])
def modèle_list_api():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        marque = str(request.args.get("marque")).upper()
        modèle_list = get_modèle_list(marque)
        return modèle_list , 200

@app.route('/sous_modele_list', methods=['GET'])
def sous_modèle_list_api():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == 'GET':
        marque = str(request.args.get("marque")).upper()
        modèle = request.args.get("modele")
        sous_modèle_list = get_sous_modèle_list(marque,modèle)
        return sous_modèle_list , 200



@app.route('/')
def index():
    return "API Flask est en ligne !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086)
