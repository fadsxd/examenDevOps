from flask import Flask, jsonify

app = Flask(__name__)

# Añadimos la / al final para que sea más flexible
@app.route('/api/v1/', methods=['GET'])
def get_status():
    return jsonify({
        "message": "Hola desde la infraestructura automatizada",
        "status": "success",
        "modulo": 3
    })

if __name__ == '__main__':
    # Configurado para ser accesible externamente en el puerto 5000 [cite: 14]
    app.run(host='0.0.0.0', port=5000)