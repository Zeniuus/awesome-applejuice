<template>
  <nav id="navbar" class="navbar" role="navigation" aria-label="main navigation">
    <div class="container">
      <div class="navbar-brand">
        <router-link class="navbar-item" :to="{ name: 'home' }">
          늘솔농원
        </router-link>
        <a role="button" class="navbar-burger" :class="{ 'is-active': isMenuActive }"
           @click="toggleBurgerMenu" aria-label="menu" aria-expanded="false">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" :class="{ 'is-active': isMenuActive }">
        <div class="navbar-start">
          <router-link class="navbar-item" :to="{ name: 'rural-life' }">
            귀농인의 삶
          </router-link>
          <router-link class="navbar-item" :to="{ name: 'apple-story' }">
            사과 이야기
          </router-link>
          <router-link class="navbar-item" :to="{ name: 'qna' }">
            질문 및 응답
          </router-link>
          <router-link class="navbar-item" :to="{ name: 'buy' }">
            구매하기
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      isMenuActive: false,
    };
  },
  methods: {
    toggleBurgerMenu() {
      this.isMenuActive = !this.isMenuActive;
    },
  },
};
</script>

<style lang="scss" scoped>
@import '~bulma/bulma';

#navbar {
  padding: 1.25rem;
  border-bottom-color: $navbar-box-shadow-color;
  border-width: $navbar-box-shadow-size;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
        color: #42b983;
    }
  }
}
</style>
