<template>
  <div  class="anek">
    <Anekdot
      v-bind:text='text'
      v-bind:num='id'
      v-bind:audio_link='audio_link'
      v-bind:gen_model='gen_model'
      v-bind:gen_k='gen_k'
      v-bind:gen_t='gen_t'
      v-bind:gen_p='gen_p'
      v-bind:gen_rp='gen_rp'
      v-bind:gen_seed='gen_seed'
      v-if="isDataReady"
    />
    <AnekdotLoader v-else/>
      <div class="rank-span">
        <button v-if="userID && isAbleVote" v-on:click="vote(-1)" class="red">Дак не смешно же</button>
        <span class="rank">{{rank}}</span>
        <button v-if="userID && isAbleVote" v-on:click="vote(1)" class="blue">Пойдет</button>
      </div>
      <button v-on:click="getNewId" >Следующий анек</button>
  </div>
</template>

<script>
import Anekdot from '@/components/Anekdot.vue'
import AnekdotLoader from '@/components/AnekdotLoader.vue'
import axios from 'axios'
import constants from '@/constants.js'
import { mapState } from 'vuex'

export default {
  name: 'Anek',
  components: {
    Anekdot,
    AnekdotLoader
  },

  created: function () {
    this.getAnekdot()
  },

  computed: mapState('auth', ['accessToken', 'userID']),

  watch: {
    '$route.params.id': 'getAnekdot'
  },
  data: () => {
    return {
      prevAnek: NaN,
      isDataReady: false,
      audio_link: '',
      text: '',
      id: 0,
      gen_model: 'funny1',
      gen_k: 1,
      gen_t: 0.5,
      gen_p: 0.6,
      gen_rp: 0.7,
      gen_seed: 0,
      rank: 0,
      isAbleVote: true
    }
  },
  methods: {
    getAnekdot () {
      this.isDataReady = false
      axios.get(constants.apiBaseURL + '/anekdot/' + this.$route.params.id).then(
        (response) => {
          this.id = response.data.id
          this.text = response.data.text
          this.gen_model = response.data.model_name
          this.gen_k = response.data.k
          this.gen_t = response.data.t
          this.gen_p = response.data.p
          this.gen_rp = response.data.rep_penalty
          this.gen_seed = response.data.seed
          this.rank = response.data.rating
          this.isAbleVote = !response.data.rated_by.find(el => el === this.userID)
          this.isDataReady = true
          return response.data.tts_hash
        }
      ).then(
        (hash) => {
          axios.get(constants.ttsBaseURL + '/tts/' + hash).then(
            (response) => {
              this.audio_link = response.data.link
            }
          )
        }
      ).catch(
        () => {
          this.$router.push('/')
        }
      )
    },
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
    },
    vote (num) {
      axios.post(constants.apiBaseURL + '/rate/', { id: this.id, rating: num }, { headers: { Authorization: `Bearer ${this.accessToken}` } }).then(
        () => {
          this.isAbleVote = false
          this.rank += num
        }
      ).catch(
        () => {
          this.isAbleVote = false
        }
      )
    }
  }
}
</script>

<style lang="scss">

@use '@/style.scss' as *;

.rank-span{
  margin-top: 32px;
  margin-bottom: 32px;
}

.rank {
  padding-left: 32px;
  padding-right: 32px;
}
</style>
