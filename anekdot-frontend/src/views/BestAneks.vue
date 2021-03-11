<template>
  <div class="anek-list">
    <h1>Лучшие анекдоты</h1>
    <AnekdotListItem
      v-for="(item) in anekList"
      v-bind:text="item.text.slice(0,50)"
      v-bind:rating="item.rating"
      v-bind:num="item.id"
      v-bind:key="item.id"
    />
  </div>
</template>

<script>
import AnekdotListItem from '@/components/AnekdotListElement.vue'
import { mapState } from 'vuex'
import axios from 'axios'
import constants from '@/constants.js'

export default {
  name: 'BestAneks',
  components: {
    AnekdotListItem
  },

  created: function () {
    this.getAnekdotList()
  },

  computed: mapState('auth', ['accessToken']),
  data: () => {
    return {
      anekList: []
    }
  },
  methods: {
    getAnekdotList () {
      axios.get(constants.apiBaseURL + '/anekdot/?count=' + 20).then(
        response => {
          this.anekList = response.data
        }
      )
    }
  }

}
</script>

<style lang="scss">

@use '@/style.scss' as *;
.anek-list{
  margin-bottom: 44px;
}
</style>
