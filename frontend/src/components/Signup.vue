<template>
    <main>
        <form>
  <div class="mb-3">
    <label for="exampleInputUser1" class="form-label">Username</label>
    <input type="text" class="form-control" id="exampleInputUser1" aria-describedby="emailHelp" v-model="username">
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="username">
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword5" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
    </main>
</template>

<script>
export default {
    name: 'SignupComponent',
    data () {
        return {
            username: "",
            password: ""
        }
    },
    methods: {

    }
}
</script>

<style scoped>

</style>