<template>
  <v-container id="map" style="margin: 0px; padding: 0px">
  <GmapMap ref="mapRef"
  :zoom="15"
  :center="{lat:10, lng:10}"
  map-type-id="roadmap"
  style="width: 100vw; height: 95vh"
  >
  <GmapMarker
   :key="index"
   v-for="(m, index) in markers"
   :position="m.position"
   :clickable="true"
   :draggable="true"
   @click="clickMarker"
  /> 
  </GmapMap> 
  </v-container>  
</template>

<script>
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
  name: 'HelloWorld',
  data() {
    return {
    markers: [{
      position: {
      lat: 10.0,
      lng: 10.0
      }
    }, {
     position: {
      lat: 11.0,
      lng: 11.0
     }
    }]
  };
 },
 mounted () {
    this.$refs.mapRef.$mapPromise.then((map) => {
      map.panTo({lat: lat1, lng: lng1})
    })
},
 methods: {
  clickMarker: function () {  
      this.$dialog.confirm({
         text: "What's your name? <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Natgeologo.svg/1200px-Natgeologo.svg.png' height=100/><input value='input'></input>", title: 'Warning'});   
  }
 }
}
</script>