<template>
 <div>
<!-- <p v-for="(post, index) in postsPlace" :key="index">
        {{ post.id }} <br>
        {{ post.title }} <br>
        {{ post.description  }} <br><br>
</p> -->
<b-card no-body header="Card with flush list group">
    <b-list-group flush v-for="(post, index) in postsPlace" :key="index">
      <b-list-group-item href="#">{{ post.id }}</b-list-group-item>
      <b-list-group-item href="#">{{ post.title }}</b-list-group-item>
      <b-list-group-item href="#">{{ post.description }}</b-list-group-item>
    </b-list-group>

    <b-card-body>
      Quis magna Lorem anim amet ipsum do mollit sit cillum voluptate ex nulla tempor. Laborum
      consequat non elit enim exercitation cillum aliqua consequat id aliqua. Esse ex consectetur
      mollit voluptate est in duis laboris ad sit ipsum anim Lorem.
    </b-card-body>
  </b-card>
</div>

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
    })
  }
}
</script>
