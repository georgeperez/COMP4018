from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_restful import reqparse
import uuid

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

CUSTOMERS = []

BUSINESSES = []

PRODUCTS = []

ORDERS = []

def remove_customer(customer_id):
    for customer in CUSTOMERS:
        if customer['customerid'] == customer_id:
            CUSTOMERS.remove(customer)
            return True
    return False

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/customers', methods=['GET', 'POST'])
def all_customers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CUSTOMERS.append({
            'customerid': uuid.uuid4().hex,
            'firstname': post_data.get('firstname'),
            'lastname': post_data.get('lastname'),
            'street': post_data.get('street'),
            'city': post_data.get('city'),
            'state': post_data.get('state'),
            'zipcode': post_data.get('zipcode'),
            'telephone': post_data.get('telephone')
        })
        response_object['message'] = 'Customer added!'
    else:
        response_object['customers'] = CUSTOMERS
    return jsonify(response_object)

@app.route('/customers/<customer_id>', methods=['PUT', 'DELETE'])
def update_customer():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_customer(customer_id)
        CUSTOMERS.append({
            'customerid': uuid.uuid4().hex,
            'firstname': post_data.get('firstname'),
            'lastname': post_data.get('lastname'),
            'street': post_data.get('street'),
            'city': post_data.get('city'),
            'state': post_data.get('state'),
            'zipcode': post_data.get('zipcode'),
            'telephone': post_data.get('telephone')
        })
        response_object['message'] = 'Customer updated!'
    if request.method == 'DELETE':
        remove_customer(customer_id)
        response_object['message'] = 'Customer deleted!'
    return jsonify(response_object)

@app.route('/businesses', methods=['GET', 'POST', 'PUT', 'DELETE'])
def all_businesses():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BUSINESSES.append({
            'businessname': post_data.get('businessname'),
            'duns': post_data.get('duns'),
            'street': post_data.get('street'),
            'city': post_data.get('city'),
            'state': post_data.get('state'),
            'zipcode': post_data.get('zipcode'),
            'telephone': post_data.get('telephone'),
            'type': post_data.get('type'),
            'numbercustomers': post_data.get('numbercustomers')
        })
        response_object['message'] = 'Business added!'
    else:
        response_object['businesses'] = BUSINESSES
    return jsonify(response_object)

@app.route('/products', methods=['GET', 'POST', 'PUT', 'DELETE'])
def all_products():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        PRODUCTS.append({
            'productid': post_data.get('productid'),
            'productlabel': post_data.get('productlabel'),
            'productcategory': post_data.get('productcategory'),
            'quantity': post_data.get('quantity'),
            'businessname': post_data.get('businessname'),
            'manufacturer': post_data.get('manufacturer'),
            'modelnumber': post_data.get('modelnumber'),
            'serialnumber': post_data.get('serialnumber'),
            'sku': post_data.get('sku'),
            'buyprice': post_data.get('buyprice'),
            'msrp': post_data.get('msrp')
        })
        response_object['message'] = 'Product added!'
    else:
        response_object['products'] = PRODUCTS
    return jsonify(response_object)


@app.route('/api/v1.0/orders', methods=['GET', 'POST', 'PUT', 'DELETE'])
def all_orders():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        ORDERS.append({
            'ordernumber': post_data.get('ordernumber'),
            'customerid': post_data.get('customerid'),
            'to_street': post_data.get('to_street'),
            'to_city': post_data.get('to_city'),
            'to_state': post_data.get('to_state'),
            'to_zipcode': post_data.get('to_zipcode'),
            'telephone': post_data.get('telephone'),
            'orderdate': post_data.get('orderdate'),
            'shipdate': post_data.get('shipdate'),
            'returndate': post_data.get('returndate'),
            'ordertotal': post_data.get('ordertotal'),
            'productid': post_data.get('productid'),
        })
        response_object['message'] = 'Order added!'
    else:
        response_object['orders'] = ORDERS
    return jsonify(response_object)

@app.route('/')
def index():
    return "Home"

if __name__ == '__main__':
    app.run()
