<template>
  <div id="not-found-page-root">
    <div id="not-found-container">
      <h2 class="title">Oops! It's 404!</h2>
      <h5 class="subtitle">페이지가 발견되지 않았습니다.</h5>
      <router-link :to="{ name: 'home' }">홈으로</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'not-found',
};
</script>

<style lang="scss" scoped>
#not-found-page-root {
  position: relative;
  width: 100%;
  height: 90vh;

  #not-found-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    .subtitle {
      margin-top: 1.5rem;
    }
  }
}
</style>
