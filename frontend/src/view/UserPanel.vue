<template>
  <div>
    
    <ProgressUser />
    
    <UserNav lang="pl" nav="user" />
    <PanelModul />
    <MainFooter/>

  </div>
  
</template>

<script>
import PanelModul from '@/modules/panel/MainPanel.vue';

import MainFooter from '@/components/Helpful/Footer/MainFooter.vue';
import UserNav from '@/components/CreateNav/UserNav.vue';
import ProgressUser from '@/components/Panel/components/ProgressUser.vue';
export default {
    name: 'UserPanel',
    components:{
        PanelModul,
        MainFooter,
        UserNav,
        ProgressUser
    }
}
</script>