<template>
  <div>
    <h2 class="title">사과즙 구매하기</h2>
    <p class="subtitle">사과즙을 구매하시려면 아래의 정보를 입력해주세요!</p>
    <horizontal-input-field>
      <label slot="label" class="label" for="sender-name">보내시는 분 성함</label>
      <input slot="input" id="sender-name" class="input"
             type="text" v-model="senderName" />
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="applejuice-number">주문 수량</label>
      <div slot="input" class="select">
        <select id="applejuice-number" v-model="applejuiceNum">
          <option v-for="num in range(10)" :key="num">{{ num }}</option>
        </select>
      </div>
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="receiver-name">받으시는 분 성함</label>
      <input slot="input" id="receiver-name" class="input"
             type="text" v-model="receiverName" />
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="receiver-address">받으시는 분 주소</label>
      <input slot="input" id="receiver-address" class="input"
             type="text" v-model="receiverAddress" />
    </horizontal-input-field>
    <div class="container">
      <button class="button is-primary">Submit</button>
    </div>
  </div>
</template>

<script>
import { range } from '../utils/number'; /* eslint-disable-line */
import HorizontalInputField from '../components/HorizontalInputField';

export default {
  name: 'Buy',
  data() {
    return {
      senderName: '',
      applejuiceNum: '',
      receiverName: '',
      receiverAddress: '',
    };
  },
  methods: {
    range(n) {
      return range(n);
    },
  },
  components: {
    HorizontalInputField,
  },
};
</script>

<style style="scss" scoped>

</style>
