<template>
  <div class="reg">
  <form v-on:submit.prevent="onClickRegButton">
    <div class='text-input'>
      <label>
        <input v-model="inviteToken" type="text" placeholder=" ">
        <span>Инвайт</span>
      </label>
    </div>
    <div class='text-input'>
      <label>
        <input v-model="login" id="username" autocomplete="username" type="text" placeholder=" ">
        <span>Логин</span>
      </label>
    </div>
    <div class='text-input'>
      <label>
        <input v-model="password" id=“current-password” autocomplete="current-password" type="password" placeholder=" ">
        <span>Пароль</span>
      </label>
    </div>
    <div>
      <button>Зарегистрироватся</button>
    </div>
  </form>
  </div>
</template>

<script>
import axios from 'axios'
import constants from '@/constants.js'

export default {

  name: 'Reg',
  components: {
  },
  data: () => {
    return {
      inviteToken: '',
      login: '',
      password: ''
    }
  },
  methods: {
    onClickRegButton () {
      axios.post(
        constants.apiBaseURL + '/register/?invite=' + this.inviteToken
        , { username: this.login, password: this.password }).then(
        () => {
          this.$store.dispatch('auth/login', { username: this.login, password: this.password })
          this.$router.push('/')
        }
      ).catch(
        error => {
          console.log(error)
        }
      )
    }
  }
}
</script>

<style lang="scss">

@use '@/style.scss' as *;

.reg{
  display: flex;
  flex-direction: column;
}
</style>
