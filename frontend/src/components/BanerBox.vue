<template>
  <div class="baner d-flex flex-column justify-content-center align-items-center">
            <div class="logo">
                <span>{{PageName}}</span>
            </div>
            <div>Tryb:<span>dziecka</span></div>
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

<style>
.baner
{
    font-size: 'ST-Tokyo hieroglyphic';
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
</style>