<template>
  <div id="app">
    <navbar />
    <div class="container">
      <div class="columns">
        <div class="column is-one-quarter">
          <advertisement />
        </div>
        <div class="column">
          <router-view/>
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
