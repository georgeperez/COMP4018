<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Customers</h1>
        <hr>
        <br>
        <br>
        <button type="button" class="btn btn-success btn-sm"
        v-b-modal.customer-modal>Add Customer</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Customer ID</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Street</th>
              <th scope="col">City</th>
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
                <button type="button" class="btn btn-warning btn-sm" v-b-modal.customer-update-modal @click="editCustomer(customer)">Update</button>
                <button type="button" class="btn btn-danger btn-sm" @click="onDeleteCustomer(customer)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addCustomerModal" id="customer-modal" title="Add a new customer" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-firstname-group" label="First Name:"
        label-for="form-firstname-input">
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
    <b-modal ref="editCustomerModal"
    id="customer-update-modal"
    title="Update"
    hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-firstname-edit-group" label="First Name:"
      label-for="form-firstname-edit-input">
        <b-form-input
          id="form-firstname-edit-input"
          type="text"
          v-model="editForm.firstname"
          required
          placeholder="Enter first name"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="form-lastname-edit-group" label="Last Name:" label-for="form-lastname-edit-input">
        <b-form-input
          id="form-lastname-edit-input"
          type="text"
          v-model="editForm.lastname"
          required
          placeholder="Enter last name"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="form-street-edit-group" label="Street:" label-for="form-street-edit-input">
        <b-form-input
          id="form-street-edit-input"
          type="text"
          v-model="editForm.street"
          required
          placeholder="Enter street"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="form-city-edit-group" label="City:" label-for="form-city-edit-input">
        <b-form-input
          id="form-city-edit-input"
          type="text"
          v-model="editForm.city"
          required
          placeholder="Enter city"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="form-state-edit-group" label="State:" label-for="form-state-edit-input">
        <b-form-input
          id="form-state-edit-input"
          type="text"
          v-model="editForm.state"
          required
          placeholder="Enter state"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="form-zipcode-edit-group" label="ZIP Code:" label-for="form-zipcode-edit-input">
        <b-form-input
          id="form-zipcode-edit-input"
          type="text"
          v-model="editForm.zipcode"
          required
          placeholder="Enter ZIP code"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="form-telephone-edit-group" label="Telephone:" label-for="form-telephone-edit-input">
        <b-form-input
          id="form-telephone-edit-input"
          type="text"
          v-model="editForm.telephone"
          required
          placeholder="Enter telephone"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Update</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
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
        firstname: '',
        lastname: '',
        street: '',
        city: '',
        state: '',
        zipcode: '',
        telephone: '',
      },
      editForm: {
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
    updateCustomer(payload, customerID) {
      const path = 'http://localhost:5000/customers/${customerID}';
      axios.put(path, payload)
        .then(() => {
          this.getCustomers();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCustomers();
        });
    },
    editCustomer(customer) {
      this.editForm = customer;
    },
    removeCustomer(customerID) {
      const path = 'http://localhost:5000/customers/${customerID}';
      axios.delete(path)
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
      this.addCustomerForm.firstname = '';
      this.addCustomerForm.lastname = '';
      this.addCustomerForm.street = '';
      this.addCustomerForm.city = '';
      this.addCustomerForm.state = '';
      this.addCustomerForm.zipcode = '';
      this.addCustomerForm.telephone = '';
      this.editForm.firstname = '';
      this.editForm.lastname = '';
      this.editForm.street = '';
      this.editForm.city = '';
      this.editForm.state = '';
      this.editForm.zipcode = '';
      this.editForm.telephone = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      const payload = {
        firstname: this.addCustomerForm.firstname,
        lastname: this.addCustomerForm.lastname,
        street: this.addCustomerForm.street,
        city: this.addCustomerForm.city,
        state: this.addCustomerForm.state,
        zipcode: this.addCustomerForm.zipcode,
        telephone: this.addCustomerForm.telephone,
      };
      this.addCustomer(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editCustomerModal.hide();
      const payload = {
        firstname: this.editForm.firstname,
        lastname: this.editForm.lastname,
        street: this.editForm.street,
        city: this.editForm.city,
        state: this.editForm.state,
        zipcode: this.editForm.zipcode,
        telephone: this.editForm.telephone,
      };
      this.updateCustomer(payload, this.editForm.customerid);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editCustomerModal.hide();
      this.initForm();
      this.getCustomers();
    },
    onDeleteCustomer(customer) {
      this.removeCustomer(customer.customerid);
    },
  },
  created() {
    this.getCustomers();
  },
};
</script>
