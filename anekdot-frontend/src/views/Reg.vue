<template>
  <div class="reg">
    <div class='text-input'>
      <label>
        <input placeholder=" ">
        <span>Инвайт</span>
      </label>
    </div>
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
      <button>Зарегистрироватся</button>
    </div>
  </div>
</template>

<script>
export default {

  name: 'Reg',
  components: {
  },
  data: () => {
    return {
      inviteToken: String,
      login: String,
      password: String
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
