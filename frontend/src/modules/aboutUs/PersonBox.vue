<template>
  <div class="person-box card mb-3">
    <div class="row no-gutters">
      <div class="col-md-6 col-sm-12">
        <img
          v-if="person.photo"
          :src="images[person.photo]"
          :alt="person.name"
          class="card-img"
        />
      </div>
      <div class="col-sm-12" :class="{ 'col-md-6': person.photo }">
        <div class="card-body">
          <h2 class="card-title">{{ person.name }} {{ person.surname }}</h2>
          <div v-if="person.photo" class="card-text">{{ person.role }}</div>
          <div v-else>
            <p class="card-text">{{ person.role }}</p>
          </div>
          <div class="additional-info">
            <div v-for="(value, key) in person.info" :key="key">
              <template v-if="key === 'link'">
                <ul class="link-list">
                  <li v-for="(link, linkKey) in value" :key="linkKey">
                    <p>
                      {{ linkKey }}:<a :href="link.href" target="_blank">
                        {{ link.text }}</a
                      >
                    </p>
                  </li>
                </ul>
              </template>
              <template v-else-if="key === 'list'">
                <p>{{ key }}:</p>
                <ul class="custom-list">
                  <li v-for="(item, itemKey) in value" :key="itemKey">
                    {{ itemKey }}: {{ item }}
                  </li>
                </ul>
              </template>
              <template v-else-if="typeof value === 'string'">
                <p>{{ key }}: {{ value }}</p>
              </template>
              <template v-else-if="Array.isArray(value)">
                <p>{{ key }}: {{ value.join(", ") }}</p>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const requireImage = require.context("@/assets/images/teams", false, /\.png$/);
const images = {};

export default {
  props: {
    person: Object,
  },
  setup() {
    requireImage.keys().forEach((fileImage) => {
      const iconName = fileImage.replace(/^\.\/(.*)\.\w+$/, "$1");
      images[iconName] = requireImage(fileImage);
    });

    return { images };
  },
};
</script>

<style scoped>
.person-box {
  max-width: 48%;
  margin-right: 2%;
  margin-bottom: 2rem;
  font-size: 1em;
  min-width: 16%;
  aspect-ratio: 16/9;
}
.card-title {
  font-size: 1.1em;
}
.card-img {
  aspect-ratio: 16/9;
  max-width: 100%;
  height: 100%;
  background-color: gray;
}

.additional-info {
  margin-top: 1rem;
  font-size: 0.9em;
}

.link-list {
  list-style-type: none;
  padding: 0;
}

.link-list li {
  margin-bottom: 5px;
}

.link-list a {
  text-decoration: none;
  color: #800080;
}

.link-list a:hover {
  text-decoration: underline;
}

.custom-list {
  list-style-type: disc;
  margin-left: 20px;
}

.custom-list li {
  margin-bottom: 5px;
  color: #800080;
}

@media (max-width: 767px) {
  .person-box {
    max-width: 100%;
    margin-right: 0;
  }

  .person-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>
