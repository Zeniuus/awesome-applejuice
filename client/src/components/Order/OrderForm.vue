<template>
  <div>
    <h2 class="title">사과즙 주문하기</h2>
    <p class="subtitle">사과즙을 주문하시려면 아래의 정보를 입력해주세요!</p>
    <horizontal-input-field>
      <label slot="label" class="label" for="sender-name">보내시는 분 성함</label>
      <input slot="input" id="sender-name" class="input"
             type="text" v-model="senderName" />
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="amount">주문 수량</label>
      <div slot="input" class="select">
        <select id="amount" v-model="amount">
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
      <label slot="label" class="label" for="receiver-phone">받으시는 분 전화번호</label>
      <div slot="input" class="input-wrapper">
        <input id="receiver-phone" class="input"
               type="tel" v-model="receiverPhone" />
        <span class="input-msg">대시 혹은 하이픈(-) 없이 작성해주세요!</span>
      </div>
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="receiver-address">받으시는 분 주소</label>
      <input slot="input" id="receiver-address" class="input"
             type="text" v-model="receiverAddr" />
    </horizontal-input-field>
    <div class="buttons">
      <button class="button is-primary" :class="{ 'is-loading': this.isLoading }"
              @click="createNewOrder">
        주문하기
      </button>
    </div>
  </div>
</template>

<script>
import HorizontalInputField from '../common/HorizontalInputField';
import { range } from '../../utils/number'; /* eslint-disable-line */
import { API_URL } from '../../config';

export default {
  name: 'order_purchase',
  data() {
    return {
      senderName: '',
      amount: '',
      receiverName: '',
      receiverAddr: '',
      receiverPhone: '',
      isLoading: false,
    };
  },
  methods: {
    range,
    async createNewOrder() {
      /* TODO: validate inputs. */
      this.isLoading = true;
      let result;
      try {
        const data = {
          sender_name: this.senderName,
          receiver_name: this.receiverName,
          receiver_phone: this.receiverPhone,
          receiver_addr: this.receiverAddr,
          amount: this.amount,
        };
        result = await this.$http.post(`${API_URL}/orders/`, data);
      } catch (e) {
        alert(e.toString()); /* eslint-disable-line */
        this.isLoading = false;
        return;
      }
      this.isLoading = false;
      const orderNumber = result.data.order_number;
      this.$router.push({ name: 'order_complete', params: { orderNumber } });
    },
  },
  components: {
    HorizontalInputField,
  },
};
</script>

<style lang="scss" scoped>
#sender-name, #receiver-name {
  width: 6rem;
}
#receiver-phone {
  width: 10rem;
}
.input-wrapper {
  position: relative;
  .input-msg {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    font-size: 0.9rem;
    margin-left: 1rem;
    font-weight: bold;
    /*&::before {*/
    /*content: '* ';*/
    /*}*/
  }
}
.buttons {
  width: 100%;
  .button {
    margin: 0 auto;
  }
}
</style>
