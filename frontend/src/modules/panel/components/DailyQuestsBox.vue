<template>
  <div class="chart-container progressUser h-100">
          <DailyQuests delay=6000 />
    </div>
</template>

<script>
import DailyQuests from '@/components/Panel/components/DailyQuests.vue';
export default {
    components: {
        DailyQuests
    }
}
</script>

<style>

</style>