<template>
    <div id="shopping_cart">
        <div class="heading"> КОРЗИНА </div>
        <div class="main_wrapper">
            <div class="cart_wrapper"> 
                <div class="cart_entry" v-for="item in cart" :key="item.position.name"> 
                    <div class="title">
                        <img width="88px" height="120px" v-bind:src="item.position.image">
                        <div class="name">{{ item.position.name }}</div>
                    </div>
                    <div class="delete_btn" @click="$store.dispatch('remove_from_cart', item, item.position.id)"> 
                        <svg width="24" height="26" viewBox="0 0 24 26"  xmlns="http://www.w3.org/2000/svg">
                            <g clip-path="url(#clip0)">
                                <path d="M15.3101 9.0733C14.9997 9.0733 14.748 9.33585 14.748 9.6598V20.7446C14.748 21.0683 14.9997 21.3311 15.3101 21.3311C15.6206 21.3311 15.8722 21.0683 15.8722 20.7446V9.6598C15.8722 9.33585 15.6206 9.0733 15.3101 9.0733Z" />
                                <path d="M8.67827 9.0733C8.36782 9.0733 8.11621 9.33585 8.11621 9.6598V20.7446C8.11621 21.0683 8.36782 21.3311 8.67827 21.3311C8.98872 21.3311 9.24033 21.0683 9.24033 20.7446V9.6598C9.24033 9.33585 8.98872 9.0733 8.67827 9.0733Z" />
                                <path d="M3.84439 7.45559V21.9056C3.84439 22.7597 4.14452 23.5618 4.66881 24.1373C5.19069 24.7144 5.91698 25.042 6.67708 25.0434H17.3114C18.0717 25.042 18.798 24.7144 19.3197 24.1373C19.844 23.5618 20.1441 22.7597 20.1441 21.9056V7.45559C21.1863 7.16693 21.8617 6.11627 21.7223 5.00033C21.5826 3.88461 20.6717 3.05 19.5932 3.04977H16.7155V2.31665C16.7188 1.70014 16.4852 1.10814 16.067 0.672624C15.6487 0.237333 15.0805 -0.0050547 14.4897 -1.44919e-05H9.49879C8.90797 -0.0050547 8.33976 0.237333 7.92151 0.672624C7.50326 1.10814 7.26965 1.70014 7.27295 2.31665V3.04977H4.39525C3.3168 3.05 2.40587 3.88461 2.26623 5.00033C2.12681 6.11627 2.80216 7.16693 3.84439 7.45559ZM17.3114 23.8704H6.67708C5.71609 23.8704 4.9685 23.009 4.9685 21.9056V7.50714H19.02V21.9056C19.02 23.009 18.2724 23.8704 17.3114 23.8704ZM8.39707 2.31665C8.39333 2.01126 8.50838 1.71732 8.71608 1.50174C8.92356 1.28615 9.2059 1.16771 9.49879 1.17298H14.4897C14.7826 1.16771 15.0649 1.28615 15.2724 1.50174C15.4801 1.71709 15.5952 2.01126 15.5914 2.31665V3.04977H8.39707V2.31665ZM4.39525 4.22276H19.5932C20.152 4.22276 20.6049 4.69539 20.6049 5.27845C20.6049 5.86151 20.152 6.33415 19.5932 6.33415H4.39525C3.83648 6.33415 3.38354 5.86151 3.38354 5.27845C3.38354 4.69539 3.83648 4.22276 4.39525 4.22276Z" />
                                <path d="M11.9942 9.0733C11.6837 9.0733 11.4321 9.33585 11.4321 9.6598V20.7446C11.4321 21.0683 11.6837 21.3311 11.9942 21.3311C12.3046 21.3311 12.5562 21.0683 12.5562 20.7446V9.6598C12.5562 9.33585 12.3046 9.0733 11.9942 9.0733Z" />
                            </g>
                            <defs>
                                <clipPath id="clip0">
                                    <rect width="24" height="25.0435" fill="white"/>
                                </clipPath>
                            </defs>
                        </svg>
                    </div>
                    <div class="amount">
                        <div class="minus" @click="$store.dispatch('change_amount', {item: item, amount: item.amount-1})"> - </div>
                        <div class="numeric">{{ item.amount }}</div>
                        <div class="plus" @click="$store.dispatch('change_amount', {item: item, amount: item.amount+1})"> + </div>
                    </div>
                    <div class="price" v-if="item.position.sale_price != null">
                        <span> {{ item.position.price*item.amount }} Р </span><br>
                        {{ item.position.sale_price }} Р
                    </div>
                    <div class="price" v-if="item.position.sale_price == null">
                        {{ item.position.price*item.amount }} Р
                    </div>
                </div>
            </div>
            <div class="order_wrapper">
                <div class="heading"> Оформить заказ </div>
                <div class="items_amount">
                    У вас {{ calcPositions }} товаров<br><br>На сумму {{ calcPrice }} Рублей<br>
                </div>
                <hr color="#000000">
                <div class="heading" style='text-align: left'> Промокод </div>
                <input type="text" v-model="promo" placeholder="Промокод"/> <div class="button" v-bind:class="{inactive:promo==null}" @click="checkPromo()"> Применить </div>
                <div class="items_amount" v-if="promo_profit != null" style="margin: 12px 4px;"> Скидка: {{ calcPrice * promo_profit }} </div> 
                <div class="summary" v-if="promo_profit != null" style="font-size:2.5rem; color:#DC9EF4; text-align:left; margin: 8px 12px"> ИТОГО: {{calcPrice * (1 - promo_profit)}}</div>
                <div class="summary" v-if="promo_profit == null" style="font-size:2.5rem; color:#DC9EF4; text-align:left; margin: 8px 12px"> ИТОГО: {{calcPrice}}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
