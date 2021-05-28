export default {
    actions: {
        show_notification({ commit }, notification) {
            return new Promise((resolve) => {
                commit('show_notification', notification)
                resolve(true)
            })
        }
    }, 
    mutations: {
        show_notification(state, notification)
        { 
            state.notifications.push({text: notification})

            setTimeout(() => {state.notifications.pop()}, 5000)
        }
    },
    state: {
        notifications: []
    },
    getters: {
        notifications: state => state.notifications
    }
}