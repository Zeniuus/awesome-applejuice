<template>
  <div id="app">
    <navbar v-if="shouldNavbarShown" />
    <div class="container">
      <div class="columns">
        <div class="column is-one-quarter" v-if="shouldAdShown">
          <advertisement />
        </div>
        <div class="column">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Advertisement from './components/Advertisement';
import Navbar from './components/Navbar';

export default {
  name: 'app',
  computed: {
    shouldNavbarShown() {
      const NAVBAR_VIEWS = [
        'home',
        'rural-life',
        'apple-story',
        'qna',
        'order',
      ];
      return NAVBAR_VIEWS.includes(this.$route.name);
    },
    shouldAdShown() {
      const AD_VIEWS = [
        'home',
        'rural-life',
        'apple-story',
        'qna',
      ];
      return AD_VIEWS.includes(this.$route.name);
    },
  },
  components: {
    Navbar,
    Advertisement,
  },
};
</script>

<style lang="scss" scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
