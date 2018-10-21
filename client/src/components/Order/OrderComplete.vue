<template>
  <div>
    <h2 class="title">주문 완료!</h2>
    <p>
      주문번호는 <span class="order-number">{{orderNumber}}</span> 입니다.
    </p>
    <p>
      혹시 주문번호를 잊어버리시면 관리자(jsh56son@gmail.com)에게 문의주세요!
    </p>
  </div>
</template>

<script>
export default {
  name: 'OrderComplete',
  props: [
    'orderNumber',
  ],
};
</script>

<style lang="scss" scoped>
.order-number {
  font-weight: bold;
}
</style>
