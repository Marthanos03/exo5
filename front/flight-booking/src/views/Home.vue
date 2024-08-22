<template>
    <div>
      <router-link to="/signup">Signup</router-link>
      <router-link to="/login">Login</router-link>
      <br />
      <router-link to="/is_admin">Admin</router-link>
      <h1>Flight Bookings</h1>
      <router-link to="/add">Add a Booking</router-link>
    </div>
  </template>
  
  <script>
  
  export default {
    name: 'Home',
  };
  </script>
  