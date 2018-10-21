<template>
  <div>
    <h2 class="title">사과즙 주문하기</h2>
    <p class="subtitle">사과즙을 주문하시려면 아래의 정보를 입력해주세요!</p>
    <horizontal-input-field>
      <label slot="label" class="label" for="sender-name">보내시는 분 성함</label>
      <input slot="input" id="sender-name" class="input" ref="senderName"
             type="text" v-model="senderName" />
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="amount">주문 수량</label>
      <div slot="input" class="select">
        <select id="amount" v-model="amount" ref="amount">
          <option v-for="num in range(10)" :key="num">{{ num + 1 }}</option>
        </select>
      </div>
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="receiver-name">받으시는 분 성함</label>
      <input slot="input" id="receiver-name" class="input" ref="receiverName"
             type="text" v-model="receiverName" />
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="receiver-phone">받으시는 분 전화번호</label>
      <div slot="input" class="input-wrapper">
        <input id="receiver-phone" class="input" ref="receiverPhone"
               type="tel" v-model="receiverPhone" />
        <span class="input-msg">대시 혹은 하이픈(-) 없이 작성해주세요!</span>
      </div>
    </horizontal-input-field>
    <horizontal-input-field>
      <label slot="label" class="label" for="receiver-address">받으시는 분 주소</label>
      <input slot="input" id="receiver-address" class="input" ref="receiverAddr"
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

const inputI18n = {
  senderName: '보내시는 분 성함',
  amount: '주문 수량',
  receiverName: '받으시는 분 성함',
  receiverPhone: '받으시는 분 전화번호',
  receiverAddr: '받으시는 분 주소',
};

function validationFailMsg({ type, input }) {
  const inputName = inputI18n[input];
  switch (type) {
    case 'notEmpty': return `[${inputName}] 항목이 비어있습니다.`;
    case 'number': return `[${inputName}] 항목은 숫자여야 합니다.`;
    default: return '알 수 없는 오류로 주문에 실패했습니다.';
  }
}

function validateForm(requiredValidationTypes) {
  const validate = {
    notEmpty: input => !!this[input],
    number: input => /\d+/.test(this[input]),
  };

  return Object.keys(requiredValidationTypes).every((input) => {
    const types = requiredValidationTypes[input];
    return types.every((type) => {
      const isValid = validate[type](input);
      if (!isValid) {
        alert(validationFailMsg({ type, input }));
        this.$refs[input].focus();
      }
      return isValid;
    });
  });
}

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
    validateForm,
    async createNewOrder() {
      const isFormValid = this.validateForm({
        senderName: ['notEmpty'],
        amount: ['notEmpty', 'number'],
        receiverName: ['notEmpty'],
        receiverPhone: ['notEmpty', 'number'],
        receiverAddr: ['notEmpty'],
      });
      if (!isFormValid) return;

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
