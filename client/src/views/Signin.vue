<template>
  <div class="signin-page-root">
    <div class="card signin-container">
      <div class="card-content">
        <h2 class="title">로그인</h2>
        <horizontal-input-field>
          <label slot="label" class="label" for="id">아이디</label>
          <input slot="input" id="id" class="input"
                 type="text" v-model="idInput"
                 @keypress.enter="signin" />
        </horizontal-input-field>
        <horizontal-input-field>
          <label slot="label" class="label" for="password">비밀번호</label>
          <input slot="input" id="password" class="input"
                 type="password" v-model="passwordInput"
                 @keypress.enter="signin" />
        </horizontal-input-field>
        <button type="button" class="button is-primary" @click="signin">로그인</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';

import HorizontalInputField from '../components/HorizontalInputField';
import { API_URL } from '../config';

export default {
  name: 'signin',
  data() {
    return {
      idInput: '',
      passwordInput: '',
    };
  },
  methods: {
    ...mapMutations([
      'stateSetter',
    ]),
    async signin() {
      let result;
      try {
        result = await this.$http.post(`${API_URL}/auth/signin`, {
          id: this.idInput,
          password: this.passwordInput,
        });
      } catch (e) {
        if (e.response.status === 401) {
          alert('잘못된 아이디 혹은 비밀번호 입니다!');
          return;
        }
      }

      /* Save user info in Vuex and localStorage. */
      const keys = ['id', 'nickname', 'jwt'];
      keys.map(field => ({
        field,
        value: result.data[field],
      })).forEach(this.stateSetter);
      keys.forEach((field) => {
        localStorage.setItem(field, result.data[field]);
      });

      this.$router.push({ name: 'home' });
    },
  },
  components: {
    HorizontalInputField,
  },
};
</script>

<style lang="scss" scoped>
.signin-page-root {
  position: relative;
  width: 100%;
  height: 90vh;

  .signin-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    /*max-width: 50rem;*/
    display: inline-block;
    margin: 0 auto;

    #id, #password {
      width: 20rem;
    }
  }
}
</style>
