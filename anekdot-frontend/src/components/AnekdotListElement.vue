<template>
    <router-link class='list-element-link' to="/anek">
        <div class="anekdot-list-element content-block">
            <div class='id'>#{{num}}</div>
            <div class='text'>{{text}}</div>
            <div class='rating'>{{rating}}</div>
        </div>
    </router-link>
</template>

<script>
export default {
  name: 'AnekdotListItem',
  props: {
    text: String,
    num: Number,
    rating: Number
  }
}
</script>

<style lang="scss" scoped>
@use '@/style.scss' as *;

.anekdot-list-element{
    display:flex;
    align-items: center;
    justify-content: space-around;
}

.list-element-link{
    color:$text-color;
    &:hover{
        color:$text-color;
        text-decoration: none;
    }
}

.id{
    padding: 0px 8px 0px 8px;
    font-size: 0.7em;
    color:$muted-text-color;
    &:hover{
        text-decoration: underline;
    }
}

.text{
    padding: 0px 16px 0px 16px;
    font-size: 0.8em;
    &:hover{
        text-decoration: none;
    }
}

.rating{
    padding: 0px 8px 0px 8px;
    font-weight: bold;
    color: $accent-color-yellow;
    &:hover{
        text-decoration: underline;
    }
}
</style>
