<template>
    <div class="anekdot">
        <div class="grid-container content-block">
            <div class='num-field'>
                #{{num}}
            </div>
            <div class='text'>
                {{text}}
            </div>
            <div class='generator-settings'>
                model: <span class="settings-value">{{gen_model}}</span> |
                k = <span class="settings-value">{{gen_k}}</span> |
                p = <span class="settings-value">{{gen_p}}</span> |
                t = <span class="settings-value">{{gen_t}}</span> |
                rp = <span class="settings-value">{{gen_rp}}</span>
            </div>
            <AudioPlayer class='sound' v-bind:file="audio_link"/>
        </div>
    </div>
</template>

<script>
import AudioPlayer from '@/components/AudioPlayer.vue'
export default {
  name: 'Anekdot',
  props: {
    text: String,
    num: Number,
    audio_link: String,
    gen_model: String,
    gen_k: Number,
    gen_p: Number,
    gen_t: Number,
    gen_rp: Number
  },
  components: {
    AudioPlayer
  }
}
</script>

<style lang="scss" scoped>
@use '@/style.scss' as *;

.content-block{
    padding: 4px
}

.grid-container {
  justify-items: center;
  align-items: center;
  display: grid;
  grid-template-columns: 0.2fr 1fr 1fr 1fr;
  grid-template-rows: 15% 70% 15%;
  gap: 0px 0px;
  grid-template-areas:
    "num-field num-field num-field sound"
    "text text text sound"
    "generator-settings generator-settings generator-settings sound";
}
.num-field {
    grid-area: num-field;
    font-size: 0.8em;
    padding:50px 8px 8px 8px;
    color: $muted-text-color;
}
.text {
    grid-area: text;
    padding:32px 32px 32px 40px;
}
.generator-settings {
    grid-area: generator-settings;
    font-size: 0.5em;
    padding:0px 0px 16px 0px;
    color: $muted-text-color;
    .settings-value{
        color: $accent-color-blue;
        font-weight: bold;
    }
}

.sound {
    grid-area: sound;
    margin: 64px;
}

</style>
