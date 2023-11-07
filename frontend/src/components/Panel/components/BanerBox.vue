<template>
  <div class="baner">
            <router-link to="/panel" class="d-flex flex-row justify-content-center align-items-center">
                <div class="logo">
                    <img src="@/assets/icons/logo.png">
                </div>
                <div>
                    <span name="PageName">{{PageName}}</span>
                    <div name="type">Tryb:<span>dziecka</span></div>
                </div>
                
            </router-link>
        </div>
</template>

<script>
export default {
    name: "BanerBox",
    setup(){
        return {PageName: process.env.VUE_APP_SITE_TITLE || ''}
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
img
{
    width: 4em;
    height: 4em;
}
span
{
    color:var(--primary-color);
}
span[name="PageName"]
{
    font-size: 2em;
    font-weight: 700;
}
</style>