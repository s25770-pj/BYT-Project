<template>
  <div>
    <highcharts :options="chartOptions" @callback="chartCallback = $event"></highcharts>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import Highcharts from 'highcharts';


export default {
  props: {
    chartOptions: Object,
  },
  setup() {
    const chartCallback = ref(null);
    Highcharts.wrap(Highcharts.Chart.prototype, 'isInsidePlot', function () {
    return true;
    });
    const updateChart = () => {
      const chart = chartCallback.value;

      if (chart && chart.container) {
        const container = chart.container.parentNode;
        chart.setSize(container.clientWidth, container.clientHeight);
      }
    };

    onMounted(() => {
      updateChart();
    });

    onBeforeUnmount(() => {
      window.removeEventListener('resize', updateChart);
    });

    return {
      chartCallback,
    };
  },
};
</script>
