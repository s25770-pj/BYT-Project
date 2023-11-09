<template>
  <div class="baner" :style="style">
            <router-link to="/panel" class="d-flex flex-row justify-content-center align-items-center">
                
                <div class="logo">
                    <img src="@/assets/icons/logo.png">
                    <div name="type" v-if="showMode">Tryb: <span>dziecka</span></div>
                </div>
                
            </router-link>
        </div>
</template>

<script>
export default {
    name: "BanerBox",
    props:{
        style:{type:Object},
        showMode:{
            type:Boolean,
            default: ()=>true
        }
    }
}
</script>

<style scoped>
.baner
{
    font-size: var(--font-family);
    position: absolute;
    top:5%;
}
.logo{
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    flex-direction: column;
}
img
{
    height: 100%;
    width: 90%;
}
span
{
    color:var(--primary-color);
}
div[name="type"]
{
    font-size: 1em;
    font-weight: 700;
    text-align: center;
}
</style>