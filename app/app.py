from flask import Flask, jsonify, request, make_response, render_template, redirect
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'applepieisawesome'
app.config['MYSQL_DB'] = 'mambadb'

CORS(app)

mysql = MySQL(app)

@app.route('/customers')
def customers():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM customer")
    customers = cur.fetchall()
    return render_template("customers.html", customers = customers)

@app.route('/customers/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        customers = request.form
        firstname = customers['firstname']
        lastname = customers['lastname']
        street = customers['street']
        city = customers['city']
        state = customers['state']
        zipcode = customers['zipcode']
        telephone = customers['telephone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer(firstname, lastname, street, city, state, zipcode, telephone) VALUES(%s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, street, city, state, zipcode, telephone))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('add_customer.html')

@app.route('/customers/update', methods=['GET', 'POST'])
def update_customer():
    return render_template('update_customer.html')


@app.route('/customers/update/firstname', methods=['GET', 'POST'])
def update_customer_firstname():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        firstname = customers['firstname']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET firstname = %s WHERE customerid = %s", (firstname, customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('update_customer_firstname.html')


@app.route('/customers/update/lastname', methods=['GET', 'POST'])
def update_customer_lastname():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        lastname = customers['lastname']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET lastname = %s WHERE customerid = %s", (lastname, customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('update_customer_lastname.html')

@app.route('/customers/update/street', methods=['GET', 'POST'])
def update_customer_street():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        street = customers['street']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET street = %s WHERE customerid = %s", (street, customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('update_customer_street.html')


@app.route('/customers/update/city', methods=['GET', 'POST'])
def update_customer_city():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        city = customers['city']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET city = %s WHERE customerid = %s", (city, customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('update_customer_city.html')


@app.route('/customers/update/state', methods=['GET', 'POST'])
def update_customer_state():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        state = customers['state']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET state = %s WHERE customerid = %s", (state, customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('update_customer_state.html')


@app.route('/customers/update/zipcode', methods=['GET', 'POST'])
def update_customer_zipcode():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        zipcode = customers['zipcode']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET zipcode = %s WHERE customerid = %s", (zipcode, customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('update_customer_zipcode.html')


@app.route('/customers/update/telephone', methods=['GET', 'POST'])
def update_customer_telephone():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        telephone = customers['telephone']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customer SET telephone = %s WHERE customerid = %s", (telephone, customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('update_customer_telephone.html')


@app.route('/customers/delete', methods=['GET', 'POST'])
def delete_customer():
    if request.method == 'POST':
        customers = request.form
        customerid = customers['customerid']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM customer WHERE customerid = %s", (customerid))
        mysql.connection.commit()
        cur.close()
        return redirect('/customers')
    return render_template('delete_customer.html')

@app.route('/businesses')
def businesses():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM business")
    businesses = cur.fetchall()
    return render_template("businesses.html", businesses = businesses)

@app.route('/businesses/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        businesses = request.form
        businessname = businesses['businessname']
        street = businesses['street']
        city = businesses['city']
        state = businesses['state']
        zipcode = businesses['zipcode']
        telephone = businesses['telephone']
        type = businesses['type']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO business(businessname, street, city, state, zipcode, telephone, type) VALUES(%s, %s, %s, %s, %s, %s, %s)", (businessname, street, city, state, zipcode, telephone, type))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('add_business.html')

@app.route('/businesses/update', methods=['GET', 'POST'])
def update_business():
    return render_template('update_business.html')

@app.route('/businesses/update/businessname', methods=['GET', 'POST'])
def update_business_businessname():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        businessname = businesses['businessname']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE business SET businessname = %s WHERE businessid = %s", (businessname, businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('update_business_businessname.html')

@app.route('/businesses/update/street', methods=['GET', 'POST'])
def update_business_street():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        street = businesses['street']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE business SET street = %s WHERE businessid = %s", (street, businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('update_business_street.html')


@app.route('/businesses/update/city', methods=['GET', 'POST'])
def update_business_city():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        city = businesses['city']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE business SET city = %s WHERE businessid = %s", (city, businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('update_business_city.html')


@app.route('/businesses/update/state', methods=['GET', 'POST'])
def update_business_state():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        state = businesses['state']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE business SET state = %s WHERE businessid = %s", (state, businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('update_business_state.html')


@app.route('/businesses/update/zipcode', methods=['GET', 'POST'])
def update_business_zipcode():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        zipcode = businesses['zipcode']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE business SET zipcode = %s WHERE businessid = %s", (zipcode, businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('update_business_zipcode.html')


@app.route('/businesses/update/telephone', methods=['GET', 'POST'])
def update_business_telephone():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        telephone = businesses['telephone']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE business SET telephone = %s WHERE businessid = %s", (telephone, businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('update_business_telephone.html')

@app.route('/businesses/update/type', methods=['GET', 'POST'])
def update_business_type():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        type = businesses['type']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE business SET type = %s WHERE businessid = %s", (type, businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('update_business_type.html')

@app.route('/businesses/delete', methods=['GET', 'POST'])
def delete_business():
    if request.method == 'POST':
        businesses = request.form
        businessid = businesses['businessid']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM business WHERE businessid = %s", (businessid))
        mysql.connection.commit()
        cur.close()
        return redirect('/businesses')
    return render_template('delete_business.html')

@app.route('/products')
def products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM product")
    products = cur.fetchall()
    return render_template("products.html", products = products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        products = request.form
        productlabel = products['productlabel']
        productcategory = products['productcategory']
        quantity = products['quantity']
        businessid = products['businessid']
        manufacturer = products['manufacturer']
        modelnumber = products['modelnumber']
        serialnumber = products['serialnumber']
        sku = products['sku']
        buyprice = products['buyprice']
        msrp = products['msrp']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product(productlabel, productcategory, quantity, businessid, manufacturer, modelnumber, serialnumber, sku, buyprice, msrp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (productlabel, productcategory, quantity, businessid, manufacturer, modelnumber, serialnumber, sku, buyprice, msrp))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('add_product.html')

@app.route('/products/update', methods=['GET', 'POST'])
def update_product():
    return render_template('update_product.html')

@app.route('/products/update/productlabel', methods=['GET', 'POST'])
def update_product_productlabel():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        productlabel = products['productlabel']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET productlabel = %s WHERE productid = %s", (productlabel, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_productlabel.html')

@app.route('/products/update/productcategory', methods=['GET', 'POST'])
def update_product_productcategory():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        productcategory = products['productcategory']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET productcategory = %s WHERE productid = %s", (productcategory, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_productcategory.html')

@app.route('/products/update/quantity', methods=['GET', 'POST'])
def update_product_quantity():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        quantity = products['quantity']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET quantity = %s WHERE productid = %s", (quantity, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_quantity.html')

@app.route('/products/update/businessid', methods=['GET', 'POST'])
def update_product_businessid():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        businessid = products['businessid']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET businessid = %s WHERE productid = %s", (businessid, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_businessid.html')

@app.route('/products/update/manufacturer', methods=['GET', 'POST'])
def update_product_manufacturer():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        manufacturer = products['manufacturer']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET manufacturer = %s WHERE productid = %s", (manufacturer, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_manufacturer.html')

@app.route('/products/update/modelnumber', methods=['GET', 'POST'])
def update_product_modelnumber():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        modelnumber = products['modelnumber']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET modelnumber = %s WHERE productid = %s", (modelnumber, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_modelnumber.html')

@app.route('/products/update/serialnumber', methods=['GET', 'POST'])
def update_product_serialnumber():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        serialnumber = products['serialnumber']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET serialnumber = %s WHERE productid = %s", (serialnumber, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_serialnumber.html')

@app.route('/products/update/sku', methods=['GET', 'POST'])
def update_product_sku():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        sku = products['sku']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET sku = %s WHERE productid = %s", (sku, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_sku.html')

@app.route('/products/update/buyprice', methods=['GET', 'POST'])
def update_product_buyprice():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        buyprice = products['buyprice']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET buyprice = %s WHERE productid = %s", (buyprice, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_buyprice.html')

@app.route('/products/update/mrsp', methods=['GET', 'POST'])
def update_product_msrp():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        mrsp = products['mrsp']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE product SET mrsp = %s WHERE productid = %s", (mrsp, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('update_product_msrp.html')

@app.route('/products/delete', methods=['GET', 'POST'])
def delete_product():
    if request.method == 'POST':
        products = request.form
        productid = products['productid']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM product WHERE productid = %s", (productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/products')
    return render_template('delete_product.html')

@app.route('/products/filter-by', methods=['GET', 'POST'])
def filter_by_product():
    if request.method == 'POST':
        products = request.form
    return render_template('filter_by_product.html')


@app.route('/orders')
def orders():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    return render_template("orders.html", orders = orders)

@app.route('/orders/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        orders = request.form
        customerid = orders['customerid']
        to_street = orders['to_street']
        to_city = orders['to_city']
        to_state = orders['to_state']
        to_zipcode = orders['to_zipcode']
        telephone = orders['telephone']
        orderdate = orders['orderdate']
        shipdate = orders['shipdate']
        returndate = orders['returndate']
        ordertotal = orders['ordertotal']
        productid = orders['productid']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO orders(customerid, to_street, to_city, to_state, to_zipcode, telephone, orderdate, shipdate, returndate, ordertotal, productid) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (customerid, to_street, to_city, to_state, to_zipcode, telephone, orderdate, shipdate, returndate, ordertotal, productid))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('add_order.html')

@app.route('/orders/update', methods=['GET', 'POST'])
def update_order():
    return render_template('update_order.html')

@app.route('/orders/update/customerid', methods=['GET', 'POST'])
def update_order_customerid():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        customerid = orders['customerid']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET customerid = %s WHERE ordernumber = %s", (customerid, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_customerid.html')

@app.route('/orders/update/to_street', methods=['GET', 'POST'])
def update_order_to_street():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        to_street = orders['to_street']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET to_street = %s WHERE ordernumber = %s", (to_street, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_to_street.html')

@app.route('/orders/update/to_city', methods=['GET', 'POST'])
def update_order_to_city():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        to_city = orders['to_city']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET to_city = %s WHERE ordernumber = %s", (to_city, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_to_city.html')

@app.route('/orders/update/to_state', methods=['GET', 'POST'])
def update_order_to_state():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        to_state = orders['to_state']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET to_state = %s WHERE ordernumber = %s", (to_state, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_to_state.html')

@app.route('/orders/update/to_zipcode', methods=['GET', 'POST'])
def update_order_to_zipcode():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        to_zipcode = orders['to_zipcode']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET to_zipcode = %s WHERE ordernumber = %s", (to_zipcode, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_to_zipcode.html')

@app.route('/orders/update/telephone', methods=['GET', 'POST'])
def update_order_telephone():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        telephone = orders['telephone']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET telephone = %s WHERE ordernumber = %s", (telephone, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_telephone.html')

@app.route('/orders/update/orderdate', methods=['GET', 'POST'])
def update_order_orderdate():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        orderdate = orders['orderdate']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET orderdate = %s WHERE ordernumber = %s", (orderdate, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_orderdate.html')

@app.route('/orders/update/returndate', methods=['GET', 'POST'])
def update_order_returndate():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        returndate = orders['returndate']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET returndate = %s WHERE ordernumber = %s", (returndate, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_returndate.html')

@app.route('/orders/update/shipdate', methods=['GET', 'POST'])
def update_order_shipdate():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        shipdate = orders['shipdate']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET shipdate = %s WHERE ordernumber = %s", (shipdate, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_shipdate.html')

@app.route('/orders/update/ordertotal', methods=['GET', 'POST'])
def update_order_ordertotal():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        ordertotal = orders['ordertotal']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET ordertotal = %s WHERE ordernumber = %s", (ordertotal, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_ordertotal.html')

@app.route('/orders/update/productid', methods=['GET', 'POST'])
def update_order_productid():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        productid = orders['productid']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE orders SET productid = %s WHERE ordernumber = %s", (productid, ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('update_order_productid.html')

@app.route('/orders/delete', methods=['GET', 'POST'])
def delete_order():
    if request.method == 'POST':
        orders = request.form
        ordernumber = orders['ordernumber']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM order WHERE ordernumber = %s", (ordernumber))
        mysql.connection.commit()
        cur.close()
        return redirect('/orders')
    return render_template('delete_order.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
