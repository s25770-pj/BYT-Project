<template>
  <div class="not-found-page">
    <h1>404 - Strona nie znaleziona</h1>
    <p>Przepraszamy, ale strona, której szukasz, nie istnieje.</p>
    <router-link to="/">Powrót do strony głównej</router-link>
  </div>
</template>

<script>
export default {
  name: "NotFoundPage",
};
</script>

<style scoped>
.not-found-page {
  text-align: center;
  margin-top: 20px;
}

h1 {
  font-size: 2em;
  margin-bottom: 10px;
}

p {
  font-size: 1.2em;
  margin-bottom: 20px;
}
</style>
