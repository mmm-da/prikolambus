<template>

  <div class="login">
    <form v-on:submit.prevent="onClickLoginButton">
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
      <button>Войти</button>
    </div>
    <div class="link">
      <router-link to="/reg">Зарегистрироватся</router-link>
    </div>
  </form>
  </div>
</template>

<script>
import auth from '@/jwtAuth'
import axios from 'axios'
import constants from '@/constants'
export default {

  name: 'Login',
  components: {
  },
  data: () => {
    return {
      login: '',
      password: '',
      remember: true
    }
  },
  methods: {
    onClickLoginButton () {
      console.log(this.login, this.password)
      axios.post(constants.apiBaseURL + '/token/', { username: this.login, password: this.password })
        .then((response) => {
          auth.isAuth = true
          localStorage.setItem('accessToken', response.data.access)
          auth.accessToken = response.data.access
          if (this.remember) {
            localStorage.setItem('refreshToken', response.data.refresh)
            auth.refreshToken = response.data.refresh
          } else auth.refreshToken = null
        }).catch(() => {
          auth.isAuth = false
          auth.refreshToken = null
          auth.accessToken = null
        })
      this.$router.push('/best')
    }
  }
}
</script>

<style lang="scss">

@use '@/style.scss' as *;

.login{
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
</style>
