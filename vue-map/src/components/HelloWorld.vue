<template>
  <v-container id="map" style="margin: 0px; padding: 0px">
  <GmapMap ref="mapRef"
  :zoom="15"
  :center="{lat:10, lng:10}"
  map-type-id="terrain"
  style="width: 100vw; height: 100vh"
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
  <PostList/>
  </v-container>  
</template>

<script>
import PostList from './PostList'

var lat1, lng1;
var post1 = "postPost"

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
      lat: 37.5682,
      lng: 126.9977
      }
    }]
  };
 },
 components: {
   PostList
 },
 mounted () {
    this.$refs.mapRef.$mapPromise.then((map) => {
      map.panTo({lat: lat1, lng: lng1})
    })
},
 methods: {
 
  clickMarker: function () {  
    this.$dialog.confirm({
        text: 
        "<div>제목</div> <input id='title'></input><br>\
        <div>내용</div> <input id='description'></input><br>\
        <button v-on:click=" + post1 + ">게시</button>",
        title: "asd"
    });   
  }
 }
}
</script>