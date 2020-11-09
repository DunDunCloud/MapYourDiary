<template>
  <div class="home">
      <SlideBar/>
      <HelloWorld/>
      <PostList/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import SlideBar from '@/components/SlideBar.vue'
import PostList from '@/components/PostList.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    SlideBar,
    PostList
   }
}
</script>