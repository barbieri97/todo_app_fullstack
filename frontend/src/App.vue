<template>
  <Header />  
  <router-view/>
  <Footer />
</template>

<script>
import '@/styles/global.css'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  components: {
    Header,
    Footer
  }
}
</script>
