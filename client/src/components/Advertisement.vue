<template>
  <div class="advertisement card">
    <p>
      사과즙 절찬 판매중!
    </p>
    <p>
      자세한 사항은 <router-link :to="{ name: 'order' }">주문하기 페이지</router-link>를 참고해주세요.
    </p>
  </div>
</template>

<script>
export default {
  name: 'advertisement',
};
</script>

<style lang="scss" scoped>
.advertisement {
  width: 100%;
  padding: 5rem 0.5rem;
  word-break: break-word;
}
</style>
