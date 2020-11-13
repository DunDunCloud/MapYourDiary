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
<!--              <img :src="place.avatar">-->
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>{{ place.title }}</v-list-item-title>

              <v-list-item-subtitle>{{ place.description }}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <img class="like-btn" :place="place" @click="click_like(place)" v-if="place.published" :src="like" alt="">
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
.like-btn {
  cursor: pointer;
}
</style>

<script>
import heart from '@/assets/img/heart.png'
import heartNo from '@/assets/img/heart_n.png'
import axios from "axios";

export default {
  name: 'PlaceCard',

  data: () => {
    return {
      like: heart,
      dislike: heartNo,
      places: [],
    }
  },
  methods: {
    // 좋아요
    click_like(place) {
      if (place.published) {
        place.published = false;
        // db에 값 변경 or 추가
      } else {
        place.published = true;
        // db에 값 변경 or 추가
      }
    },
    getPost (){
      axios.get("http://127.0.0.1:8000/api/diary", {auth: {
          username: "admin",
          password: "admin",
      }})
      .then(response => {
          console.log(response.data);
          this.places=response.data;
          this.$EventBus.$on('get-post', () => {
            this.getPost();
          })
      })
      .catch(error => {
          console.log(error)
      });
    },
  },
  created() {
      this.getPost();
  }
}
</script>
