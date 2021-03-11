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
      this.$store.dispatch('auth/login', { username: this.login, password: this.password })
      this.$router.push('/')
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
