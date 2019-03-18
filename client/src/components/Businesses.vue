<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Businesses</h1>
        <hr>
        <br>
        <br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.business-modal>Add Business</button>
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
        <b-form-group id="form-businessname-group" label="Name:" label-for="form-businessname-input">
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
        <b-form-group id="form-numbercustomers-group" label="Number customers:" label-for="form-numbercustomers-input">
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
        state:'',
        zipcode:'',
        type:'',
        numbercustomers:'',
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
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBusinessModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBusinesses();
  },
};
</script>
