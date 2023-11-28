<template>
  <div class="aboutUs">
    <div class="container">
      <header class="page-header">
        <h1>Witaj na naszej innowacyjnej platformie naukowej!</h1>
        <p>Strona została utworzona w celach naukowych.</p>
        <p>
          <strong>Informacja ważna:</strong> Ta strona jest przeznaczona
          wyłącznie do celów pokazowych i nie jest oparta na żadnej konkretnej
          wiedzy naukowej. Zawarte treści są wyłącznie demonstracyjne, a my nie
          ponosimy odpowiedzialności za ich dokładność czy zastosowanie.
        </p>
      </header>
      <h1>Nasz zespół:</h1>
      <div class="row justify-content-center">
        <div class="col-md-6 person-list">
          <div class="row">
            <person-box
              v-for="(person, index) in people"
              :key="index"
              :person="person"
              :class="{ 'offset-md-3': index === people.length - 1 }"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PersonBox from "@/modules/aboutUs/PersonBox.vue";
import TeamData from "@/data/team.json";
import { ref } from "vue";

export default {
  components: {
    PersonBox,
  },
  setup() {
    const people = ref(TeamData);

    return {
      people,
    };
  },
};
</script>

<style scoped>
.person-list {
  width: 80%;
}

.row.no-gutters .person-box {
  flex: 0 0 48%;
  margin-right: 2%;
  margin-bottom: 2rem;
}

@media (max-width: 900px) {
  .row.no-gutters .person-box {
    flex: 0 0 100%;
    margin-right: 0;
  }
}

.page-header {
  color: #494949;
  text-align: center;
  padding: 20px;
}
</style>
