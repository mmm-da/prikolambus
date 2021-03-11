import axios from 'axios'
import constants from '@/constants'

function validateToken (token) {
  try {
    const payload = JSON.parse(
      atob(
        token.split('.')[1]
      )
    )
    return (Date.now() < payload.exp * 1000)
  } catch (error) {
    return false
  }
}

const auth = {
  namespaced: true,
  state: () => ({
    accessToken: localStorage.getItem('accessToken') || null,
    isAuth: validateToken(localStorage.getItem('accessToken')),
    username: localStorage.getItem('username'),
    isAdmin: localStorage.getItem('isAdmin') || false,
    userID: localStorage.getItem('userID') || null
  }),
  actions: {
    login: async ({ commit, state }, payload) => {
      const loginResponse = await axios.post(constants.apiBaseURL + '/token/', { username: payload.username, password: payload.password })
      commit('setAccessToken', loginResponse.data.access)
      commit('setAuthState', true)
      const response = await axios.get(constants.apiBaseURL + '/user/', { headers: { Authorization: `Bearer ${state.accessToken}` } })
      commit('setUsername', response.data.username)
      commit('setAdminState', response.data.is_superuser)
      commit('setUserID', response.data.id)
    },
    logout: ({ commit }) => {
      commit('removeAccessToken')
      commit('removeAdminState')
      commit('removeUsername')
      commit('removeUserID')
      commit('setAuthState', false)
    }
  },
  mutations: {
    setUsername (state, username) {
      state.username = username
      localStorage.setItem('username', username)
    },
    setUserID (state, id) {
      state.userID = id
      localStorage.setItem('userID', id)
    },
    setAdminState (state, adminState) {
      state.isAdmin = adminState
      localStorage.setItem('isAdmin', adminState)
    },
    setAuthState (state, authState) {
      state.isAuth = authState
    },
    setAccessToken (state, token) {
      state.accessToken = token
      localStorage.setItem('accessToken', token)
    },
    removeAccessToken (state) {
      state.accessToken = null
      localStorage.removeItem('accessToken')
    },
    removeAdminState (state) {
      state.isAdmin = null
      localStorage.removeItem('isAdmin')
    },
    removeUserID (state) {
      state.userID = null
      localStorage.removeItem('userID')
    },
    removeUsername (state) {
      state.username = null
      localStorage.removeItem('username')
    }
  }

}

export default auth
