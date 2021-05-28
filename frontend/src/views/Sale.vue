<template>
    <div>
        <div class="title"> SALE - Красивые скидки </div>
        <CategoryWrapper name="Цветы" :positions="flowers" :hide_titles="true" :show_sale="true"></CategoryWrapper>
        <CategoryWrapper name="Веснушки" :positions="dots" :hide_titles="true" :show_sale="true"></CategoryWrapper>
        <CategoryWrapper name="Слова" :positions="words" :hide_titles="true" :show_sale="true"></CategoryWrapper>
        <CategoryWrapper name="Животные" :positions="animals" :hide_titles="true" :show_sale="true"></CategoryWrapper>
        <CategoryWrapper name="Другое" :positions="other" :hide_titles="true" :show_sale="true"></CategoryWrapper>
        <CategoryWrapper name="Однушки" :positions="once" :hide_titles="true" :show_sale="true"></CategoryWrapper>
        <CategoryWrapper name="Наборы" :positions="sets" :hide_titles="true" :show_sale="true"></CategoryWrapper>
    </div>
</template>
<script>
const axios = require('axios')
import CategoryWrapper from './../components/CategoryWrapper'
export default {
    name: 'Sale',
    components: {
        CategoryWrapper
    },
    mounted: function () {
        axios.get('api/positions?show_sale=1&category=FL').then((response) => { this.flowers = response.data })
        axios.get('api/positions?show_sale=1&category=DO').then((response) => { this.dots = response.data })
        axios.get('api/positions?show_sale=1&category=WO').then((response) => { this.words = response.data })
        axios.get('api/positions?show_sale=1&category=AN').then((response) => { this.animals = response.data })
        axios.get('api/positions?show_sale=1&category=OT').then((response) => { this.other = response.data })
        axios.get('api/positions?show_sale=1&category=ON').then((response) => { this.once = response.data })
        axios.get('api/positions?show_sale=1&category=SE').then((response) => { this.sets = response.data })
    },
    data: () => ({
        flowers: [],
        dots: [],
        words: [],
        animals: [],
        other: [],
        once: [],
        sets: []
    })
}
</script>

<style scoped>
.title {
    font-size: 2rem;
    text-align: left;
    margin: 32px 0 0 32px;
}
</style>