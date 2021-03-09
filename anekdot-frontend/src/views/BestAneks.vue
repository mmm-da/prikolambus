<template>
  <div class="anek-list">
    <h1>Лучшие анекдоты</h1>
    <AnekdotListItem
      v-for="(item) in anekList"
      v-bind:text="item.text"
      v-bind:rating="item.rating"
      v-bind:num="item.id"
      v-bind:key="item.id"
    />
  </div>
</template>

<script>
import AnekdotListItem from '@/components/AnekdotListElement.vue'

export default {
  name: 'BestAneks',
  components: {
    AnekdotListItem
  },
  data: () => {
    return {
      anekList: [
        { id: 192, text: 'Купил мужик шляпу, а она ему как раз.', rating: 100 },
        { id: 95, text: 'Купил мужик шляпу, а она ему как раз.', rating: 80 },
        { id: 19, text: 'Купил мужик шляпу, а она ему как раз.', rating: 73 },
        { id: 24, text: 'Купил мужик шляпу, а она ему как раз.', rating: 14 },
        { id: 6, text: 'Купил мужик шляпу, а она ему как раз.', rating: 4 }
      ]
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
