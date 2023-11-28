<template>
  <div class="not-found-page">
    <div class="not-found-content">
        <h1 class="animation">
          <span class="glitch-animation">4</span>
          <span class="glitch-animation" style="animation-delay:.5s">0</span>
          <span class="glitch-animation" style="animation-delay:1s">4</span>
        </h1>
      <div>
        <p>Przepraszamy, ale strona, której szukasz, nie istnieje.</p>
        <router-link to="/" class="back-link">Powrót do strony głównej</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotFoundPage",
};
</script>

<style scoped>
.not-found-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, var(--primary-color), var(--second-color));
  position: relative;
}

.not-found-content {
  text-align: center;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  animation: fadeIn 1s ease-in-out;
  position: relative;
  z-index: 2;
}

h1 {
  font-size: 4em;
  margin-bottom: 20px;
  color: #333;
  display: inline;
}

.back-link {
  text-decoration: none;
  background: #e74c3c;
  color: #fff;
  padding: 15px 30px;
  border-radius: 4px;
  font-weight: bold;
  transition: background 0.3s;
  text-transform: uppercase;
}

.back-link:hover {
  background: #c0392b;
}
.animation
{
  padding: 5%;
  display: flex;
  width: 50%;
  margin:auto;
  justify-content: space-around;
}
.glitch-animation {
  animation: glitch 1s infinite alternate;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes glitch {
  0% {
    transform: translateY(0);
    opacity: 1;
  }
  10% {
    transform: translateY(-5px);
    opacity: 0.8;
  }
  20% {
    transform: translateY(5px);
    opacity: 0.8;
  }
  30% {
    transform: translateY(-2px);
    opacity: 0.7;
  }
  40% {
    transform: translateY(2px);
    opacity: 0.7;
  }
  50% {
    transform: translateY(0);
    opacity: 0.6;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>
