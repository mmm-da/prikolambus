<template>
    <div class="anekdot">
        <ContentLoader class="content-block grid-container">
            <rect x="52" y="44" rx="5" ry="5" width="169" height="7" />
            <rect x="52" y="60" rx="5" ry="5" width="169" height="7" />
            <rect x="52" y="75" rx="5" ry="5" width="169" height="7" />
            <rect x="52" y="90" rx="5" ry="5" width="169" height="7" />
            <rect x="310" y="35" rx="100" ry="100" width="50" height="50" />
            <rect x="82" y="112" rx="5" ry="5" width="100" height="6" />
            <rect x="82" y="16" rx="5" ry="5" width="100" height="8" />
        </ContentLoader>
    </div>
</template>

<script>
import { ContentLoader } from 'vue-content-loader'
export default {
  name: 'AnekdotLoader',
  components: {
    ContentLoader
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
    padding:32px 8px 8px 8px;
    color: $muted-text-color;
}
.text {
    grid-area: text;
    padding:32px 32px 32px 64px;
}
.generator-settings {
    grid-area: generator-settings;
    font-size: 0.5em;
    padding:0px 0px 16px 0px;
    color: $muted-text-color;
    .settings-value{
        font-weight: bold;
        color: $accent-color-blue;
    }
}

.sound {
    grid-area: sound;
    margin: 64px;
}

</style>
