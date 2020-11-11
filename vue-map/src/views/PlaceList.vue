<template>
 <!-- <div>
<p v-for="(post, index) in postsPlace" :key="index">
        {{ post.id }} <br>
        {{ post.title }} <br>
        {{ post.description  }} <br><br>
</p>
</div> -->
  <v-row>
     {{ dislike }}
    <v-col>
      <v-card>
        <v-list>
          <v-list-item-group>
          <v-list-item v-for="post in postsPlace" :key="post.id">
            {{post.id}}
            <!-- <v-list-item-avatar>
               <img :src="place.avatar"> 
            </v-list-item-avatar>

            <v-list-item-content> -->
            {{ post.id }}
            {{ post.title }}
            {{ post.description }}
              <!-- <v-list-item-title>{{ post.title }}</v-list-item-title>
              <v-list-item-subtitle>{{ post.description }}</v-list-item-subtitle>
            </v-list-item-content> -->
            <v-list-item-action>
              <img class="like-btn" :place="place" @click="click_like(place)" v-if="place.like_status" :src="like" alt="">
              <img class="like-btn" :place="place" @click="click_like(place)" v-else :src="dislike" alt="">
            </v-list-item-action>
          </v-list-item>
          </v-list-item-group>
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

let postsPlace2 = []
export default {
  name: 'PlaceCard',

  data: () => {
    return {
      like: heart,
      dislike: heartNo,
      postsPlace: []
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
  },
  created () {
    this.$EventBus.$on("post-list", posts  => {
      this.postsPlace = posts
      console.log(posts)
      console.log(this.postsPlace)
      console.log(postsPlace2)
      console.log(this.dislike)
      this.dislike = 'test'
      console.log(this.dislike)
    })
  }
}
</script>
