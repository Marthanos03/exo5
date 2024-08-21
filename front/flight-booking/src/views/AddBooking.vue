<template>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
      </nav>
      <h2>Add a Booking</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="passengerName">Passenger Name:</label>
          <input type="text" v-model="form.passengerName" required />
        </div>
        <div>
          <label for="flightNumber">Flight Number:</label>
          <input type="text" v-model="form.flightNumber" required />
        </div>
        <div>
          <label for="departure">Departure:</label>
          <input type="text" v-model="form.departure" required />
        </div>
        <div>
          <label for="destination">Destination:</label>
          <input type="text" v-model="form.destination" required />
        </div>
        <div>
          <label for="date">Date:</label>
          <input type="datetime-local" v-model="form.date" required />
        </div>
        <button type="submit">Add Booking</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AddBooking',
    data() {
      return {
        form: {
          passengerName: '',
          flightNumber: '',
          departure: '',
          destination: '',
          date: '',
        },
      };
    },
    methods: {
        convertToISO(dateString) {
            const date = new Date(dateString);
            return date.toISOString();
        },
        async submitForm() {
            try {
                const isoDate = this.convertToISO(this.form.date);
                const data = {
                    passenger_name: this.form.passengerName,
                    flight_number: this.form.flightNumber,
                    departure: this.form.departure,
                    destination:  this.form.destination,
                    date: isoDate,
                };
                const response = await fetch('http://localhost:8000/booking/', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json',},
                    body: JSON.stringify(data),
                });
                if (response.ok) {
                    this.$router.push('/');
                } else {
                    console.error('Failed to add booking');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
    },
  };
  </script>
  