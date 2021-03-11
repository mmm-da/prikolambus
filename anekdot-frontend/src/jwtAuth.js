import constants from '@/constants'
import axios from 'axios'

class Auth {
  accessToken = localStorage.getItem('accessToken')
  refreshToken = localStorage.getItem('refreshToken')

  logout () {
    this.isAuth = false
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
  }

  getAccessToken () {
    if (this.validateToken(this.accessToken)) {
      return this.accessToken
    } else {
      this.accessToken = this.refreshAccessToken()
      if (this.accessToken) {
        return this.accessToken
      } else {
        return null
      }
    }
  }

  refreshAccessToken () {
    if (this.getRefreshToken()) {
      axios.post(this.refreshEndpoint, `{ ${this.refreshTokenFieldName}: ${this.refreshToken} }`)
        .then(response => {
          localStorage.setItem('accessToken', response.data.access)
          return response.data.access
        })
    } else {
      return null
    }
  }

  getRefreshToken () {
    if (this.validateToken(this.refreshToken)) {
      return this.refreshToken
    } else {
      this.logout()
      return null
    }
  }

  getAxios () {
    return axios.create({
      baseURL: constants.apiBaseURL,
      timeout: 1000,
      headers: { Authorization: `Bearer ${this.getAccessToken()}` }
    })
  }
}

const auth = new Auth(constants.apiBaseURL + '​/token​/refresh​/')
console.log('auth created')

export default auth
