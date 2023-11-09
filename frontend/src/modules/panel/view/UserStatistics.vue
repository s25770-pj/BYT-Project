<template>

  <div class="leout-3x3">

    <main-panel class="main"/>
    <Highcharts-chart-box class="chart"/>
    <Daily-quests-box class="chest"/>
    <Progress-bar-box class="progress"/>

  </div>
  
</template>

<script>

import DailyQuestsBox from '../components/DailyQuestsBox.vue';
import HighchartsChartBox from '../components/HighchartsChartBox.vue';
import MainPanel from '../components/MainPanel.vue';
import ProgressBarBox from '../components/ProgressBarBox.vue';

export default {
  components: {
    DailyQuestsBox,HighchartsChartBox,MainPanel,ProgressBarBox
  },
};

</script>
<style scoped>

.leout-3x3 > div {
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.main {
  grid-area: main;
}
.chest {
  grid-area: chest;
}
.progress {
  grid-area: progress;
}
.chart {
  grid-area: chart;
}

</style>
