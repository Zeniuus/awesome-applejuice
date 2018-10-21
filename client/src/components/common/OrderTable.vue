<template>
  <div class="order-detail" v-if="orders.length">
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th v-if="isAdmin">주문번호</th>
          <th class="sender-name">주문인</th>
          <th class="amount">주문 수량</th>
          <th class="receiver-name">수령인</th>
          <th class="receiver-phone">수령인 전화번호</th>
          <th class="receiver-addr">수령인 주소</th>
        </tr>
      </thead>
      <tbody>
        <order-table-row v-for="order in orders" :order="order" :key="order.order_number" />
      </tbody>
    </table>
  </div>
</template>

<script>
import OrderTableRow from './OrderTableRow';

export default {
  name: 'order-table',
  props: [
    'orders',
    'isAdmin',
  ],
  components: {
    OrderTableRow,
  },
};
</script>

<style lang="scss" scoped>
.sender-name {
  width: 5rem;
}

.amount {
  width: 6rem;
}

.receiver-name {
  width: 5rem;
}

.receiver-phone {
  width: 10rem;
}
</style>
