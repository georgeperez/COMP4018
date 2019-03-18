<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Orders</h1>
        <hr>
        <br>
        <br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.orders-modal>Add Order</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Order number</th>
              <th scope="col">Customer id</th>
              <th scope="col">to Street</th>
              <th scope="col">to City</th>
              <th scope="col">to State</th>
              <th scope="col">to ZIP Code</th>
              <th scope="col">Telephone</th>
              <th scope="col">Order date</th>
              <th scope="col">Ship date</th>
              <th scope="col">Return date</th>
              <th scope="col">Order total</th>
              <th scope="col">Product id</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(orders, index) in orders" :key="index">
              <td>{{ orders.ordernumber }}</td>
              <td>{{ orders.customerid }}</td>
              <td>{{ orders.to_street }}</td>
              <td>{{ orders.to_city }}</td>
              <td>{{ orders.to_state }}</td>
              <td>{{ orders.to_zipcode }}</td>
              <td>{{ orders.telephone }}</td>
              <td>{{ orders.orderdate }}</td>
              <td>{{ orders.shipdate }}</td>
              <td>{{ orders.returndate }}</td>
              <td>{{ orders.ordertotal }}</td>
              <td>{{ orders.productid }}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addOrdersModal" id="orders-modal" title="Add a new order" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-ordernumber-group" label="Name:" label-for="form-ordernumber-input">
          <b-form-input
            id="form-ordernumber-input"
            type="text"
            v-model="addOrdersForm.ordernumber"
            required
            placeholder="Enter Order Number"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-customerid-group" label="Customer ID:" label-for="form-customerid-input">
          <b-form-input
            id="form-customerid-input"
            type="text"
            v-model="addOrdersForm.customerid"
            required
            placeholder="Enter Customer ID"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-tostreet-group" label="To Street:" label-for="form-tostreet-input">
          <b-form-input
            id="form-tostreet-input"
            type="text"
            v-model="addOrdersForm.to_street"
            required
            placeholder="Enter to street"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-tocity-group" label="To City:" label-for="form-tocity-input">
          <b-form-input
            id="form-tocity-input"
            type="text"
            v-model="addOrdersForm.to_city"
            required
            placeholder="Enter to city"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-tostate-group" label="To State:" label-for="form-tostate-input">
          <b-form-input
            id="form-tostate-input"
            type="text"
            v-model="addOrdersForm.to_state"
            required
            placeholder="Enter to state"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-tozipcode-group" label="To ZIP Code:" label-for="form-tozipcode-input">
          <b-form-input
            id="form-tozipcode-input"
            type="text"
            v-model="addOrdersForm.to_zipcode"
            required
            placeholder="Enter to ZIP code"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-telephone-group" label="Telephone:" label-for="form-telephone-input">
          <b-form-input
            id="form-telephone-input"
            type="text"
            v-model="addOrdersForm.telephone"
            required
            placeholder="Enter telephone"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-orderdate-group" label="Order Date:" label-for="form-orderdate-input">
          <b-form-input
            id="form-orderdate-input"
            type="text"
            v-model="addOrdersForm.orderdate"
            required
            placeholder="Order date"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-shipdate-group" label="Ship Date:" label-for="form-shipdate-input">
          <b-form-input
            id="form-shipdate-input"
            type="text"
            v-model="addOrdersForm.shipdate"
            placeholder="Ship Date"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-returndate-group" label="Return Date:" label-for="form-returndate-input">
          <b-form-input
            id="form-returndate-input"
            type="text"
            v-model="addOrdersForm.returndate"
            placeholder="Return Date"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-ordertotal-group" label="Order Total:" label-for="form-ordertotal-input">
          <b-form-input
            id="form-ordertotal-input"
            type="text"
            v-model="addOrdersForm.ordertotal"
            required
            placeholder="Order Total"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-productid-group" label="Product id:" label-for="form-productid-input">
          <b-form-input
            id="form-productid-input"
            type="text"
            v-model="addOrdersForm.productid"
            required
            placeholder="Product id"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      orders: [],
      addOrdersForm: {
        ordernumber: '',
        customerid: '',
        to_street: '',
        to_city: '',
        to_state:'',
        to_zipcode:'',
        telephone:'',
        orderdate:'',
        shipdate:'',
        returndate:'',
        ordertotal:'',
        productid:'',
      },
    };
  },
  methods: {
    getOrders() {
      const path = 'http://localhost:5000/orders';
      axios.get(path)
        .then((res) => {
          this.orders = res.data.orders;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addOrdersForm(payload) {
      const path = 'http://localhost:5000/orders';
      axios.post(path, payload)
        .then(() => {
          this.getOrders();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getOrders();
        });
    },
    initForm() {
      this.addOrdersForm.ordernumber = '';
      this.addOrdersForm.customerid = '';
      this.addOrdersForm.to_street = '';
      this.addOrdersForm.to_city = '';
      this.addOrdersForm.to_state = '';
      this.addOrdersForm.to_zipcode = '';
      this.addOrdersForm.telephone = '';
      this.addOrdersForm.orderdate = '';
      this.addOrdersForm.shipdate = '';
      this.addOrdersForm.returndate = '';
      this.addOrdersForm.ordertotal = '';
      this.addOrdersForm.productid = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addOrdersModal.hide();
      const payload = {
        ordernumber: this.addOrdersForm.ordernumber,
        customerid: this.addOrdersForm.customerid,
        to_street: this.addOrdersForm.to_street,
        to_city: this.addOrdersForm.to_city,
        to_state: this.addOrdersForm.to_state,
        to_zipcode: this.addOrdersForm.to_zipcode,
        telephone: this.addOrdersForm.telephone,
        orderdate: this.addOrdersForm.orderdate,
        shipdate: this.addOrdersForm.shipdate,
        returndate: this.addOrdersForm.returndate,
        ordertotal: this.addOrdersForm.ordertotal,
        productid: this.addOrdersForm.productid,
      };
      this.addOrdersForm(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addOrdersModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getOrders();
  },
};
</script>
