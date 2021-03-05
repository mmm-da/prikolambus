<template>
    <div class="player">
        <a v-on:click.prevent="playing = !playing" title="Play/Pause" href="#">
            <svg width="1.5em" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <path v-if="!playing" fill="currentColor" d="M15,10.001c0,0.299-0.305,0.514-0.305,0.514l-8.561,5.303C5.51,16.227,5,15.924,5,15.149V4.852c0-0.777,0.51-1.078,1.135-0.67l8.561,5.305C14.695,9.487,15,9.702,15,10.001z"/>
              <path v-else fill="currentColor" d="M15,3h-2c-0.553,0-1,0.048-1,0.6v12.8c0,0.552,0.447,0.6,1,0.6h2c0.553,0,1-0.048,1-0.6V3.6C16,3.048,15.553,3,15,3z M7,3H5C4.447,3,4,3.048,4,3.6v12.8C4,16.952,4.447,17,5,17h2c0.553,0,1-0.048,1-0.6V3.6C8,3.048,7.553,3,7,3z"/>
            </svg>
        </a>
      <audio :loop="innerLoop" ref="audiofile" :src="file" preload="auto" style="display: none"></audio>
    </div>
</template>

/* eslint-disable no-tabs */
<script>
const AudioPlayer = {
  props: {
    file: {
      type: String,
      default: null
    },
    autoPlay: {
      type: Boolean,
      default: false
    },
    loop: {
      type: Boolean,
      default: false
    }
  },
  data: () => ({
    audio: undefined,
    currentSeconds: 0,
    durationSeconds: 0,
    innerLoop: false,
    loaded: false,
    playing: false,
    previousVolume: 35,
    showVolume: false,
    volume: 100
  }),
  watch: {
    playing (value) {
      if (value) { return this.audio.play() }
      this.audio.pause()
    },
    volume (value) {
      this.showVolume = false
      this.audio.volume = this.volume / 100
    }
  },
  methods: {
    download () {
      this.stop()
      window.open(this.file, 'download')
    },
    load () {
      if (this.audio.readyState >= 2) {
        this.loaded = true
        this.durationSeconds = parseInt(this.audio.duration)
        this.playing = this.autoPlay
        return this.playing
      }

      throw new Error('Failed to load sound file.')
    },
    seek (e) {
      if (!this.playing || e.target.tagName === 'SPAN') {
        return
      }

      const el = e.target.getBoundingClientRect()
      const seekPos = (e.clientX - el.left) / el.width

      this.audio.currentTime = parseInt(this.audio.duration * seekPos)
    },
    stop () {
      this.playing = false
      this.audio.currentTime = 0
    },
    update (e) {
      this.currentSeconds = parseInt(this.audio.currentTime)
    }
  },
  created () {
    this.innerLoop = this.loop
  },
  mounted () {
    this.audio = this.$el.querySelectorAll('audio')[0]
    this.audio.addEventListener('timeupdate', this.update)
    this.audio.addEventListener('loadeddata', this.load)
    this.audio.addEventListener('pause', () => { this.playing = false })
    this.audio.addEventListener('play', () => { this.playing = true })
  }
}

export default AudioPlayer
</script>

<style scoped lang='scss'>

@use "@/style.scss" as *;

.player {
  transition-duration: 0.1s;
  display: flex;
  align-items: center;
  justify-content: center;
  width:3em;
  height:3em;
  border: 3px solid $accent-color-yellow;
  border-radius: 100px;
  outline: none;
  &:hover{
    background-color: $accent-color-yellow;
  }

  a{
    height: 100%;
    width: 100%;
    border-radius: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    &:hover{
      color: #fff;
    }
    -webkit-tap-highlight-color: transparent;
  }
}

</style>
