<template>
  <div id="app">
    <!--<div id="nav">-->
      <!--<router-link to="/">Home</router-link> |-->
    <!--</div>-->
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link class="navbar-item" :to="{ name: 'home' }">
          늘솔농원
        </router-link>
      </div>
      <div class="navbar-menu">
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
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
