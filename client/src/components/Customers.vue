<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <nav class="navbar navbar-default">
          <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
              <ul class="nav navbar-nav">
                <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">Separated link</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">One more separated link</a></li>
                  </ul>
                </li>
              </ul>
              <form class="navbar-form navbar-left">
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="Search">
                </div>
                <button type="submit" class="btn btn-default">Submit</button>
              </form>
              <ul class="nav navbar-nav navbar-right">
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">Separated link</a></li>
                  </ul>
                </li>
              </ul>
            </div><!-- /.navbar-collapse -->
          </div><!-- /.container-fluid -->
        </nav>
        <h1>Customers</h1>
        <hr>
        <br>
        <br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.customer-modal>Add Customer</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Street</th>
              <th scope="col">State</th>
              <th scope="col">ZIP Code</th>
              <th scope="col">Telephone</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(customer, index) in customers" :key="index">
              <td>{{ customer.customerid }}</td>
              <td>{{ customer.firstname }}</td>
              <td>{{ customer.lastname }}</td>
              <td>{{ customer.street }}</td>
              <td>{{ customer.city }}</td>
              <td>{{ customer.state }}</td>
              <td>{{ customer.zipcode }}</td>
              <td>{{ customer.telephone }}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addCustomerModal" id="customer-modal" title="Add a new customer" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-customerid-group" label="ID:" label-for="form-customerid-input">
          <b-form-input
            id="form-customerid-input"
            type="text"
            v-model="addCustomerForm.customerid"
            required
            placeholder="Enter ID"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-firstname-group" label="First Name:" label-for="form-firstname-input">
          <b-form-input
            id="form-firstname-input"
            type="text"
            v-model="addCustomerForm.firstname"
            required
            placeholder="Enter first name"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-lastname-group" label="Last Name:" label-for="form-lastname-input">
          <b-form-input
            id="form-lastname-input"
            type="text"
            v-model="addCustomerForm.lastname"
            required
            placeholder="Enter last name"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-street-group" label="Street:" label-for="form-street-input">
          <b-form-input
            id="form-street-input"
            type="text"
            v-model="addCustomerForm.street"
            required
            placeholder="Enter street"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-city-group" label="City:" label-for="form-city-input">
          <b-form-input
            id="form-city-input"
            type="text"
            v-model="addCustomerForm.city"
            required
            placeholder="Enter city"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-state-group" label="State:" label-for="form-state-input">
          <b-form-input
            id="form-state-input"
            type="text"
            v-model="addCustomerForm.state"
            required
            placeholder="Enter state"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-zipcode-group" label="ZIP Code:" label-for="form-zipcode-input">
          <b-form-input
            id="form-zipcode-input"
            type="text"
            v-model="addCustomerForm.zipcode"
            required
            placeholder="Enter ZIP code"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-telephone-group" label="Telephone:" label-for="form-telephone-input">
          <b-form-input
            id="form-telephone-input"
            type="text"
            v-model="addCustomerForm.telephone"
            required
            placeholder="Enter telephone"
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
      customers: [],
      addCustomerForm: {
        customerid: '',
        firstname: '',
        lastname: '',
        street: '',
        city: '',
        state: '',
        zipcode: '',
        telephone: '',
      },
    };
  },
  methods: {
    getCustomers() {
      const path = 'http://localhost:5000/customers';
      axios.get(path)
        .then((res) => {
          this.customers = res.data.customers;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addCustomer(payload) {
      const path = 'http://localhost:5000/customers';
      axios.post(path, payload)
        .then(() => {
          this.getCustomers();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCustomers();
        });
    },
    initForm() {
      this.addCustomerForm.customerid = '';
      this.addCustomerForm.firstname = '';
      this.addCustomerForm.lastname = '';
      this.addCustomerForm.street = '';
      this.addCustomerForm.city = '';
      this.addCustomerForm.state = '';
      this.addCustomerForm.zipcode = '';
      this.addCustomerForm.telephone = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      const payload = {
        customerid: this.addCustomerorm.customerid,
        firstname: this.adCustomerForm.firstname,
        lastname: this.adCustomerForm.lastname,
        street: this.adCustomerForm.street,
        city: this.adCustomerForm.city,
        state: this.adCustomerForm.state,
        zipcode: this.adCustomerForm.zipcode,
        telephone: this.adCustomerForm.telephone,
      };
      this.addCustomer(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getCustomers();
  },
};
</script>
