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
    :draggable="true"
    @click="removeMarker"
    /> 
  </GmapMap>
  </v-container>  
</template>

<script>
  let lat1, lng1;
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
  // addMarker (e) {
  // const { lat, lng } = e.latLng.toJSON()
  // this.markers.push({
  // position: {
  // lat, lng
  // }
  // })
  // },
  // panTo (e, map) {
  // map.panTo(e.latLng)
  // }
    },
    addMarker (e) {
      let newMarker = {
        position: {
          lat: e.latLng.lat(),
          lng: e.latLng.lng()
        },
        key: e.vb.timestamp
      }
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

  // export default {
  //   name: 'HelloWorld',
  //   data() {
  //     return {
  //     markers: [{
  //       position: {
  //       lat: 10.0,
  //       lng: 10.0
  //       }
  //     }, {
  //      position: {
  //       lat: 11.0,
  //       lng: 11.0
  //      }
  //     }]
  //   };
  //  },
  //  mounted () {
  //     this.$refs.mapRef.$mapPromise.then((map) => {
  //       map.panTo({lat: lat1, lng: lng1})
  //     })
  // },
  //  methods: {
  //   clickMarker: function () {  
  //       this.$dialog.confirm({
  //          text: "What's your name? <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Natgeologo.svg/1200px-Natgeologo.svg.png' height=100/><input value='input'></input>", title: 'Warning'});   
  //   }
  //  }
  // }
</script>