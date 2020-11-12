<template>
  <v-row justify="center">
    <v-expansion-panels accordion>
      <v-expansion-panel
        v-for="place in places"
        :key="place.id"
      >
        <v-expansion-panel-header>{{ place.name }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <p>{{ place.address }}</p>
          <v-col>
            <img :src="place.avatar">
            <v-row>
              <v-btn color="primary" class="ma-2" v-on:click="test">
                상세정보
              </v-btn>
              <v-btn depressed color="primary" v-on:click="test">
                글쓰기
              </v-btn>
              <v-btn depressed color="primary" v-on:click="test">
                길찾기
              </v-btn>
            </v-row>
            <v-row>
              <img class="like-btn" :place="place" @click="click_like(place)" v-if="place.like_status" :src="like" alt="">
              <img class="like-btn" :place="place" @click="click_like(place)" v-else :src="dislike" alt="">
            </v-row>
          </v-col>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-row>
</template>

<style>
.like-btn {
  width: 30px;
  height: auto;
}
.like-btn {
  cursor: pointer;
}
</style>

<script>
import heart from '@/assets/img/heart.png'
import heartNo from '@/assets/img/heart_n.png'


export default {
  name: 'PlaceCard',
  data () {
    return {
      like: heart,
      dislike: heartNo,
      places: [
        { id:0, avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg', name: '경복궁', address: '서울특별시 종로구 세종로 사직로 161', like_status: false },
        { id:1, avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg', name: '창경궁', address: '서울특별시 종로구 세종로 사직로 161', like_status: false  },
        { id:2, avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg', name: '덕수궁', address: '서울특별시 종로구 세종로 사직로 161', like_status: false  },
      ],
    }
  },
  methods: {
    test() {
      console.log(this.places[0].name)
    },
    // 좋아요
    click_like(place) {
      if (place.like_status) {
        place.like_status = false;
        // db에 값 변경 or 추가
      } else {
        place.like_status = true;
        // db에 값 변경 or 추가
      }
    }
  }
}
</script>
