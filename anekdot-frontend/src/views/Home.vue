<template>
  <div class="home">
    <h1><a href="/">Элитный клуб несмешных анекдотов</a></h1>
    <div class="content-block">
      Все анекдоты которые тут есть, сгенерированы при помощи <a href="https://github.com/sberbank-ai/ru-gpts">ru-gpt3-small</a>
      которой скормлены пару сотен цитат с баша и анекдотов.<br>
      Просим извинить если анекдоты оказались несмешные или оскорбительные, это все нейросеть а не мы честно.
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

</script>

<style lang="scss" scoped>
@use '@/style.scss' as *;

.content-block{
  a{
    color: $text-color;
    text-decoration: underline dotted;
    &:hover{
            color: $accent-color-yellow;
    }
  }
}
</style>
