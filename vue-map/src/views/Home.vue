<template>
  <div class="home">
      <SlideBar/>
      <HelloWorld/>
      <App/>
      <googleMapMarker/>
      <googleMapFactory/>
      <!-- <AppJs/> -->
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import SlideBar from '@/components/SlideBar.vue'
import App from '@/App.vue'
import googleMapFactory from '@/components/map.js'
import googleMapMarker from '@/components/marker.js'
// import AppJs from '@/app.js'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    SlideBar,
    App,
    googleMapMarker,
    googleMapFactory,
    // AppJs
   }
}
</script>