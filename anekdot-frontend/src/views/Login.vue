<template>

  <div class="login">
    <div class='text-input'>
      <label>
        <input placeholder=" ">
        <span>Логин</span>
      </label>
    </div>
    <div class='text-input'>
      <label>
        <input placeholder=" ">
        <span>Пароль</span>
      </label>
    </div>
    <div>
      <button>Войти</button>
    </div>
    <div class="link">
      <router-link to="/reg">Зарегистрироватся</router-link>
    </div>
  </div>
</template>

<script>
export default {

  name: 'Login',
  components: {
  },
  data: () => {
    return {
      login: String,
      password: String
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
