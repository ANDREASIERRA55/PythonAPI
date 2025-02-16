from flask import Flask, request, jsonify
import db 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API de Inventario en ejecución"}), 200

@app.route('/producto/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    mydb = db.get_connection()
    mycursor = mydb.cursor()
    
    sql = "SELECT p.id, p.nombre, p.precio, c.nombre AS categoria FROM productos p LEFT JOIN categorias c ON p.categoria_id = c.id WHERE p.id = %s"
    val = (producto_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    
    mydb.close()
    
    if result:
        producto = {
            "id": result[0],
            "nombre": result[1],
            "precio": float(result[2]),
            "categoria": result[3] if result[3] else "Sin categoría"
        }
        return jsonify(producto), 200
    else:
        return jsonify({"message": "Producto no encontrado"}), 404

@app.route('/inventario/<int:producto_id>', methods=['GET'])
def get_inventario(producto_id):
    mydb = db.get_connection()
    mycursor = mydb.cursor()
    
    sql = "SELECT i.id, p.nombre, i.cantidad, i.fecha_actualizacion FROM inventario i JOIN productos p ON i.producto_id = p.id WHERE i.producto_id = %s"
    val = (producto_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    
    mydb.close()
    
    if result:
        inventario = {
            "id": result[0],
            "producto": result[1],
            "cantidad": result[2],
            "fecha_actualizacion": result[3].strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(inventario), 200
    else:
        return jsonify({"message": "Inventario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
