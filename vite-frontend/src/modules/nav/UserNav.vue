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
              fontSize: "var(--font-size-btn)",
              width: '85%',
              textTransform: 'uppercase',
              fontWeight: '700',
              padding: '10px',
              borderRadius:'var(--border-radius-btn)',
              background: 'var(--bg-btn-mNav)',
              backgroundPosition: 'right',
              transition: "all 1s",
            },
            hover:{
              backgroundPosition: 'left',
            }
          },
          img:{
            normal:{
              width: "var(--img-width)",
              height: "var(--img-height)"
            }
          }
        },
        containerMenu:{
          minWidth:"50%",
          maxWidth:"90%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
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
  width: var(--menu-size);
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  transition: width 1s;
}
.navbar
{
  width:90%;
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
}

</style>
