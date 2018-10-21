<template>
  <div>
    <div id="order-tabs" class="tabs is-centered is-medium">
      <ul>
        <li :class="{ 'is-active': [Tab.PURCHASE, Tab.COMPLETE].includes(tab) }">
          <router-link :to="{ name: 'order_purchase' }">주문하기</router-link>
        </li>
        <li :class="{ 'is-active': tab === Tab.MY_ORDER }">
          <router-link :to="{ name: 'order_my-order' }">내 주문 확인하기</router-link>
        </li>
      </ul>
    </div>
    <router-view />
  </div>
</template>

<script>
import HorizontalInputField from '../components/HorizontalInputField';

const constants = {
  Tab: {
    PURCHASE: 'PURCHASE',
    MY_ORDER: 'MY_ORDER',
    COMPLETE: 'COMPLETE',
  },
};

function updateTab(_this, nextTab) {
  const routeTabConst = nextTab
    .replace('-', '_')
    .toUpperCase();
  _this.tab = constants.Tab[routeTabConst]; /* eslint-disable-line no-param-reassign */
}

export default {
  name: 'Order',
  data() {
    return {
      tab: '',
      ...constants,
    };
  },
  beforeRouteEnter(to, from, next) {
    const nextTab = to.name.split('_')[1];
    if (!nextTab) next({ name: 'order_purchase' });
    else next(vm => updateTab(vm, nextTab));
  },
  beforeRouteUpdate(to, from, next) {
    const nextTab = to.name.split('_')[1];
    if (!nextTab) next({ name: 'order_purchase' });
    else {
      updateTab(this, nextTab);
      next();
    }
  },
  components: {
    HorizontalInputField,
  },
};
</script>

<style lang="scss" scoped>
#order-tabs {
  margin-bottom: 3rem;
}
</style>
