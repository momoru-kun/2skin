<template>
    <div class="category" v-bind:class="{dense: hide_titles}" v-if="positions.length > 0">
        <div class="category_name" v-if="!hide_titles" > {{hide_titles}} {{ name }}</div>
        <div class="goods_wrapper">
            <div class="card" v-for="item in positions" :key="item.name">
                <img width="232px" height="300px" v-bind:src="item.image"/>
                <div class="name"> {{ item.name }} </div>
                <div class="price" v-if="!show_sale"> {{ item.price }} Р </div>
                <div class="price sale" v-if="show_sale"> <span class="old-price">{{ item.price }} Р</span> {{ item.sale_price }} Р  </div>
                <div class="button" @click="addToCart({amount:1, position: item})">В КОРЗИНУ</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['name', 'positions', 'hide_titles', 'show_sale'],
    methods: {
        addToCart: function(item) {
            this.$store.dispatch('add_to_cart', item)
        }
    }
}
</script>

<style scoped>
.category {
    margin: 100px 0 64px 0;
    text-align:left;
}
.category.dense {
    margin: 50px 0 32px 0;
}
.category_name {
    font-size: 2rem;
    padding-left: 100px;
    margin-bottom: 16px;
    text-transform: uppercase;
}
.goods_wrapper {
    display: grid;
    grid-auto-flow: row;
    grid-template-columns: repeat(4, 1fr);
    width: 100%;
    grid-column-gap: 20px;
    grid-row-gap: 36px; 
}
.card:hover {
    transform: scale(1.05) translateY(-10px);
}
.card {
    position: relative;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: .3s ease-in-out;
}
.card img {
    margin: 0 auto;
}
.card .name {
    font-size: 1.3rem;
    text-transform: uppercase;
    text-align: center;
}
.card .price {
    font-size: 1.2rem;
    margin: 10px 0;
}
.card .price.sale {
    color: #ff0000;
}
.card .price .old-price {
    font-size: .7em;  
    color: #000000;
    
    text-decoration: line-through;
}

.card .button {
    font-size: 1.25rem;
    margin: 10px auto 0 auto;
    background-color: #e5b6f7;
    padding: 1rem 4.375rem;
    width: fit-content;
    transition: .3s;
    bottom: 0;
}
.card .button:hover {
    background-color: #DC9EF4;
    cursor: pointer;
}
@media screen and (max-width: 1000px) {
    .category {
        margin: 32px 8px 32px 8px;
    }
    .goods_wrapper {
        overflow-x: auto;
        overflow-y: none;
        grid-auto-flow: column;
        grid-column-gap: 4px;
    }
    .card:hover {
        transform: none;
    }
    .card .button {
        font-size: 1rem;
        padding: 18px 4rem;
    }
    .category_name {
        font-size: 2rem;
        padding-left: 32px;
    }
}
</style>