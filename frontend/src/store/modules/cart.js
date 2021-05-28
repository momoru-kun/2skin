import axios from 'axios'
export default {
    state: {
        cart: [],
    }, 
    actions: {
        add_to_cart({ commit }, item) {
            return new Promise((resolve, reject) => {
                let params = {
                    method: 'post',
                    data: {id: item.position.id, amount: 1},
                } 
                axios('/api/cart.add', params).then((response) => {
                    commit('add_to_cart', item)
                    this.dispatch('show_notification', `Товар "${item.position.name}" добавлен в корзину!`)
                    resolve(response)
                }).catch(response => {
                    reject(response)
                }) 
            })
        },
        init_cart({ commit }) {
            return new Promise((resolve, reject) => {
                let params = {
                    method: 'get',
                } 
                axios('/api/cart.get', params).then((response) => {
                    commit('init_cart', response.data)
                    resolve(response)
                }).catch(response => {
                    reject(response)
                }) 
            })
        },
        remove_from_cart({ commit }, item) {
            let index = item.position.id
            return new Promise((resolve, reject) => {
                axios.post('/api/cart.remove', {position_id: item.position.id}).then(response => {
                    console.log("Index:", index)
                    commit('remove_from_cart', index)
                    resolve(response)
                }).catch(response => {
                    reject(response)
                })
            })
        },
        change_amount({ commit }, item) {
            return new Promise((resolve, reject) => {
                console.log(item.amount)
                axios.post('/api/cart.amount', {position_id: item.item.position.id, amount: item.amount}).then(response => {
                    commit('change_position_amount', item)
                    resolve(response)
                }).catch(response => {
                    reject(response)
                })
            })
        }
    },
    mutations: {
        add_to_cart(state, item) {
            let founded = false
            for (let cart_item of state.cart) {
                if (cart_item.position.id == item.position.id) {
                    cart_item.amount += item.amount
                    founded = true
                    break
                }
            } 
            if (!founded) state.cart.push(item)
        },
        remove_from_cart(state, index) {
            for (let item in state.cart) {
                console.log(item, index)
                if (state.cart[item].position.id == index){
                    console.log(state.cart.splice(item, 1))
                    console.log("splice")
                }
            }
            
        },
        change_position_amount(state, item) {
            state.cart.forEach(position => {
                if (position.position.id == item.item.position.id) {
                    position.amount = item.amount
                }
            })
        },
        init_cart(state, cart) {
            state.cart = cart
        }
    },
    getters: {
        cart: state => state.cart,
        cart_amount: state => state.cart.length
    }
}