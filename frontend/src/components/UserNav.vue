<template>
  <div class="navbar">
    
    <div class="menu d-flex flex-row justify-content-center align-items-center">
        <div class="baner d-flex flex-column justify-content-center align-items-center">
            <div class="logo">EduPJWSTK</div>
            <div>Tryb:<span>dziecka</span></div>
        </div>
        <MainNav lang="pl" nav="user"/>
    </div>
  </div>
</template>

<script>
import MainNav from './MainNav.vue';

export default {
  components:{
    MainNav
  }
};
</script>

<style scoped>
:root
{
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.navbar {
  position: relative;
}
.baner
{
    position: absolute;
    width: 100%;
    height: 5%;
    top:5%;
}
.logo
{
    font-size: 2em;
    font-weight: 700;
}
.menu {
  background: linear-gradient(to bottom, rgb(241 235 235 / 58%), rgb(241 235 235 / 49%));
  color: #333;
  width: 200px;
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  overflow-y: auto; 
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
