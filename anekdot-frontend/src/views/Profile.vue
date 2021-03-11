/* eslint-disable vue/require-v-for-key */
<template>
  <div class="profile content-block">
      <h3>{{username}}</h3>
      <p v-if="isAdmin">админ</p>
    <div v-if="isInviteVisible">
      Инвайт пропадет при переходе на другую страницу, скопирую и отправь кому надо.
      <ul v-for="(invite, index) in invites" v-bind:key="index">
        <div>{{invite}}</div>
      </ul>
      <div v-if="isInviteWarningVisible" class="warning">Обнови страницу и можешь получить еще 5</div>
    </div>
    <button v-on:click="getInvite">Получить инвайт</button>
    <button class="red" v-on:click="logout">Выйти</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import constants from '@/constants'

export default {
  name: 'Profile',
  data: () => {
    return {
      invites: [],
      isInviteVisible: false,
      isInviteWarningVisible: false
    }
  },
  computed: mapState('auth', ['accessToken', 'username', 'isAdmin']),
  methods: {
    logout () {
      this.$store.dispatch('auth/logout')
      this.$router.push('/')
    },
    getInvite () {
      if (this.invites.length < 5) {
        this.isInviteVisible = true
        axios.get(constants.apiBaseURL + '/invite/', { headers: { Authorization: `Bearer ${this.accessToken}` } }).then(
          response => this.invites.push(response.data.code)
        )
      } else this.isInviteWarningVisible = true
    }
  }
}
</script>

<style lang="scss">

@use '@/style.scss' as *;

h3{
  margin-bottom: 16px;
}

p{
  font-size: 0.7em;
  font-weight: 600;
  margin-top: 8px;
  color: $accent-color-blue
}

.warning {
  margin-bottom: 16px;
  color: $accent-color-red;
  font-weight: 600;
}

ul {
  font-size: 0.8em;
  padding: 0px;
}

</style>
