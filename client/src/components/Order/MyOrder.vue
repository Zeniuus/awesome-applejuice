<template>
  <div>
    <h4 class="subtitle">주문하셨을 때 받으신 주문번호를 입력해주세요.</h4>
    <div class="form-wrapper">
      <horizontal-input-field width="20rem">
        <label slot="label" class="label" for="order-number">주문번호</label>
        <div slot="input" class="input-wrapper">
          <input slot="input" id="order-number" class="input"
                 type="text" v-model="orderNumber"
                 @input="hideError" @keypress.enter="fetchMyOrder" />
          <p class="input-msg error" :class="{ 'is-active': hasErrorOccurred }">해당하는 주문이 없습니다.</p>
        </div>
      </horizontal-input-field>
    </div>
    <div class="order-detail" v-if="orders.length">
      <table class="table is-fullwidth">
        <thead>
        <tr>
          <!--<th>주문번호</th>-->
          <th>주문인</th>
          <th>주문 수량</th>
          <th>수령인</th>
          <th>수령인 전화번호</th>
          <th>수령인 주소</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="order in orders">
          <!--<th>{{ order.order_number }}</th>-->
          <th>{{ order.sender_name }}</th>
          <th>{{ order.amount }}</th>
          <th>{{ order.receiver_name }}</th>
          <th>{{ order.receiver_phone }}</th>
          <th>{{ order.receiver_addr }}</th>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import HorizontalInputField from '../HorizontalInputField';
import { API_URL } from '../../config';

export default {
  name: 'my-order',
  data() {
    return {
      orderNumber: '',
      hasErrorOccurred: false,
      orders: [],
    };
  },
  methods: {
    hideError() {
      this.hasErrorOccurred = false;
    },
    async fetchMyOrder() {
      let result;
      try {
        result = await this.$http.get(`${API_URL}/orders/${this.orderNumber}`);
      } catch (e) {
        this.hasErrorOccurred = true;
        this.orders = [];
        return;
      }
      this.orders = [result.data];
    },
  },
  components: {
    HorizontalInputField,
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
    .input-msg {
      display: none;
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
