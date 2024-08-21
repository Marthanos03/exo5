<template>
    <div>
      <h2>All Bookings</h2>
      <ul>
        <li v-for="booking in bookings" :key="booking.id">
          passenger {{ booking.passenger_name }} - flight {{ booking.flight_number }} - from {{ booking.departure }} - to {{ booking.destination }} - at {{ booking.date }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'BookingList',
    data() {
      return {
        bookings: [],
      };
    },
    async created() {
      try {
        const response = await fetch('http://localhost:8000/booking/', {
          headers: {
            "Access-Control-Allow-Origin": "*",
          }
        });
        this.bookings = await response.json();
      } catch (error) {
        console.error('Error fetching bookings:', error);
      }
    },
  };
  </script>
  