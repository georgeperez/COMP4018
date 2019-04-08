<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand href="/">MambaDB</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/customers">Customers</b-nav-item>
        <b-nav-item href="/businesses">Businesses</b-nav-item>
        <b-nav-item href="/products">Products</b-nav-item>
        <b-nav-item href="/orders">Orders</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
    <b-jumbotron bg-variant="light" type="light" header="MambaDB"
    lead="The world's most advanced inventory system, built for business owners.">
      <p>Sign up to learn more.</p>
      <b-button variant="primary" href="#">Sign up</b-button>
    </b-jumbotron>
  </div>
</template>
