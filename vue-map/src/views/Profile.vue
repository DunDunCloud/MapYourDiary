<template>
  <div>
    <div>
      <img :src="$auth.user.picture">
      <h2>{{ $auth.user.nickname }}</h2>
      <p>{{ $auth.user.name }}</p>
      <p>{{ $auth.user.id }}</p>
      <p>{{ $auth.user.email }}</p>
    </div>

<!--    <div>-->
<!--      <pre>{{ JSON.stringify($auth.user, null, 3) }}</pre>-->

<!--    </div>-->
  </div>
</template>

<style>
  img {
    width: 16rem;
    length: auto;
  }
</style>

<script>
export default {
  name: 'Profile'
}
</script>