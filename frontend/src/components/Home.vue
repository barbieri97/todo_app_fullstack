<template>
    <main class="">
        <h1 class="saudacao">Bem vindo ao Todo APP!</h1>
        <h2 class="saudacao">Faça o login ou se cadastre para começar.</h2>
        <div class="auth">
            <RouterLink to="/login"><button class="login">Login</button></RouterLink>
            <RouterLink to="/singup"><button class="singup">cadastre-se</button></RouterLink>
        </div>
    </main>
</template>

<script>
export default {
    name: 'HomeComponent'
}
</script>
<style scoped>

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.saudacao {
    color: var(--color-text-dark);
}

button {
    border-color: var(--color-background-home);
    background-color: var(--color-background-nav);
    border-radius: 15px;
    padding: 10px;
    color: var(--color-text-light);
    box-shadow: 5px 5px 5px black;
    margin: 20px;
}

.auth {
    display: flex;
    justify-content: space-around;
}

</style>