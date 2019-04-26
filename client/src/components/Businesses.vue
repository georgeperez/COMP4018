<template>
  <div class="container">
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/customers">Customers</b-nav-item>
        <b-nav-item href="/businesses">Businesses</b-nav-item>
        <b-nav-item href="/products">Products</b-nav-item>
        <b-nav-item href="/orders">Orders</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
    <div class="row">
      <div class="col-sm-10">
        <h1>Businesses</h1>
        <hr>
        <br>
        <br>
        <button type="button" class="btn btn-success btn-sm"
        v-b-modal.business-modal>Add Business</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Business Name</th>
              <th scope="col">DUNS</th>
              <th scope="col">Street</th>
              <th scope="col">City</th>
              <th scope="col">State</th>
              <th scope="col">ZIP Code</th>
              <th scope="col">Type</th>
              <th scope="col">Number of Customers</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(business, index) in businesses" :key="index">
              <td>{{ business.businessname }}</td>
              <td>{{ business.duns }}</td>
              <td>{{ business.street }}</td>
              <td>{{ business.city }}</td>
              <td>{{ business.state }}</td>
              <td>{{ business.zipcode }}</td>
              <td>{{ business.type }}</td>
              <td>{{ business.numbercustomers }}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBusinessModal" id="business-modal" title="Add a new business" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-businessname-group" label="Name:"
        label-for="form-businessname-input">
          <b-form-input
            id="form-businessname-input"
            type="text"
            v-model="addBusinessForm.businessname"
            required
            placeholder="Enter name"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-duns-group" label="DUNS:" label-for="form-duns-input">
          <b-form-input
            id="form-duns-input"
            type="text"
            v-model="addBusinessForm.duns"
            required
            placeholder="Enter DUNS"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-street-group" label="Street:" label-for="form-street-input">
          <b-form-input
            id="form-street-input"
            type="text"
            v-model="addBusinessForm.street"
            required
            placeholder="Enter street"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-city-group" label="City:" label-for="form-city-input">
          <b-form-input
            id="form-city-input"
            type="text"
            v-model="addBusinessForm.city"
            required
            placeholder="Enter city"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-state-group" label="State:" label-for="form-state-input">
          <b-form-input
            id="form-state-input"
            type="text"
            v-model="addBusinessForm.state"
            required
            placeholder="Enter state"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-zipcode-group" label="ZIP Code:" label-for="form-zipcode-input">
          <b-form-input
            id="form-zipcode-input"
            type="text"
            v-model="addBusinessForm.zipcode"
            required
            placeholder="Enter ZIP code"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-telephone-group" label="Telephone:" label-for="form-telephone-input">
          <b-form-input
            id="form-telephone-input"
            type="text"
            v-model="addBusinessForm.telephone"
            required
            placeholder="Enter telephone"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-type-group" label="Type:" label-for="form-type-input">
          <b-form-input
            id="form-type-input"
            type="text"
            v-model="addBusinessForm.type"
            required
            placeholder="Enter business type"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-numbercustomers-group" label="Number customers:"
        label-for="form-numbercustomers-input">
          <b-form-input
            id="form-numbercustomers-input"
            type="text"
            v-model="addBusinessForm.numbercustomers"
            required
            placeholder="Enter number of customers"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editBusinessModal" id="business-update-modal" title="Update a new business" hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-businessname-edit-group" label="Name:"
        label-for="form-businessname-edit-input">
          <b-form-input
            id="form-businessname-edit-input"
            type="text"
            v-model="editForm.businessname"
            required
            placeholder="Enter name"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-duns-edit-group" label="DUNS:" label-for="form-duns-edit-input">
          <b-form-input
            id="form-duns-input"
            type="text"
            v-model="editForm.duns"
            required
            placeholder="Enter DUNS"
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
        <b-form-group id="form-type-edit-group" label="Type:" label-for="form-type-edit-input">
          <b-form-input
            id="form-type-edit-input"
            type="text"
            v-model="editForm.type"
            required
            placeholder="Enter business type"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-numbercustomers-edit-group" label="Number customers:"
        label-for="form-numbercustomers-edit-input">
          <b-form-input
            id="form-numbercustomers-edit-input"
            type="text"
            v-model="editForm.numbercustomers"
            required
            placeholder="Enter number of customers"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
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
      businesses: [],
      addBusinessForm: {
        name: '',
        duns: '',
        street: '',
        city: '',
        state: '',
        zipcode: '',
        type: '',
        numbercustomers: '',
      },
    };
  },
  methods: {
    getBusinesses() {
      const path = 'http://localhost:5000/businesses';
      axios.get(path)
        .then((res) => {
          this.businesses = res.data.businesses;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBusiness(payload) {
      const path = 'http://localhost:5000/businesses';
      axios.post(path, payload)
        .then(() => {
          this.getBusinesses();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBusinesses();
        });
    },
    updateBusiness(payload, customerID) {
      const path = 'http://localhost:5000/businesses/${customerID}';
      axios.put(path, payload)
        .then(() => {
          this.getBusinesses();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBusinesses();
        });
    },
    editBusiness(business) {
      this.editForm = business;
    },
    removeBusiness(businessID) {
      const path = 'http://localhost:5000/businesses/${businessID}';
      axios.delete(path)
        .then(() => {
          this.getBusinesses();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBusinesses();
        });
    },
    initForm() {
      this.addBusinessForm.businessname = '';
      this.addBusinessForm.duns = '';
      this.addBusinessForm.street = '';
      this.addBusinessForm.city = '';
      this.addBusinessForm.state = '';
      this.addBusinessForm.zipcode = '';
      this.addBusinessForm.telephone = '';
      this.addBusinessForm.type = '';
      this.addBusinessForm.numbercustomers = '';
      this.editForm.businessname = '';
      this.editForm.duns = '';
      this.editForm.street = '';
      this.editForm.city = '';
      this.editForm.state = '';
      this.editForm.zipcode = '';
      this.editForm.telephone = '';
      this.editForm.type = '';
      this.editForm.numbercustomers = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBusinessModal.hide();
      const payload = {
        businessname: this.addBusinessForm.businessname,
        duns: this.addBusinessForm.duns,
        street: this.addBusinessForm.street,
        city: this.addBusinessForm.city,
        state: this.addBusinessForm.state,
        zipcode: this.addBusinessForm.zipcode,
        telephone: this.addBusinessForm.telephone,
        type: this.addBusinessForm.type,
        numbercustomers: this.addBusinessForm.numbercustomers,
      };
      this.addBusiness(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.updateBusinessModal.hide();
      const payload = {
        businessname: this.editForm.businessname,
        duns: this.editForm.duns,
        street: this.editForm.street,
        city: this.editForm.city,
        state: this.editForm.state,
        zipcode: this.editForm.zipcode,
        telephone: this.editForm.telephone,
        type: this.editForm.type,
        numbercustomers: this.editForm.numbercustomers,
      };
      this.updateBusiness(payload, this.editForm.businessid)
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBusinessModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBusinessModal.hide();
      this.initForm();
      this.getBusinesses();
    },
    onDeleteBusiness(business) {
      this.removeBusiness(business.businessid);
    },
  },
  created() {
    this.getBusinesses();
  },
};
</script>
