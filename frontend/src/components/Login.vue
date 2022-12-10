<template>
    <main>
        <form @submit.prevent>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Username</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="username">
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword5" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
  </div>
  <button type="submit" class="btn btn-primary" @click="doLogin(username, password)">Submit</button>
</form>
    </main>
</template>

<script>
import api from '@/services/api.js';
import qs from 'qs'

export default {
    name: 'LoginComponent',
    data () {
        return {
            username: "",
            password: ""
        }
    },
    methods: {
      async doLogin () {
        try {
          let res = await api.post('/login', qs.stringify({
            "username": this.username, 
            "password": this.password, 
          }))
          localStorage.setItem('access_token', res.data.access_token)
          this.$router.push('/me')
        }
        catch (error) {
          console.log(error)
        }
        this.username = ""
        this.password = ""


      } 

    }
}
</script>

<style scoped>

</style>
