<template>
  <footer class="footer w-100">
    <div class="container">
      <div class="row">
        <div class="col-md-6 text-md-end">
          <p>&copy; {{ currentYear }} {{ pageTitle }}</p>
        </div>
        <div class="col-md-6 text-md-end">
          <MainNav lang="pl" nav="footer" />
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import MainNav from '@/components/MainNav.vue';
export default {
  name: 'MainFooter',
  components:{
    MainNav,
  },
  setup() {
    return {
      currentYear: new Date().getFullYear(),
      pageTitle: process.env.VUE_APP_SITE_TITLE || ''
    };
  },
};
</script>
<style>
:root{
  --color:#000444;
}
</style>
<style scoped>
.footer {
  font-size: 1.1em;
  color: var(--color);
  padding: 20px 0; 
  position: fixed;
  bottom: 0;
  background-color: transparent;
  border:none;
}

.footer-link {
  color: var(--color);
  border:none;
  margin-right: 20px;
  text-decoration: none;
  position: relative;
  transition: color 0.3s ease-in-out; 
}

.footer-link::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: -10px; 
  width: 0;
  height: 2px; 
  background-color: var(--background); 
  transition: width 0.3s ease-in-out; 
}

.footer-link:hover {
  color: var(--color-dark); 
}

.footer-link:hover::before {
  width: 100%;
}

@media (max-width: 575.98px) {
  .footer .row {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .footer .col-md-6.text-md-end {
    text-align: center;
    margin-top: 10px;
  }
}
</style>