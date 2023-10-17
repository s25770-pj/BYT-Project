<template>
  <div class="navbar">
    
    <div class="menu d-flex flex-row justify-content-center align-items-center">
        <router-link to="/panel"><BanerBox /></router-link>
        <MainNav lang="pl" nav="user"/>
    </div>
  </div>
</template>

<script>
import MainNav from './MainNav.vue';
import BanerBox from './BanerBox.vue';

export default {
  components:{
    BanerBox,
    MainNav
  }
};
</script>

<style scoped>
:root
{
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.menu {
  background: linear-gradient(to bottom, rgb(241 235 235 / 58%), rgb(241 235 235 / 49%));
  color: #333;
  width: 15%;
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
}
.menu > div > div
{
  width: 80%;
}
.menu > div
{
  width: 80%;
}
.menu > div{
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  justify-content: center;
}
ul {
  list-style-type: none;
  padding: 0;
}

ul li {
  padding: 20px 0;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: background-color 0.2s;
}

ul li a {
  text-decoration: none;
  font-size: 18px;
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: space-between;
  color: #333;
}

ul li a .icon {
  margin-right: 10px;
  font-size: 24px;
}

ul li:hover {
  background-color: #eee;
}

ul li a:hover {
  color: #ffd700;
}
</style>
