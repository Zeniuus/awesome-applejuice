<template>
  <div class="field is-horizontal">
    <div class="field-label is-normal">
      <slot name="label"></slot>
    </div>
    <div class="field-body">
      <div class="control">
        <slot name="input"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'horizontal-input-field',
};
</script>

<style lang="scss" scoped>
.control {
  width: 100%;
}
</style>
