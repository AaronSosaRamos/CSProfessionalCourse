from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database
products = {}

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product_id = data.get('id')
    products[product_id] = data
    return jsonify({'message': 'Product added successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
