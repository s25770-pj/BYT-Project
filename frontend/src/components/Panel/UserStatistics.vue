<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-9">
        <div class="main-panel">
          <div class="row">
            <div class="col-md-12 col-sm-6">
              <HighchartsChart :chartOptions="chartOptions" class="chart" />
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3 userData">
        <div class="chart-container progressUser">
           <DailyChest />
        </div>
        <div class="chart-container progressUser">
          <DailyQuests delay=6000 />
        </div>
        <div class="chart-container progressUser">
            <ProgressBar/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProgressBar from '@/components/Panel/components/ProgressBar.vue';
import DailyQuests from '@/components/Panel/components/DailyQuests.vue';
import HighchartsChart from '@/components/ChartHighcharts.vue';
import DailyChest from '@/components/Panel/components/DailyChest.vue';

import { ref} from 'vue';


export default {
  components: {
    ProgressBar,
    DailyQuests,
    HighchartsChart,
    DailyChest
  },
  setup() {
    const date = ref(new Date().getDate()+3);
    const chartOptions = ref({
      chart: {
        type: 'spline',
        width: null,
        height: null,
      },
      title: {
        text: 'Twój progres',
      },
      xAxis: {
        categories: Array.from({ length: date.value }, (_, index) => index + 1),
      },
      yAxis: {
        title: {
          text: 'Wartość',
        },
      },
      plotOptions: {
        series: {
          showCheckbox: false,
        },
      },
      series: [
        {
          name: 'Twój progres',
          data: Array.from({ length: date.value }, () => (Math.round(Math.random() * 100 * 100) / 100))
        },
        {
          name: 'Średni progres użytkowników',
          data: Array.from({ length: date.value }, () => (Math.round(Math.random() * 100 * 100) / 100))
        },
      ],
      accessibility: {
        enabled: false,
      },
    });

    const dailyView = ref(false); 


    const toggleView = () => {
      dailyView.value = !dailyView.value;
    };

    return {
      chartOptions,
      toggleView,
      dailyView,
    };
  },
};
</script>
<style scoped>
.main-panel {
  display: flex;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  height: 75vh;
}
.static-container {
  display: flex;
  flex-direction: column;
}
.chart-container {
  display: flex;
  flex-direction: column;
  min-width: 100%;
  height: 30%;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.container-fluid,.row
{
  min-height: 70vh;
}
.userData
{
  min-height: 100%;
  display: flex;
  align-content: center;
  flex-direction: column;
  justify-content: space-between;
}
.chart{
  aspect-ratio: 16/9;
  min-height: 50%;
}
.main-panel.row
{
  align-content: center;
}
.col-md-8
{
  height: 50%;
}
</style>
