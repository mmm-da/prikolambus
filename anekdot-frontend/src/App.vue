<template>
  <div id="app">
    <main>
      <nav id="nav">
        <a v-on:click="getNewId">Случайный анекдот</a>
        <router-link to="/best">Лучшие анеки</router-link>
        <router-link v-if="isAdmin" to="/gen">Генератор</router-link>
        <router-link v-if="isAuth" to="/profile">
            <span class="admin-badge" v-if="isAdmin"># </span>{{username}}
        </router-link>
        <router-link v-else to="/login">
            Вход
        </router-link>
      </nav>
        <router-view/>
    </main>
    <footer>
      <strike>Сделали</strike> <a href="https://github.com/spAm25">Даня</a> и <a href="https://github.com/znifer"> Илюха</a>
    </footer>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import constants from '@/constants.js'

export default {
  state: () => ({
    isAuth: true,
    prevAnek: NaN
  }),
  computed: mapState('auth', ['isAuth', 'isAdmin', 'username']),
  methods: {
    getNewId () {
      axios.get(constants.apiBaseURL + '/next/').then(
        (response) => {
          if (response.data.id === this.prevAnek) {
            this.getNewId()
          } else {
            this.prevAnek = response.data.id
            this.$router.push('/anek/' + response.data.id)
          }
        }
      ).catch(
        () => {
          this.$router.push('/')
        }
      )
    }
  }
}
</script>

<style lang="scss">

@use "./style.scss" as *;

main {
  min-height: calc(100vh - 70px);

  @media (min-width: 1320px) {
    margin-right: 10%;
    margin-left: 10%;
    width:80%;
  }
}
footer {
  font-size: 0.7em;
  height: 50px;
}

nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 30px;
  text-align: center;
  a {
    cursor: pointer;
    padding:16px;
    font-weight: bold;
    color: $text-color;

    &:hover{
      color: $accent-color-yellow;
    }

    @media (max-width: 600px) {
      font-size:0.9em;
    }

  }

}

.admin-badge{
  color: $accent-color-blue;
}
</style>
