from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

CUSTOMERS = [
    {
        'customerid': 1000,
        'firstname': 'George',
        'lastname': 'Perez',
        'street': '3022 Calle Ibiza',
        'city': 'Cabo Rojo',
        'state': 'PR',
        'zipcode': '00623-8962',
        'telephone': 7874210026
    },
    {
        'customerid': 1001,
        'firstname': 'Steve',
        'lastname': 'Jobs',
        'street': '1 Infinite Loop',
        'city': 'Cupertino',
        'state': 'CA',
        'zipcode': '95014',
        'telephone': 4089961010
    },
    {
        'customerid': 1002,
        'firstname': 'Carlos',
        'lastname': 'Malave',
        'street': 'PR-109',
        'city': 'Anasco',
        'state': 'PR',
        'zipcode': '00610',
        'telephone': 7875555555
    },
    {
        'customerid': 1003,
        'firstname': 'Barack',
        'lastname': 'Obama',
        'street': '1600 Pennssylvania Avenue NW',
        'city': 'Washington, DC',
        'state': '',
        'zipcode': '200003',
        'telephone': 5555555555
    }
]

BUSINESS = [
    {
        'businessname': 'TITANPOINTE',
        'duns': '123-123-1231',
        'street': '3022 Calle Ibiza',
        'city': 'Cabo Rojo',
        'state': 'PR',
        'zipcode': '00623-8962',
        'telephone': 7874210026,
        'type': 'type',
        'numbercustomers': 42
    },
    {
        'businessname': 'Apple Inc.',
        'duns': '123-123-1232',
        'street': '1 Infinite Loop',
        'city': 'Cupertino',
        'state': 'CA',
        'zipcode': '95014',
        'telephone': 4089961010,
        'type': 'type',
        'numbercustomers': 42
    },
    {
        'businessname': 'Floral Bouquet',
        'duns': '123-123-1233',
        'street': 'PR-109',
        'city': 'Anasco',
        'state': 'PR',
        'zipcode': '00610',
        'telephone': 7875555555,
        'type': 'type',
        'numbercustomers': 42
    },
    {
        'businessname': 'The Executive Branch of the United States of America',
        'duns': '123-123-1234',
        'street': '1600 Pennssylvania Avenue NW',
        'city': 'Washington, DC',
        'state': '',
        'zipcode': '200003',
        'telephone': 5555555555,
        'type': 'type',
        'numbercustomers': 42
    }
]

PRODUCTS = []

ORDERS = [
    {
        'ordernumber': 'ON-1000',
        'customerid': '1000',
        'to_street': '3022 Calle Ibiza',
        'to_city': 'Cabo Rojo',
        'to_state': 'PR',
        'to_zipcode': '00623-8962',
        'telephone': 7874210026,
        'orderdate': '2018-03-01',
        'shipdate': '2018-03-02',
        'returndate': '',
        'ordertotal': 123.42,
        'productid': 'P000001'
    },
    {
        'ordernumber': 'ON-1001',
        'customerid': '1001',
        'to_street': '1 Infinite Loop',
        'to_city': 'Cupertino',
        'to_state': 'CA',
        'to_zipcode': '95014',
        'telephone': 4089961010,
        'orderdate': '2018-03-01',
        'shipdate': '2018-03-02',
        'returndate': '',
        'ordertotal': 123.42,
        'productid': 'P000002'
    },
    {
        'ordernumber': 'ON-1002',
        'customerid': '1002',
        'to_street': 'PR-109',
        'to_city': 'Anasco',
        'to_state': 'PR',
        'to_zipcode': '00610',
        'telephone': 7875555555,
        'orderdate': '2018-03-01',
        'shipdate': '2018-03-02',
        'returndate': '',
        'ordertotal': 123.42,
        'productid': 'P000003'
    },
    {
        'ordernumber': 'ON-1003',
        'customerid': '1003',
        'to_street': '1600 Pennssylvania Avenue NW',
        'to_city': 'Washington, DC',
        'to_state': '',
        'to_zipcode': '200003',
        'telephone': 5555555555,
        'orderdate': '2018-03-01',
        'shipdate': '2018-03-02',
        'returndate': '',
        'ordertotal': 123.42,
        'productid': 'P000004'
    }
]


@app.route('/customers', methods=['GET', 'POST', 'DELETE'])
def all_customers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CUSTOMERS.append({
            'customerid': post_data.get('customerid'),
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

@app.route('/businesses', methods=['GET', 'POST', 'DELETE'])
def all_businesses():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BUSINESS.append({
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
        response_object['business'] = BUSINESS
    return jsonify(response_object)

@app.route('/products', methods=['GET', 'POST', 'DELETE'])
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

@app.route('/orders', methods=['GET'])
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

if __name__ == '__main__':
    app.run()
