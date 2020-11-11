<template>
<v-app>
  <div id="app">
    <router-view/>
  </div>
</v-app>
</template>

<script>
export default {
  name: 'app',
data () {
return {
markers: [
{ position: { lat: 37, lng: 126.98 } },
{ position: { lat: 37, lng: 126.99 } },
{ position: { lat: 37, lng: 127.00 } },
{ position: { lat: 37, lng: 127.01 } },
{ position: { lat: 37, lng: 127.02 } }
]
}
},
methods: {
addMarker (e) {
const { lat, lng } = e.latLng.toJSON()
this.markers.push({
position: {
lat, lng
}
})
},
panTo (e, map) {
map.panTo(e.latLng)
}
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
