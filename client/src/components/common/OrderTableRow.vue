<template>
  <tr>
    <th v-if="isAdmin">{{ order.order_number }}</th>
    <th>{{ order.sender_name }}</th>
    <th>{{ order.amount }}</th>
    <th>{{ order.receiver_name }}</th>
    <th>{{ order.receiver_phone }}</th>
    <th>{{ order.receiver_addr }}</th>
  </tr>
</template>

<script>
export default {
  name: 'order-table-row',
  props: [
    'order',
    'isAdmin',
  ],
};
</script>

<style lang="scss" scoped>

</style>
