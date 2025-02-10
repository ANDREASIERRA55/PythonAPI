from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hola'

@app.route('/user/<int:user_id>')  # Especifica <int:user_id> para que sea un entero
def get_user(user_id):
    user = {"id": user_id, "name": "Andrea", "telefono": "1234567890"}
    query = request.args.get('query')  # Obtiene el parámetro 'query' de la URL
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route('/user', methods=['POST'])
def create_user():
    '''user = request.get_json
    return jsonify(user), 201'''

    try:
        user_data = request.get_json()  # Obtener los datos JSON de la solicitud
        # Aquí deberías validar y procesar user_data, por ejemplo:
        if not user_data or 'username' not in user_data or 'email' not in user_data:
            return jsonify({'error': 'Faltan datos en la solicitud'}), 400

        # Crear el usuario en la base de datos (ejemplo)
        # ... (código para interactuar con la base de datos) ...
        # Supongamos que se crea el usuario correctamente y obtenemos un diccionario 'user' con los datos.

        return jsonify(user_data), 201  # Devolver los datos del usuario creado y el código 201 (Created)

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Capturar errores y devolver un mensaje de error genérico (Internal Server Error)


if __name__ == '__main__':
    app.run(debug=True)