<template>
    <div>
        <div class="slider">
            <div class="slide" id="slide_1"> 
                <div id="gallery_bigpick">
                    <div class="text-container"> ПЕРЕВОДНЫЕ<br>ТАТУ </div>
                </div>
                <div class="slider_1000" id="pic_2">
                    
                </div>
                <div class="slider_1000" id="pic_3">
                
                </div>
            </div>
            <div class="paginator"> 
                <div class="active"></div> <div></div> <div></div>
            </div>
        </div>
        <CategoryWrapper id="flowers" name="Цветы" :positions="flowers"></CategoryWrapper>
        <CategoryWrapper id="dots" name="Веснушки" :positions="dots"></CategoryWrapper>
        <CategoryWrapper id="words" name="Слова" :positions="words"></CategoryWrapper>
        <CategoryWrapper id="animals" name="Животные" :positions="animals"></CategoryWrapper>
        <CategoryWrapper id="other" name="Другое" :positions="other"></CategoryWrapper>
        <CategoryWrapper id="once" name="Однушки" :positions="once"></CategoryWrapper>
        <CategoryWrapper id="sets" name="Наборы" :positions="sets"></CategoryWrapper>
    </div>
</template>

<script>
const axios = require('axios')
import CategoryWrapper from './../components/CategoryWrapper'
export default {
    name: 'Home',
    components: {
        CategoryWrapper
    },
    mounted: function () {
        axios.get('api/positions?show_sale=0&category=FL').then((response) => { this.flowers = response.data })
        axios.get('api/positions?show_sale=0&category=DO').then((response) => { this.dots = response.data })
        axios.get('api/positions?show_sale=0&category=WO').then((response) => { this.words = response.data })
        axios.get('api/positions?show_sale=0&category=AN').then((response) => { this.animals = response.data })
        axios.get('api/positions?show_sale=0&category=OT').then((response) => { this.other = response.data })
        axios.get('api/positions?show_sale=0&category=ON').then((response) => { this.once = response.data })
        axios.get('api/positions?show_sale=0&category=SE').then((response) => { this.sets = response.data })
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
.slider {
    margin: 44px 80px;
    height: 442px;
}
.slider .paginator {
    display: none;
    justify-content: center;
    margin-top: 8px;
}
.slider .paginator div {
    background-color: white;
    width: 36px;
    height: 8px;
    border: solid 1px #000000;
    margin: 0 8px;
}
.slider .paginator div.active {
    background-color: #DC9EF4;
}
#slide_1 {
    display: grid;
    grid-template-columns: 1fr 0.5fr;
    grid-template-rows: 1fr 1fr;
    grid-column-gap: 21px;
    grid-row-gap: 21px;
    height: calc(100% - 18px);
    width: calc(100%);
}
#slide_1 #gallery_bigpick {
    grid-row-start: 1;
    grid-row-end: 3;
    background-image: url('./../assets/1.jpg');
    background-size: contain;
    background-repeat: no-repeat;
    background-color: transparent;
}
#gallery_bigpick .text-container {
    display: flex;
    padding: 128px 48px;
    background-color: transparent;
    color: white;
    font-size: 2.5rem;
    text-align: left;
}

#slide_1 #pic_2 { background-image: url('./../assets/2.jpg'); }
#slide_1 #pic_3 { background-image: url('./../assets/3.jpg'); }
@media screen and (max-width: 1000px) {
    .slider {margin: 36px 12px; height: 260px;}
    .slider .paginator {display: flex;}
    #slide_1 {
        grid-template-columns: 1fr;
        grid-row-gap: 0; grid-column-gap: 0;
    }
    #gallery_bigpick .text-container {
        padding: 72px 8px;
        font-size: 1.75rem
    }
}
</style>