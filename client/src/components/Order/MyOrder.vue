<template>
  <div>
    <h6 class="subtitle is-6">주문하셨을 때 받으신 주문번호를 입력해주세요.</h6>
    <div class="form-wrapper">
      <horizontal-input-field width="20rem">
        <label slot="label" class="label" for="order-number">주문번호</label>
        <div slot="input" class="input-wrapper">
          <input slot="input" id="order-number" class="input"
                 type="text" v-model="orderNumber"
                 @input="hideError" @keypress.enter="fetchMyOrder" />
          <p class="input-msg error" :class="{ 'is-active': errorMsg }">{{ errorMsg }}</p>
        </div>
      </horizontal-input-field>
    </div>
    <order-table :orders="orders" />
  </div>
</template>

<script>
import HorizontalInputField from '../common/HorizontalInputField';
import OrderTable from '../common/OrderTable';
import { API_URL } from '../../config';

export default {
  name: 'my-order',
  data() {
    return {
      orderNumber: '',
      errorMsg: '',
      orders: [],
    };
  },
  methods: {
    displayError(errorMsg) {
      this.errorMsg = errorMsg;
      this.orders = [];
    },
    hideError() {
      this.errorMsg = '';
    },
    async fetchMyOrder() {
      if (/^\s*$/.test(this.orderNumber)) {
        this.displayError('주문번호를 입력해주세요!');
        return;
      }

      let result;
      try {
        result = await this.$http.get(`${API_URL}/orders/${this.orderNumber}`);
      } catch (e) {
        if (!e.response) {
          this.displayError('알 수 없는 이유로 주문 조회에 실패했습니다.');
          return;
        }
        const { status } = e.response;
        if (status === 404) {
          this.displayError('해당하는 주문이 없습니다.');
        } else {
          this.displayError('알 수 없는 이유로 주문 조회에 실패했습니다.');
        }
        return;
      }
      this.orders = [result.data];
    },
  },
  components: {
    HorizontalInputField,
    OrderTable,
  },
};
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: inline-block;
  margin: 2rem 0 4rem;

  #order-number {
    width: 20rem;
  }

  .input-wrapper {
    position: relative;

    .input-msg {
      display: none;
      position: absolute;
      font-size: 0.9rem;
      margin-top: 0.25rem;

      &.error {
        color: red;
      }

      &.is-active {
        display: block;
      }
    }
  }
}
</style>
