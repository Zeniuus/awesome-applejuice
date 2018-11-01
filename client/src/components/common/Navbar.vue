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
          <router-link class="navbar-item" :to="{ name: 'order' }">
            주문하기
          </router-link>
          <router-link v-if="nickname" class="navbar-item" :to="{ name: 'manage' }">
            주문 관리
          </router-link>
        </div>
        <div class="navbar-end" v-show="isUserSignedIn">
          <div class="navbar-item">
            안녕하세요, {{ this.nickname }}님!
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Navbar',
  data() {
    return {
      isMenuActive: false,
    };
  },
  computed: {
    ...mapState([
      'nickname',
    ]),
    isUserSignedIn() {
      return !!this.nickname;
    },
  },
  methods: {
    toggleBurgerMenu() {
      this.isMenuActive = !this.isMenuActive;
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../../main';

#navbar {
  position: fixed;
  width: 100%;
  height: $navbar-height;
  padding: 0 1.25rem;
  border-bottom-color: $navbar-box-shadow-color;
  border-width: $navbar-box-shadow-size;
  box-shadow: 2px 2px 4px 0 #cccccc;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-active {
        color: #42b983;
    }
  }
}
</style>
