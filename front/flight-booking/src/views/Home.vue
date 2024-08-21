<template>
    <div>
      <h1>Flight Bookings</h1>
      <BookingList />
      <router-link to="/add">Add a Booking</router-link>
    </div>
  </template>
  
  <script>
  import BookingList from '../components/BookingList.vue';
  
  export default {
    name: 'Home',
    components: {
      BookingList,
    },
  };
  </script>
  