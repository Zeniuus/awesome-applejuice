<template>
  <div class="field">
    <slot name="label"></slot>
    <div class="control">
      <slot name="input"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'input-field',
};
</script>

<style lang="scss" scoped>
.field {
  margin-bottom: 2rem;

  &:not(:last-child) {
    margin-bottom: 2rem;
  }

  .control {
    width: 100%;
  }
}
</style>
