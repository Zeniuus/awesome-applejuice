<template>
  <div id="manage-page-root">
    <div v-if="isLoading" class="page-loader">
      <div class="page-loader-spinner-wrapper">
        <div class="page-loader-spinner">
          주문 목록을 불러오는 중입니다...
        </div>
      </div>
    </div>
    <order-table v-else :orders="orders" :is-admin="true" />
  </div>
</template>

<script>
import OrderTable from '../components/common/OrderTable';
import { API_URL } from '../config';

export default {
  name: 'manage',
  data() {
    return {
      orders: null,
    };
  },
  computed: {
    isLoading() {
      return !this.orders;
    },
  },
  components: {
    OrderTable,
  },
  async created() {
    const result = await this.$http.get(`${API_URL}/orders/`);
    this.orders = result.data;
  },
};
</script>

<style lang="scss" scoped>
#manage-page-root {
  .page-loader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 10;
    background: #eeeeeeee;

    .page-loader-spinner {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  }
}
</style>
