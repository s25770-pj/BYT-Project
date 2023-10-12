<template>
  <div class="logPage login-container d-flex justify-content-center align-items-center">
      <div class="card">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Login</h2>
          <form @submit.prevent="login">
            <div class="mb-3">
              <label for="username" class="form-label">Username:</label>
              <input type="text" id="username" v-model="username" class="form-control" required />
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password:</label>
              <input type="password" id="password" v-model="password" class="form-control" required />
            </div>
            <div class="mb-3 d-flex align-items-center justify-content-between">
                <div>
                    <button type="submit" class="btn btn-primary btn-block">Log in</button>
                </div>
                <div>
                    <div>
                         <router-link to="/">Forgot Password?</router-link>
                    </div>
                   <div>
                    <router-link to="/register">I don't have a account</router-link>
                   </div>
                    
                </div>
            </div>
          </form>
           <div class="text-center mt-3">
          
        </div>
        </div>
      </div>
    <loginProgress :show="loading" :message="message" />
  </div>
</template>

<script>
import loginProgress from '@/components/LoginProgress.vue';
import { ref } from 'vue';

export default {
  name: "LoginPage",
  components: {
    loginProgress,
  },
  setup() {
    const loading = ref(false);
    const username = ref('');
    const password = ref('');
    const message = ref(''); 

    function login() {
      loading.value = true;
      console.log('Logowanie...');
      
      
      setTimeout(() => {
        loading.value = false; 
        message.value = 'Zalogowano pomyślnie!'; 
        console.log('Zalogowano pomyślnie!');
      }, 2000);
    }

    return {
      username,
      password,
      loading,
      login,
      message,
    };
  },
};
</script>


<style scoped>
.logPage
{
    background-image: url('@/assets/images/backgrounds/background-home.svg');
    background-size: cover;
}
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  width: 400px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 2rem;
}

.card-title {
  font-size: 1.5rem;
}

.form-label {
  font-weight: bold;
}

.btn {
  background-color: #3b39cb;
  border-color: #3b39cb;
}

.btn-primary {
  background-color: #3b39cb;
  border-color: #3b39cb;
}

.btn-primary:hover {
  background-color: #2c2aa7;
  border-color: #2c2aa7;
}
</style>
