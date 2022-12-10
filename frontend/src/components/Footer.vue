<template>
    <footer>
        <a href="/"><img src="https://raw.githubusercontent.com/william-costa/wdev-mock-site-resources/master/assets/icons/instagram.svg" alt="instagram"></a>
        <a href="/"><img src="https://raw.githubusercontent.com/william-costa/wdev-mock-site-resources/master/assets/icons/facebook.svg" alt="facebook"></a>
        <a href="/"><img src="https://raw.githubusercontent.com/william-costa/wdev-mock-site-resources/master/assets/icons/twitter.svg" alt="twitter"></a>
    </footer>
</template>

<script>

export default {
    name:'MyFooter'
}
</script>

<style scoped>

footer{
    background-color: var(--color-background-nav);
    width: 100%;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
}
a{
    margin-right: 10px;
}
img{
    width: 20px;
}

</style>