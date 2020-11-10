<template>
  <v-container id="map" style="margin: 0px; padding: 0px">
    <GmapMap ref="mapRef"
    :zoom="15"
    :center="{lat:37.506, lng:126.98}"
    map-type-id="roadmap"
    style="width: 100vw; height: 95vh"
    @click="addMarker"
    >
  
    <GmapMarker
    v-for="m in markers"
    :key= "m.key"
    :position="m.position"
    :clickable="true"
    :draggable="false"
    @click="$EventBus.$emit('open-modal')"
    />
  </GmapMap>
  <MyModal/>
  </v-container>  
</template>

<script>
import MyModal from './MyModal'

  var lat1, lng1;

  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(
      function(pos) {
        lat1 = pos.coords.latitude;
        lng1 = pos.coords.longitude;
        alert("현재 위치는 : " + lat1 + ", "+ lng1);
    });
  }else {
      alert('GPS를 지원하지 않습니다');
  }
  export default {
    name: 'app',
    data () {
    return {
      clientPos: {
        lat: 0.0,
        lng: 0.0
      },
      markers: [
      { position: { lat: 37.5, lng: 126.98 } },
      { position: { lat: 37.5, lng: 126.99 } },
      { position: { lat: 37.5, lng: 127.00 } },
      { position: { lat: 37.5, lng: 127.01 } },
      { position: { lat: 37.5, lng: 127.02 } }
      ]
      };
    },
    components: {
      MyModal
    },
    mounted () {
      this.getClientPosition()
      this.$refs.mapRef.$mapPromise.then((map) => {
        map.panTo(this.clientPos)
      })
    },
    methods: {
      getClientPosition(){
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
          this.clientPos.lat = pos.coords.latitude
          this.clientPos.lng = pos.coords.longitude
        })
      } else {
        alert('GPS system is not working properly')
      }
    },
    addMarker (e) {
      let newMarker = {
        position: {
          lat: e.latLng.lat(),
          lng: e.latLng.lng()
        },
        key: e.vb.timestamp
      }
      this.markers.pop()
      this.markers.push(newMarker)
    },
    removeMarker (e) {
      // complete this part to remove our markers
      console.log(e.vb)
    },
      clickMarker () {

      }
  }
}
</script>