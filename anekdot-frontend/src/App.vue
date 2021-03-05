<template>
  <div id="app">
    <main>
      <nav id="nav">
        <router-link to="/anek">Случайный анекдот</router-link>
        <router-link to="/best">Лучшие анеки</router-link>
        <router-link to="/login">
            Войти
        </router-link>
      </nav>
        <router-view/>
    </main>
    <footer>
      <strike>Сделали</strike> <a href="https://github.com/spAm25">Даня</a> и <a href="https://github.com/znifer"> Илюха</a>
    </footer>
  </div>
</template>

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
  justify-content: center;
  align-content: center;
  padding: 30px;
  text-align: center;
  a {
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

</style>
