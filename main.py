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

if __name__ == '__main__':
    app.run(debug=True)