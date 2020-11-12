<template>
  <v-card class="pa-2" outlined>
    <v-btn @click="onClose">Close</v-btn>
  <card-content>
      <v-card-actions>
        <v-btn color="primary" class="ma-2" v-on:click="test">
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
  </v-card>
</template>

<script>
export default {
  data: function(){
    return {
      markerPopup: false
    }
  },
  methods: {
    test() {
      console.log('테스트');
    }
  }
  // created() {
  //   // this.$EventBus.$on('open-marker-popup', () => {
  //     this.markerPopup = true;
  //   // });
  // }
}
</script>