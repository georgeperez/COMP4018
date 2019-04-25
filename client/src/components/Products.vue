<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Products</h1>
        <hr>
        <br>
        <br>
        <button type="button" class="btn btn-success btn-sm"
        v-b-modal.product-modal>Add Product</button>
        <br>
        <br>
        <table class="table table-hover responsive">
          <thead>
            <tr>
              <th scope="col">Product ID</th>
              <th scope="col">Product Label</th>
              <th scope="col">Category</th>
              <th scope="col">Quantity</th>
              <th scope="col">Business Name</th>
              <th scope="col">Manufacturer</th>
              <th scope="col">Model Number</th>
              <th scope="col">Serial Number</th>
              <th scope="col">SKU</th>
              <th scope="col">Buy Price</th>
              <th scope="col">MSRP</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(product, index) in products" :key="index">
              <td>{{ product.productid }}</td>
              <td>{{ product.productlabel }}</td>
              <td>{{ product.productcategory }}</td>
              <td>{{ product.quantity }}</td>
              <td>{{ product.businessname }}</td>
              <td>{{ product.manufacturer }}</td>
              <td>{{ product.modelnumber }}</td>
              <td>{{ product.serialnumber }}</td>
              <td>{{ product.sku }}</td>
              <td>{{ product.buyprice }}</td>
              <td>{{ product.msrp }}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addProductModal" id="product-modal" title="Add a new product" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-productid-group" label="ID:" label-for="form-productid-input">
          <b-form-input
            id="form-productid-input"
            type="text"
            v-model="addProductForm.productid"
            required
            placeholder="Enter product ID"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-productlabel-group" label="Label:"
        label-for="form-productlabel-input">
          <b-form-input
            id="form-productlabel-input"
            type="text"
            v-model="addProductForm.productlabel"
            required
            placeholder="Enter label"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-productcategory-group" label="Category:"
        label-for="form-productcategory-input">
          <b-form-input
            id="form-productcategory-input"
            type="text"
            v-model="addProductForm.productcategory"
            required
            placeholder="Enter category"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-quantity-group" label="Quantity:" label-for="form-quantity-input">
          <b-form-input
            id="form-quantity-input"
            type="text"
            v-model="addProductForm.quantity"
            required
            placeholder="Enter quantity"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-businessname-group" label="Business Name:"
        label-for="form-businessname-input">
          <b-form-input
            id="form-businessname-input"
            type="text"
            v-model="addProductForm.businessname"
            required
            placeholder="Enter business name"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-manufacturer-group" label="Manufacturer:"
        label-for="form-manufacturer-input">
          <b-form-input
            id="form-manufacturer-input"
            type="text"
            v-model="addProductForm.manufacturer"
            required
            placeholder="Enter manufacturer"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-modelnumber-group" label="Model Number:"
        label-for="form-modelnumber-input">
          <b-form-input
            id="form-modelnumber-input"
            type="text"
            v-model="addProductForm.modelnumber"
            required
            placeholder="Enter model number"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-serialnumber-group" label="Type:"
        label-for="form-serialnumber-input">
          <b-form-input
            id="form-serialnumber-input"
            type="text"
            v-model="addProductForm.serialnumber"
            required
            placeholder="Enter serial number"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-sku-group" label="SKU:" label-for="form-sku-input">
          <b-form-input
            id="form-sku-input"
            type="text"
            v-model="addProductForm.sku"
            required
            placeholder="Enter SKU"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-buyprice-group" label="Buy Price:" label-for="form-buyprice-input">
          <b-form-input
            id="form-buyprice-input"
            type="text"
            v-model="addProductForm.buyprice"
            required
            placeholder="Enter buy price"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="form-msrp-group" label="MSRP:" label-for="form-msrp-input">
          <b-form-input
            id="form-msrp-input"
            type="text"
            v-model="addProductForm.msrp"
            required
            placeholder="Enter MSRP"
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
      products: [],
      addProductForm: {
        productid: '',
        productlabel: '',
        productcategory: '',
        quantity: '',
        businessname: '',
        manufacturer: '',
        modelnumber: '',
        serialnumber: '',
        sku: '',
        buyprice: '',
        msrp: '',
      },
    };
  },
  methods: {
    getProducts() {
      const path = 'http://localhost:5000/products';
      axios.get(path)
        .then((res) => {
          this.products = res.data.products;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addProduct(payload) {
      const path = 'http://localhost:5000/products';
      axios.post(path, payload)
        .then(() => {
          this.getProducts();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getProducts();
        });
    },
    initForm() {
      this.addProductForm.productid = '';
      this.addProductForm.productlabel = '';
      this.addProductForm.productcategory = '';
      this.addProductForm.quantity = '';
      this.addProductForm.businessname = '';
      this.addProductForm.modelnumber = '';
      this.addProductForm.serialnumber = '';
      this.addProductForm.sku = '';
      this.addProductForm.buyprice = '';
      this.addProductForm.msrp = '';
      this.editForm.productid = '';
      this.editForm.productlabel = '';
      this.editForm.productcategory = '';
      this.editForm.quantity = '';
      this.editForm.businessname = '';
      this.editForm.modelnumber = '';
      this.editForm.serialnumber = '';
      this.editForm.sku = '';
      this.editForm.buyprice = '';
      this.editForm.msrp = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addProductModal.hide();
      const payload = {
        productid: this.addProductForm.productid,
        productlabel: this.addProductForm.productlabel,
        productcategory: this.addProductForm.productcategory,
        quantity: this.addProductForm.quantity,
        businessname: this.addProductForm.businessname,
        modelnumber: this.addProductForm.modelnumber,
        serialnumber: this.addProductForm.serialnumber,
        sku: this.addProductForm.sku,
        buyprice: this.addProductForm.buyprice,
        msrp: this.addProductForm.msrp,
      };
      this.addProduct(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editProductModal.hide();
      const payload = {
        productid: this.editForm.productid,
        productlabel: this.editForm.productlabel,
        productcategory: this.editForm.productcategory,
        quantity: this.editForm.quantity,
        businessname: this.editForm.businessname,
        modelnumber: this.editForm.modelnumber,
        serialnumber: this.editForm.serialnumber,
        sku: this.editForm.sku,
        buyprice: this.editForm.buyprice,
        msrp: this.editForm.msrp,
      };
      this.addProduct(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addProductModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getProducts();
  },
};
</script>
