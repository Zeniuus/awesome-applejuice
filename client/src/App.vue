<template>
  <div id="app">
    <navbar v-if="shouldNavbarShown" />
    <div id="page-root" class="container">
      <div class="columns">
        <div class="column is-one-fifth-widescreen is-one-quarter is-desktop"
             v-if="shouldAdShown">
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
import Advertisement from './components/common/Advertisement';
import Navbar from './components/common/Navbar';

export default {
  name: 'app',
  computed: {
    shouldNavbarShown() {
      // const NAVBAR_VIEWS = [
      //   'home',
      //   'rural-life',
      //   'apple-story',
      //   'qna',
      //   'order',
      // ];
      const NO_NAVBAR_VIEWS = [
        'signin',
      ];
      return !NO_NAVBAR_VIEWS.includes(this.$route.name);
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
  beforeCreate() {
    /*
     * We cannot use mapMutations for initializeAuth mutation
     * because vue instance is not initialized in beforeCreate hook.
     */
    this.$store.commit('initializeAuth');
  },
  components: {
    Navbar,
    Advertisement,
  },
};
</script>

<style lang="scss" scoped>
@import './main';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  #page-root {
    padding-top: $navbar-height + 2rem;
  }
}
</style>
