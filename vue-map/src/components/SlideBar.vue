<template>
<div>
  <b-navbar>
    <div>
      <b-navbar-nav>
        <b-nav-item href="#">Map Your Diary</b-nav-item>
        <b-button v-b-toggle.sidebar-variant2 variant="link">장소</b-button>
        <b-button v-b-toggle.sidebar-variant3 variant="link">친구</b-button>
        <b-button v-b-toggle.sidebar-variant4 variant="link">Test</b-button>

        <div v-if="!$auth.loading">
          <!-- show login when not authenticated -->
          <b-button v-if="!$auth.isAuthenticated" @click="login" variant="link">Log in</b-button>
          <!-- show logout when authenticated -->
          <b-button v-b-toggle.sidebar-variant1 v-if="$auth.isAuthenticated" variant="link">내 정보</b-button>
          <b-button v-if="$auth.isAuthenticated" @click="logout" variant="link">Log out</b-button>
          <!-- <router-link to="/external-api">External Api</router-link> -->
        </div>
      </b-navbar-nav>
    </div>
      <b-sidebar id="sidebar-variant1" title="내 정보" shadow>
        <div class="px-3 py-2">
          <p v-if="$auth.isAuthenticated">
            <Profile/>
          </p>
        </div>
      </b-sidebar>

      <b-sidebar id="sidebar-variant2" title="장소" shadow>
        <div class="px-3 py-2">
          <p>
            <PostList/>
          </p>
        </div>
      </b-sidebar>

      <b-sidebar id="sidebar-variant3" title="친구" shadow>
        <div class="px-3 py-2">
          <p>
            여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!
          </p>
        </div>
      </b-sidebar>

      <b-sidebar id="sidebar-variant4" title="Test" shadow>
        <div class="px-3 py-2">
          <p>
            여기에 넣고 싶은거!   여기에 넣고 싶은거!   여기에 넣고 싶은거!   여기에 넣고 싶은거!   여기에 넣고 싶은거!
          </p>
        </div>
      </b-sidebar>
  </b-navbar>
</div>
</template>

<style scoped>
#navbar-100{
  z-index: 300;
}
</style>

<script>
import Profile from '@/views/Profile.vue'
import PostList from '@/components/PostList.vue'

export default {
  name: 'SlideBar',
  components: {
    Profile,
    PostList
  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    },
    // Log the user out
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin
      });
    }
  }
}
</script>

