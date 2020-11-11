<template>
  <v-row>
    <v-col
      cols="12"
    >
      <v-card>
        <v-list>
          <v-list-item
            v-for="place in places"
            :key="place.id"
          >
            <v-list-item-avatar>
              <img :src="place.avatar">
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>{{ place.name }}</v-list-item-title>

              <v-list-item-subtitle>{{ place.address }}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <img class="like-btn" :place="place" @click="click_like(place)" v-if="place.like_status" :src="like" alt="">
              <img class="like-btn" :place="place" @click="click_like(place)" v-else :src="dislike" alt="">
            </v-list-item-action>
          </v-list-item>

        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

<style>
.like-btn {
  width: 30px;
  height: auto;
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
    // test() {
    //   alert(this.places[0].name)
    // },
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
