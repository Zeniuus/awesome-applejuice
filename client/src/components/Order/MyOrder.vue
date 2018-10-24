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
          <p class="input-msg error" :class="{ 'is-active': isEmptyOrderNumber }">주문번호를 입력해주세요!</p>
          <p class="input-msg error" :class="{ 'is-active': hasErrorOccurred }">해당하는 주문이 없습니다.</p>
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
      isEmptyOrderNumber: false,
      hasErrorOccurred: false,
      orders: [],
    };
  },
  methods: {
    hideError() {
      this.isEmptyOrderNumber = false;
      this.hasErrorOccurred = false;
    },
    async fetchMyOrder() {
      if (/^\s*$/.test(this.orderNumber)) {
        this.isEmptyOrderNumber = true;
        return;
      }

      let result;
      try {
        result = await this.$http.get(`${API_URL}/orders/${this.orderNumber}`);
      } catch (e) {
        const { status } = e.response;
        if (status === 400 || status === 404) {
          this.hasErrorOccurred = true;
        } else {
          alert(e.toString());
        }
        this.orders = [];
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
