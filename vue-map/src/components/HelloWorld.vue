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
<!--      $EventBus.$emit('open-modal')-->
<!--    <MarkerBtns/>-->
<!--    @click="toggleInfoWindow(m,m.key)"-->
    <gmap-info-window
      :options="infoOptions"
      :position="infoWindowPos"
      :opened="infoWinOpen"
      @closeclick="infoWinOpen=false"
    >
<!--      <div v-html="infoContent"></div>-->
    </gmap-info-window>
  </GmapMap>
  <MyModal/>
<!--    <Modal2/>-->
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
      infoContent: '',
      infoWindowPos: {
        lat: 0,
        lng: 0
      },
      infoWinOpen: false,
      currentMidx: null,
      //optional: offset infowindow so it visually sits nicely on top of our marker
      infoOptions: {
        pixelOffset: {
          width: 0,
          height: -35
        }
      },
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
      MyModal,
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
      openSidebar(marker, idx) {
        let m = marker
        let i = idx
        console.log(m, i)
        this.$refs.placesidebar.open;
      },
      toggleInfoWindow(marker, idx) {
        this.infoWindowPos = marker.position;
        this.infoContent = this.getInfoWindowContent();

        //check if its the same marker that was selected if yes toggle
        if (this.currentMidx == idx) {
          this.infoWinOpen = !this.infoWinOpen;
        }
        //if different marker set infowindow to open and reset current marker index
        else {
          this.infoWinOpen = true;
          this.currentMidx = idx;
        }
      },
      getInfoWindowContent() {
        return (`<v-card class="pa-2" outlined>
    <v-btn @click="onClose">Close</v-btn>
  <card-content>
      <v-card-actions>
        <v-btn color="primary" class="ma-2" @click="showmodal = true">
          상세정보
        </v-btn>
        <v-btn depressed color="primary" v-on:click="test">
          글쓰기
        </v-btn>
        <v-btn depressed color="primary" v-on:click="test">
          길찾기
        </v-btn>
      </v-card-actions>
  </card-content>
  </v-card>`)
      },
  }
}
</script>
