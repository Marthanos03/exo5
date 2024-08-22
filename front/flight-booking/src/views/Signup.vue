<template>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
      </nav>
      <h2>Signup</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="username">Username:</label>
          <input type="text" v-model="form.username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="text" v-model="form.password" required />
        </div>
        <div>
          <label for="role">Role:</label>
          <input type="text" v-model="form.role" required />
        </div>
        <button type="submit">Signup</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Signup',
    data() {
      return {
        form: {
          username: '',
          password: '',
          role: 'user',
        },
      };
    },
    methods: {
        async submitForm() {
            try {
                const response = await fetch('http://localhost:8000/signup/', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json',
                        "Access-Control-Allow-Origin": "*"
                    },
                    body: JSON.stringify(this.form),
                });
                if (response.ok) {
                    this.$router.push('/');
                } else {
                    console.error('Failed to signup');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
    },
  };
  </script>
  