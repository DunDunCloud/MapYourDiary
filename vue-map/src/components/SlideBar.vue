<template>
<div>
  <b-navbar type="dark" variant="dark">
    <div>
      <b-navbar-nav>
        <b-nav-item href="#">Map Your Diary</b-nav-item>
        <b-button v-b-toggle.sidebar-variant1>내 정보</b-button>
        <b-button v-b-toggle.sidebar-variant2>장소</b-button>
        <b-button v-b-toggle.sidebar-variant3>친구</b-button>
        <b-button v-b-toggle.sidebar-variant4>Test</b-button>

        <div v-if="!$auth.loading">
          <!-- show login when not authenticated -->
          <b-button v-if="!$auth.isAuthenticated" @click="login">Log in</b-button>
          <!-- show logout when authenticated -->
          <b-button v-if="$auth.isAuthenticated" @click="logout">Log out</b-button>
          <!-- <router-link to="/external-api">External Api</router-link> -->
        </div>
      </b-navbar-nav>
    </div>
      <b-sidebar id="sidebar-variant1" title="내 정보" bg-variant="dark" text-variant="light" shadow>
        <div class="px-3 py-2">
          <p v-if="$auth.isAuthenticated">
            <Profile/>
          </p>
        </div>
      </b-sidebar>

      <b-sidebar id="sidebar-variant2" title="장소" bg-variant="dark" text-variant="light" shadow>
        <div class="px-3 py-2">
          <p>
            여기에 장소 목록!   여기에 장소 목록!   여기에 장소 목록!   여기에 장소 목록!   여기에 장소 목록!
          </p>
        </div>
      </b-sidebar>

      <b-sidebar id="sidebar-variant3" title="친구" bg-variant="dark" text-variant="light" shadow>
        <div class="px-3 py-2">
          <p>
            여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!
          </p>
        </div>
      </b-sidebar>

      <b-sidebar id="sidebar-variant4" title="Test" bg-variant="dark" text-variant="light" shadow>
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

export default {
  name: 'SlideBar',
  components: {
    Profile
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