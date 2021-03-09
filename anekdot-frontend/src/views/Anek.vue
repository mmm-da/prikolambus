<template>
  <div  class="anek">
    <Anekdot
      v-bind:text='anekdotData.text'
      v-bind:num='anekdotData.num'
      v-bind:audio_link='anekdotData.audio_link'
      v-bind:gen_model='anekdotData.gen_model'
      v-bind:gen_k='anekdotData.gen_k'
      v-bind:gen_t='anekdotData.gen_t'
      v-bind:gen_p='anekdotData.gen_p'
      v-bind:gen_rp='anekdotData.gen_rp'
      v-if="isDataReady"
    />
    <AnekdotLoader v-else/>
      <button class="red">Дак не смешно же</button>
      <button class="blue">Пойдет</button>
      <button v-on:click="isDataReady = !isDataReady" >Следующий анек</button>
  </div>
</template>

<script>
import Anekdot from '@/components/Anekdot.vue'
import AnekdotLoader from '@/components/AnekdotLoader.vue'

export default {

  name: 'Anek',
  components: {
    Anekdot,
    AnekdotLoader
  },
  data: () => {
    return {
      isDataReady: true,
      anekdotData: {
        text: 'Купил мужик шляпу, а она ему как раз.',
        num: 10,
        audio_link: 'https://storage.yandexcloud.net/tts-cloud-s3/f8284eaf808be39d5310869c34719013658a7f8d466769cdc33b9ad1e811cd80f5d726ad203c4df6cde975034ff1f203a9bed55039882a2df3957b8a4a199e91?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=I89EjR7hpjWoYGE7xm7A%2F20210301%2Fru-central1%2Fs3%2Faws4_request&X-Amz-Date=20210301T130751Z&X-Amz-Expires=172800&X-Amz-Signature=535326d532798373e4602f86118d4c7183fb0fc08825eeca6d4f5b5ad2bb37d5&X-Amz-SignedHeaders=host',
        gen_model: 'funny1',
        gen_k: 1,
        gen_t: 0.5,
        gen_p: 0.6,
        gen_rp: 0.7
      }
    }
  }

}
</script>

<style lang="scss">

@use '@/style.scss' as *;

</style>
