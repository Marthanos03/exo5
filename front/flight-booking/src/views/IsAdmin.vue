<template>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
      </nav>
      <h2>Login</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="username">Username:</label>
          <input type="text" v-model="form.username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="text" v-model="form.password" required />
        </div>
        <button type="submit">Check</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'IsAdmin',
    data() {
      return {
        form: {
          username: '',
          password: '',
        },
      };
    },
    methods: {
        async submitForm() {
            try {
                const response = await fetch('http://localhost:8000/is_admin/', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json',
                        "Access-Control-Allow-Origin": "*"
                    },
                    body: JSON.stringify(this.form),
                });
                if (response.ok) {
                    const userdata = await response.json()
                    if (userdata.is_admin == true)
                        this.$router.push('/admin');
                    else {
                        this.$router.push('/');
                    }
                } else {
                    console.error('Failed to check');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
    },
  };
  </script>
  