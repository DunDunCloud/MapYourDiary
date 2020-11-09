<template>
<div>
  <b-navbar>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#"><b>Map Your Diary</b></b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="onSubmit">
          <b-form-input v-model="place" size="sm" class="mr-sm-2" placeholder="장소 검색"></b-form-input>
          <b-button variant="info" size="sm" class="my-2 my-sm-0" type="submit">검색</b-button>
        </b-nav-form>
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
    </b-collapse>
      <b-sidebar bg-variant="white" id="sidebar-variant1" title="내 정보" width="400px" shadow>
        <div class="px-3 py-2">
          <p v-if="$auth.isAuthenticated">
            <Profile/>
          </p>
        </div>
      </b-sidebar>

      <b-sidebar bg-variant="white" id="sidebar-variant2" title="장소" width="400px" shadow>
        <div class="px-3 py-2">
          <p>
            여기에 장소 목록!   여기에 장소 목록!   여기에 장소 목록!   여기에 장소 목록!   여기에 장소 목록!
          </p>
        </div>
      </b-sidebar>

      <b-sidebar bg-variant="white" id="sidebar-variant3" title="친구" width="400px" shadow>
        <div class="px-3 py-2">
          <p>
            여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!   여기에 친구 목록!
          </p>
        </div>
      </b-sidebar>

      <b-sidebar bg-variant="white" id="sidebar-variant4" title="Test" width="400px" shadow>
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
b-sidebar {
  width: 500px;
}
</style>

<script>
import Profile from '@/views/Profile.vue'

let searchPlace;

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
    },
    onSubmit() {
      searchPlace = this.place;
      this.$dialog.confirm({
        text: `검색한 장소: ${searchPlace}`,
        title: `검색`
        // eslint-disable-next-line no-unused-vars
      }).then(r => console.log(r)).then(r => {
        this.$dialog.notify.info('test notification', {
          position: 'top-right',
          timeout: 5000
        })
      })
      // this.$dialog.confirm({ title: '검색한 장소', text: `입력한 장소는 ${searchPlace}입니다.` })
    }
  }
}
</script>

