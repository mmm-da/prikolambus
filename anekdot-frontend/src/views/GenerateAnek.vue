<template>
  <div class="anek-generator-form">
    <form v-if=" state === 'form' " v-on:submit.prevent="onClickGenerateButton">
      <h2 v-if="status === 'error'">Ошибка генерации</h2>
      <h2 v-if="status === 'success'">Анекдоты сгенерированы</h2>
      <div class='text-input'>
          <select v-model="model">
              <option value="mmm-da/anekdot_funny1_rugpt3Small">funny1</option>
              <option value="mmm-da/anekdot_funny2_rugpt3Small">funny2</option>
          </select>
      </div>
      <div class='text-input'>
        <label>
          <input v-model="count" placeholder=" ">
          <span>Количество анекдотов</span>
        </label>
      </div>
      <div class='text-input'>
        <label>
          <input v-model="t" placeholder=" ">
          <span>t</span>
        </label>
      </div>
      <div class='text-input'>
        <label>
          <input v-model="k" placeholder=" ">
          <span>k</span>
        </label>
      </div>
      <div class='text-input'>
        <label>
          <input v-model="p" placeholder=" ">
          <span>p</span>
        </label>
      </div>
      <div class='text-input'>
        <label>
          <input v-model="r_p" placeholder=" ">
          <span>r_p</span>
        </label>
      </div>
      <div class='text-input'>
        <label>
          <input v-model="length" placeholder=" ">
          <span>Длина анекдота</span>
        </label>
      </div>
      <div>
        <button>Сгенерировать</button>
      </div>
    </form>
    <div v-if="state === 'spinner'" class="spinner">
      <div class="double-bounce1"></div>
      <div class="double-bounce2"></div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import constants from '@/constants.js'

export default {

  name: 'GenerateAnek',
  computed: mapState('auth', ['accessToken']),
  data: () => {
    return {
      state: 'form',
      status: 'idle',

      model: 'mmm-da/anekdot_funny1_rugpt3Small',
      count: 5,
      t: 0.95,
      k: 0,
      p: 0.95,
      r_p: 1,
      length: 100
    }
  },
  methods: {
    onClickGenerateButton () {
      this.state = 'spinner'
      axios.post(
        constants.apiBaseURL + '/generate/?length=' + this.length + '&count=' + this.count
        , { model_name: this.model, t: this.t, p: this.p, k: this.k, rep_penalty: this.r_p },
        { headers: { Authorization: `Bearer ${this.accessToken}` } }).then(
        () => {
          this.state = 'form'
          this.status = 'success'
        }
      ).catch(
        error => {
          this.state = 'form'
          this.status = 'error'
          console.log(error)
        }
      )
    }
  }
}
</script>

<style lang="scss">

@use '@/style.scss' as *;

.anek-generator-form{
  margin-bottom: 64px;
}

h2{
  margin-top: 4px;
}

.spinner {
  width: 100px;
  height: 100px;

  position: relative;
  margin: 100px auto;
}

.double-bounce1, .double-bounce2 {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: adjust-color($accent-color-yellow, $alpha: 0.5);
  opacity: 0.6;
  position: absolute;
  top: 0;
  left: 0;

  -webkit-animation: sk-bounce 2s infinite ease-in-out;
  animation: sk-bounce 2s infinite ease-in-out;
}

.double-bounce2 {
  -webkit-animation-delay: -1s;
  animation-delay: -1s;
}

@-webkit-keyframes sk-bounce {
  0%, 100% { -webkit-transform: scale(0.0) }
  50% { -webkit-transform: scale(1.0) }
}

@keyframes sk-bounce {
  0%, 100% {
    transform: scale(0.0);
    -webkit-transform: scale(0.0);
  } 50% {
    transform: scale(1.0);
    -webkit-transform: scale(1.0);
  }
}

</style>
