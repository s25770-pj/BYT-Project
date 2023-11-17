<template>
  <div class="navbar">
      <div class="menu d-flex flex-row justify-content-center align-items-center align-content-center flex-wrap">
          <BanerBox />
          <MainNav lang="pl" nav="user" :baseStyle="baseStyle" class="navbar" :textShow="textShow" :containerMenu="containerMenu"/>
      </div>
    </div>
</template>

<script>
import MainNav from './MainNav.vue';
import BanerBox from '@/components/Panel/components/BanerBox.vue';

export default {
  components:{
    BanerBox,
    MainNav
  },
  props:{
    textShow:{
      type:Boolean
    }
  },
  setup(){
    return {
        baseStyle:{
          btn:{
            normal:{
              width: '100%',
              textTransform: 'uppercase',
              fontWeight: '700',
              fontSize: '1.2em',
              padding: '10px',
              borderRadius:'var(--border-radius-btn)',
              transition: 'all .5s ease-in-out',
              background: 'var(--bg-btn-mNav)',
              backgroundPosition: 'right',
            },
            hover:{
              backgroundPosition: 'left',
            }
          },
          img:{
            normal:{
              width: '2em',
              height: '2em'
            }
          }
        },
        containerMenu:{
          minWidth:"50%",
          maxWidth:"90%"
        }
      }
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
  width: 15%;
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
}
.navbar
{
  width:90%;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
