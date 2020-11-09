<template>
  <div>
    <div>
      <img :src="$auth.user.picture">
      <h2>{{ $auth.user.name }}</h2>
      <p>{{ $auth.user.email }}</p>
      <p>{{ $auth.user.id }}</p>
    </div>

    <div>
      <pre>{{ JSON.stringify($auth.user, null, 3) }}</pre>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile'
}
</script>