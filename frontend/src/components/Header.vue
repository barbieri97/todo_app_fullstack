<template>
    <header>
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start first">
            <RouterLink to="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
                <img class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap" src="../assets/blue_check-removebg-preview.png">
            </RouterLink>

      <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
        <li><RouterLink to="/" class="nav-link px-2 text-white">Home</RouterLink></li>
        <li><RouterLink to="/about" class="nav-link px-2 text-white">About</RouterLink></li>
      </ul>

      <div class="text-end">
          <RouterLink to="/login"><button type="button" class="btn btn-outline-light me-2">Login</button></RouterLink>
        <RouterLink to="/signup"><button type="button" class="btn btn-warning">Sign-up</button></RouterLink>
    </div>
    </div>
</header>
</template>

<script>
export default {
    name: 'HeaderComponent'
}
</script>

<style scoped>
header {
    display: flex;
    background-color: var(--color-background-nav);
    padding: 5px;
    height: 60px;
    justify-content: center;
}

.first {
    width: 100%;
    padding-inline: 10px;
}
</style>