mounted: function() {
    console.log(this.cart)
},
data: () => ({
    promo: null,
    promo_profit: null
}),
methods: {
    checkPromo: function() {
        axios.post('/api/promo.check', {promo:this.promo}).then((response) => {
            let status = response.data.status
            if (status == 'no promo') this.$store.dispatch('show_notification', 'Промокод не существует')
            if (status == 'expiried') this.$store.dispatch('show_notification', 'Срок действия промокода истёк')
            if (status == 'activated') this.$store.dispatch('show_notification', 'Промокод уже активирован')
            if (status == 'active') {
                this.promo_profit = response.data.percent / 100
                this.$store.dispatch('show_notification', 'Промокод принят')
            }
        })
    }
},
computed: {
    cart: function () {
        return this.$store.getters.cart
    },
    calcPositions: function () {
        let amount = 0
        this.cart.forEach(item => {
            amount += item.amount
        });
        return amount
    },
    calcPrice: function () {
        let price = 0
        this.cart.forEach(item => {
            let item_price = item.position.sale_price !== null ? item.position.sale_price : item.position.price  
            price += item_price * item.amount
        })
        return price
    }
}
}
</script>

<style scoped>
.heading {
    font-size: 1.75rem;
    margin: 2rem
}
.main_wrapper {
    display: flex;
    flex-direction: row;
    margin-bottom: 24px;
    gap: 12px;
}
.cart_wrapper {
    display: flex;
    flex-direction: column;
    gap: 12px;
    width: 800px;
}
.cart_entry {
    border: 2px solid #000000;
    padding: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.cart_entry div.title {
    display: flex;
    align-items: center;
    width: 350px;
    text-align: left;
}
.cart_entry .name {
    padding-left: 8px;
    font-size: 1.25rem;
    text-transform: uppercase;
}

.cart_entry .delete_btn {
    transition: .3s;
}

.cart_entry .delete_btn:hover {
    fill: #EE1B1B;
    cursor: pointer;
}

.cart_entry .amount {
    display: flex;
    font-size: 1.5rem;
    border: 2px solid #000000;
}

.cart_entry .amount div {
    padding: 1rem 1.5rem;
    transition: .3s;
}

.cart_entry .amount .minus {
    border-right: 2px solid #000;
}
.cart_entry .amount .minus:hover, .cart_entry .amount .plus:hover {cursor: pointer; background-color: #DC9EF4; color: white;}


.cart_entry .amount .plus {
    border-left: 2px solid #000;
}

.cart_entry .price {
    font-size: 1.5rem;
    color: #DC9EF4;
}

.cart_entry .price span {
    font-size: 0.75em;
    color: #000000;
    text-decoration: line-through;
}
.order_wrapper {
    border: 2px solid #000000;
    width: 388px;
    height: fit-content;
    padding-bottom: 12px;
}

.order_wrapper .items_amount {
    font-size: 1.25rem;
    text-align: left;
    padding: 0 12px;
}

input[type="text"] {
    outline: none;
    border: 1px solid #c4c4c4;
    border-radius: 0;
    font-size: 1.5rem;
    padding: 6px 8px;
    margin: 0 8px;
    transition: .3s;
}

input[type="text"]:focus {
    border: 1px solid #000000;
}
.button {
    display: inline;
    font-size: 1.25rem;
    padding: 8px 12px;
    background-color: #E7B8F5;
    transition: .3s;
}
.button:hover {
    background-color: #DC9EF4;
    cursor: pointer;
}
.button.grey {
    background-color: #c4c4c4;
}
.button.grey {
    background-color: #cccccc;
}

@media screen and (max-width: 1000px) {
    .main_wrapper {
        flex-direction: column;
    }
    .cart_wrapper {width: 100vw}
    .cart_entry {
        padding: 12px 2px;
        width: calc(100% - 8px);
    }
    .cart_entry div.title {
        flex-direction: column;
        width: 144px;
    }
    .cart_entry .amount div {
        padding: 0.25rem 0.75rem;
    }
    .cart_entry .name {
        font-size: 1rem;
    }
    .order_wrapper { 
        width: calc(100vw - 4px);
    }
    .button {display: block; width: 100px; margin: 16px auto}
}
</style>